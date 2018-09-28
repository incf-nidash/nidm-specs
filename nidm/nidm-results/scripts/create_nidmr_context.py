"""
Create csv file listing preferred prefixes for NIDM terms
@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2015
"""

import os
import sys
import glob
import json
from collections import OrderedDict

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)
NIDMPATH = os.path.join(NIDMRESULTSPATH, os.pardir)

# Append parent script directory to path
sys.path.append(os.path.join(NIDMRESULTSPATH, os.pardir, os.pardir, "scripts"))
from nidmresults.owl.owl_reader import *
from nidmresults.objects.constants_rdflib import *

logging.basicConfig(filename='debug.log', level=logging.DEBUG, filemode='w')
logger = logging.getLogger(__name__)


def main(owl=None):
    if owl is None:
        owl = os.path.join(NIDMRESULTSPATH, "terms",
                           "nidm-results.owl")

    owl_imports = glob.glob(
        os.path.join(os.path.dirname(owl),
                     os.pardir, os.pardir, "imports", '*.ttl'))

    owl_reader = OwlReader(owl, import_owl_files=owl_imports)

    prefix_file = os.path.join(
        os.path.dirname(__file__), '..', 'terms', 'prefixes.csv')
    context = OrderedDict()
    context['@context'] = OrderedDict()
    context['@context']['@version'] = 1.1
    context['@context']['records'] = OrderedDict()
    context['@context']['records']['@container'] = "@type"
    context['@context']['records']['@id'] = "@graph"
    context['prov'] = 'http://www.w3.org/ns/prov#'
    context['nidm'] = 'http://purl.org/nidash/nidm#'
    context['niiri'] = 'http://iri.nidash.org/'
    context['afni'] = 'http://purl.org/nidash/afni#'
    context['spm'] = 'http://purl.org/nidash/spm#'
    context['fsl'] = 'http://purl.org/nidash/fsl#'
    context['rdfs'] = 'http://www.w3.org/2000/01/rdf-schema#'
    context['crypto'] = 'http://id.loc.gov/vocabulary/preservation/\
cryptographicHashFunctions#'
    context['dc'] = 'http://purl.org/dc/elements/1.1/'
    context['dct'] = 'http://purl.org/dc/terms/'
    context['owl'] = 'http://www.w3.org/2002/07/owl#'
    context['xsd'] = 'http://www.w3.org/2001/XMLSchema#'
    context['obo'] = 'http://purl.obolibrary.org/obo/'
    context['nfo'] = 'http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#'
    context['scr'] = 'http://scicrunch.org/resolver/'
    context['nlx'] = 'http://uri.neuinfo.org/nif/nifstd/'
    context['skos'] = 'http://www.w3.org/2004/02/skos/core#'

    with open(prefix_file) as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # skip the headers
        for alphanum_id, prefix, uri in reader:
            context['@context'][prefix] = OrderedDict()
            context['@context'][prefix]['@id'] = uri
            context['@context'][prefix]['@type'] = '@id'
    with open(os.path.join(NIDMRESULTSPATH, "terms", "nidmr.json"), 'w+') as c:
        c.write(json.dumps(context, indent=2))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        owl = sys.argv[1]
    else:
        owl = None

    main(owl)
