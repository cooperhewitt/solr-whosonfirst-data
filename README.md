solr-whosonfirst-data
==

Data files and scripts for working with the
[solr-whosonfirst](https://github.com/cooperhewitt/solr-whosonfirst)
repository.

data
--

Sample data files are available from the following sources:

* [Cooper-Hewitt National Design Museum](https://github.com/cooperhewitt/collection/)

* [Indianopolis Museum of Art](https://github.com/IMAmuseum/ima-collection)

* [Open Library (authors)](http://openlibrary.org/developers/dumps)

* Walker Arts Center

Please note that the data in these files is not standardized. There are source
specific tools for importing each dataset in the `bin` directory.

In some cases the data here is a subset of the data that the source itself
publishes. For example, the Open Library dataset only contains authors and IDs
since there are so many of them (approxiamately 7M).

Additional datasets will be added as time and circumstances (and pull requests)
permit. We're looking at you, Wikipedia.

bin
--

Because of the size of the data the scripts below assume that the input files
are bzip2 encoded and uncompressed (and processed) on the fly.

### import-cooperhewitt.py

	$> ./bin/import-cooperhewitt.py -p ./data/people-cooperhewitt.csv.bz2

### import-imamuseum.py

	$> ./bin/import-imamuseum.py -p ./data/people-imamuseum.csv.bz2

### import-openlibrary.py

	$> ./bin/import-openlibrary.py -p ./data/people-openlibrary.csv.bz2

### import-walkerarts.py

	$> ./bin/import-walkerarts.py -p ./data/people-walkerarts.csv.bz2

See also
--

* [solr-whosonfirst](https://github.com/cooperhewitt/solr-whosonfirst)
