#!/usr/bin/env python
'''Common functions for test procedures

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>, Satrajit Ghosh
@copyright: University of Warwick 2014
'''

import os
import re
import urllib2, urllib
from rdflib.graph import Graph
from rdflib.compare import *
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Examples used for unit testing
import_test_filenames = set([
                                os.path.join('spm', 'example001', 'example001_spm_results.provn'),
                                os.path.join('fsl', 'example001', 'fsl_nidm.provn')
                            ])
# All examples
example_filenames = import_test_filenames.union(set([
                                os.path.join('spm', 'spm_results.provn') , 
                                os.path.join('spm', 'example002', 'spm_results_2contrasts.provn'),
                                os.path.join('spm', 'example003', 'spm_results_conjunction.provn'),
                                os.path.join('spm', 'example004', 'spm_inference_activities.provn'),
                                os.path.join('fsl', 'fsl_results.provn')
                            ]))


# If True turtle file will be downloaded from the prov store using the address specified in the README. 
# If False the turtle version will be retreived on the fly using the prov translator. By default set to True
# to check as README should be up to date but setting to False can be useful for local testing.
ttl_from_readme = False

def get_turtle(provn_file):
    if ttl_from_readme:
        # Get URL of turtle from README file
        readme_file = os.path.join(os.path.dirname(provn_file), 'README')
        readme_file = open(readme_file, 'r')
        readme_txt = readme_file.read()
        turtle_search = re.compile(r'.*turtle: (?P<ttl_file>.*\.ttl).*')
        extracted_data = turtle_search.search(readme_txt) 
        ttl_file_url = extracted_data.group('ttl_file');
    else:
        # Open corresponding provn file
        logger.info(' Converting '+provn_file)
        provn_file = open(provn_file, 'r')
        ex_provn = provn_file.read()

        # Convert to turtle using Prov Translator APIs
        url = "https://provenance.ecs.soton.ac.uk/validator/provapi/documents/"
        headers = { 'Content-type' : "text/provenance-notation",
                    'Accept' : "text/turtle" }
        req = urllib2.Request(url, ex_provn, headers)
        response = urllib2.urlopen(req)
        ttl_file_url = response.geturl()

    logger.info(' Loading turtle file '+ttl_file_url)

    return ttl_file_url

def merge_exception_dict(excep_dict, other_except_dict):
    merged_dict = dict(excep_dict.items() + other_except_dict.items())
    # When key is in both dictionaries, we need to merge the set manually
    for key in list(set(excep_dict.keys()) & set(other_except_dict.keys())):
        merged_dict[key] = excep_dict[key].union(other_except_dict[key])

    return merged_dict

def compare_ttl_documents(ttl_doc1, ttl_doc2, prefix_uri_from_first=False):
    # Check whether most recent document is identical to current version
    doc_graph = Graph()
    doc_graph.parse(ttl_doc1)
    same_doc_graph = Graph()

    try:
        # This is a fix as sometimes prefixes URIs are lost on the Prov Store 
        # if doc_graph.parse(ttl_doc2) is called directly
        logger.info(' Opening '+ttl_doc2)
        ttl_doc2_req = urllib2.urlopen(ttl_doc2)
        same_doc_graph.parse(data=ttl_doc2_req.read(), format='turtle')
    except urllib2.HTTPError:
        return False
    except ValueError:
        same_doc_graph.parse(ttl_doc2, format='turtle')

    # Use isomorphic to ignore BNode
    iso1 = to_isomorphic(same_doc_graph)
    iso2 = to_isomorphic(doc_graph)

    found_difference = False
    if iso1 != iso2:

        in_both, in_first, in_second = graph_diff(iso1, iso2)

        diff_graph = (in_first+in_second)

        for s,p,o in diff_graph.triples((None,None,None)):
            # workaround to avoid issue with "5853" being a string
            if iso1.qname(p) != "spm:softwareRevision":
                if iso1.qname(p) != "fsl:featVersion":
                    found_difference = True
                    logger.info('\tDifference in: s='+str(s)+\
                        ", p="+str(p)+\
                        ", o="+o)
                    # break;
    return found_difference