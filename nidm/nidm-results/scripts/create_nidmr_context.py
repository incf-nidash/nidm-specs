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
import rdflib

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
    context['@context']['crypto'] = 'http://id.loc.gov/vocabulary/preservation/\cryptographicHashFunctions#'
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
        json_key = str(o)  
        context['@context'][json_key] = OrderedDict()
        if s in owl.ranges:
            context['@context'][json_key]['@id'] = str(s)
            context['@context'][json_key]['@type'] = next(iter(owl.ranges[s]))
        else:
            context['@context'][json_key] = str(s)
        if owl.is_deprecated(s): 
            del context['@context'][json_key]
            
    for json_key in context['@context']:
        if '_' in json_key:
           new_key = json_key.split('_')[1] 
           context['@context'][new_key]=context['@context'].pop(json_key)
                             
            
    # join one path components from terms ans nidmr.json
    ctxfile = os.path.join(NIDMRESULTSPATH, "terms", "nidmr.json")
    with open(ctxfile, 'w+') as c:
        c.write(json.dumps(context, indent=2))

    # Replace double by float and PositiveInteger by int i.e. compatible
    # Python types
    # Suppress boolean and string type 
    
    import re 
    with open(ctxfile, 'r') as c:
        ctxt = c.read()
    ctxt = ctxt.replace('XMLSchema#double', 'XMLSchema#float')
    ctxt = ctxt.replace('XMLSchema#positiveInteger', 'XMLSchema#int')
    ctxt = ctxt.replace('XMLSchema#integer', 'XMLSchema#int')
    ctxt = re.sub(r',\s*\n\s*"@type": "http://www.w3.org/2001/XMLSchema#boolean"', '', ctxt)
    ctxt = re.sub(r',\s*\n\s*"@type": "http://www.w3.org/2001/XMLSchema#string"', '', ctxt)
    with open(ctxfile, 'w+') as c:
        c.write(ctxt)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        owl = sys.argv[1]
    else:
        owl = None

    main(owl)
