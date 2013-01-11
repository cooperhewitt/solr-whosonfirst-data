#!/usr/bin/env python

import logging
import sys
import pysolr
import unicodecsv
import machinetag
import bz2

def do_import (options):

    people = options.people

    if options.uncompressed:
        fh = open(people, 'r')
    else:
        fh = bz2.BZ2File(people, 'r')

    reader = unicodecsv.UnicodeReader(fh)
    docs = []

    endpoint = options.solr
    solr = pysolr.Solr(endpoint)

    if options.purge:
        solr.delete(q="collection:imamuseum")

    for row in reader:

        doc = {
            'uri': 'x-urn:imamuseum:id=%s' % row['irn'],
            'collection': 'imamuseum',
            'collection_id': row['irn'],
            'name' : row['display_name']
            }

        for prop in ('birth_date', 'death_date'):

            if row[ prop ] != '':
                parts = row[ prop ].split('-')

                if prop == 'birth_date':
                    doc['year_birth'] = parts[0]
                else:
                    if len(parts) == 1:
                        doc['year_death'] = parts[0]
                    else:
                        doc['year_death'] = parts[1]

        concordances = []

        if row['ulan:id'] != '':
            concordances.append('ulan:id=%s' % row['ulan:id'])

        if len(concordances):
            doc['concordances'] = concordances

        docs.append(doc)

        if len(docs) == 1000:
            solr.add(docs)
            docs = []

    if len(docs) == 1000:
        solr.add(docs)
        docs = []

    solr.optimize()

if __name__ == '__main__':

    import optparse

    parser = optparse.OptionParser()
    parser.add_option("-p", "--people", dest="people", action="store", help="path of the list of people to import")
    parser.add_option("-s", "--solr", dest="solr", action="store", help="your solr endpoint; default is http://localhost:8983/solr/whosonfirst", default="http://localhost:8983/solr/whosonfirst")
    parser.add_option("-u", "--uncompressed", dest="uncompressed", action="store_true", help="a flag to indicate whether the list of people has been uncompressed; default is false", default=False)
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", help="enable chatty logging; default is false", default=False)
    parser.add_option("--purge", dest="purge", action="store_true", help="purge all your existing bookmarks before starting the import; default is false", default=False)

    (opts, args) = parser.parse_args()

    if opts.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    do_import(opts)
