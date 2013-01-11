import machinetag

def generate_concordances_machinetags(concordances):

    machinetags = []

    for c in concordances:
        mt = machinetag.machinetag(c)
        machinetags.extend(mt.magic_8s())

    return machinetags

def generate_concordances_machinetags_hierarchy(concordances):

    hierarchies = []

    for c in concordances:
        mt = machinetag.machinetag(c)
        c = "%s/%s/%s" % (mt.namespace(), mt.predicate(), mt.value())

        hierarchies.append(c)

    return hierarchies
