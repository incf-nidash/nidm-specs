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

    owl = OwlReader(owl, import_owl_files=owl_imports)

    prefix_file = os.path.join(
        os.path.dirname(__file__), '..', 'terms', 'prefixes.csv')
    context = OrderedDict()
    context['@context'] = OrderedDict()
    context['@context']['@version'] = 1.1
    context['@context']['records'] = OrderedDict()
    context['@context']['records']['@container'] = "@type"
    context['@context']['records']['@id'] = "@graph"
    context['@context']['prov'] = 'http://www.w3.org/ns/prov#'
    context['@context']['nidm'] = 'http://purl.org/nidash/nidm#'
    context['@context']['niiri'] = 'http://iri.nidash.org/'
    context['@context']['afni'] = 'http://purl.org/nidash/afni#'
    context['@context']['spm'] = 'http://purl.org/nidash/spm#'
    context['@context']['fsl'] = 'http://purl.org/nidash/fsl#'
    context['@context']['rdfs'] = 'http://www.w3.org/2000/01/rdf-schema#'
    context['@context']['crypto'] = 'http://id.loc.gov/vocabulary/preservation/\
cryptographicHashFunctions#'
    context['@context']['dc'] = 'http://purl.org/dc/elements/1.1/'
    context['@context']['dct'] = 'http://purl.org/dc/terms/'
    context['@context']['owl'] = 'http://www.w3.org/2002/07/owl#'
    context['@context']['xsd'] = 'http://www.w3.org/2001/XMLSchema#'
    context['@context']['obo'] = 'http://purl.obolibrary.org/obo/'
    context['@context']['nfo'] = 'http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#'
    context['@context']['scr'] = 'http://scicrunch.org/resolver/'
    context['@context']['nlx'] = 'http://uri.neuinfo.org/nif/nifstd/'
    context['@context']['skos'] = 'http://www.w3.org/2004/02/skos/core#'

    #     sep = \
    #         '#################################################################'

    #     with open(self.file, 'r') as fp:
    #         owl_txt = fp.read()
    # For anything that has a label
    for s, o in sorted(owl.graph.subject_objects(SKOS['prefLabel'])):
        print(str(s))
        print(str(o))
        print('---')
        context['@context'][str(o)] = OrderedDict()
        context['@context'][str(o)]['@id'] = str(s)
        context['@context'][str(o)]['@type'] = '@id'
        # try:
        #     owl.graph.qname(s)
        # except Exception:
        #     # Some URIs don't have qname
        #     # (e.g. http://www.w3.org/ns/prov-o#)
        #     continue
        # prefix = owl.get_preferred_prefix(s)

        # if prefix is not None:
        #     # Add prefix as preferred label in the owl file
        #     preflabel = str('<' + str(s) + '> ' +
        #                     '<' + str(SKOS.prefLabel) + '> ' +
        #                     '"' + prefix + '" . \n')
        #     owl_txt = owl_txt.replace(sep, preflabel + sep, 1)

    #     with open(owl.file, 'w') as fp:
    #         fp.write(owl_txt)

    # with open(prefix_file) as csvfile:
    #     reader = csv.reader(csvfile)
    #     next(reader, None)  # skip the headers
    #     for alphanum_id, prefix, uri in reader:
    #         context['@context'][prefix] = OrderedDict()
    #         context['@context'][prefix]['@id'] = uri
    #         context['@context'][prefix]['@type'] = '@id'
    with open(os.path.join(NIDMRESULTSPATH, "terms", "nidmr.json"), 'w+') as c:
        c.write(json.dumps(context, indent=2))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        owl = sys.argv[1]
    else:
        owl = None

    main(owl)
