#!/usr/bin/env python
'''Common functions for test procedures

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>, Satrajit Ghosh
@copyright: University of Warwick 2014
'''

import os
import re
import urllib2
import rdflib
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

def display_graph(diff_graph, prefix_msg="Difference in:"):
    found_difference = False
    for s,p,o in diff_graph.triples((None,None,None)):
            # workaround to avoid issue with "5853" being a string
            prefix, namespace, name = diff_graph.compute_qname(p)
            if name != "softwareRevision":
                if name != "featVersion":
                    o_name = ""
                    if isinstance(o, rdflib.URIRef):
                        unused, unused, o_name = diff_graph.compute_qname(o)
                    # Ignore prov:Location not specified explicitely
                    if o_name != 'Location':
                        found_difference = True

                        s_str = str(s)
                        if isinstance(s, rdflib.term.URIRef) \
                            and not isinstance(s, rdflib.term.BNode):
                            s_str = diff_graph.qname(s)
                        elif isinstance(s, rdflib.term.Literal):
                            s_str = s_str+" ("+str(s.datatype)+")"
                        p_str = str(p)
                        if isinstance(p, rdflib.term.URIRef) \
                            and not isinstance(p, rdflib.term.BNode):
                            p_str = diff_graph.qname(p)
                        elif isinstance(p, rdflib.term.Literal):
                            p_str = p_str+" ("+str(p.datatype)+")"                        
                        o_str = str(o)
                        if isinstance(o, rdflib.term.URIRef) \
                            and not isinstance(o, rdflib.term.BNode):
                            o_str = diff_graph.qname(o)
                        elif isinstance(o, rdflib.term.Literal):
                            o_str = o_str+" ("+str(o.datatype)+")"    
                                                    
                        logger.info("\t"+prefix_msg+' s='+s_str+\
                                ", p="+p_str+\
                                ", o="+o_str)

    return found_difference

def compare_graphs(graph_doc1, graph_doc2):
    # Use isomorphic to ignore BNode
    iso1 = to_isomorphic(graph_doc1)
    iso2 = to_isomorphic(graph_doc2)

    found_difference = False
    if iso1 != iso2:

        in_both, in_first, in_second = graph_diff(iso1, iso2)

        # diff_graph = (in_first+in_second)
        found_difference_1 = display_graph(in_first, "\t In first: ")
        found_difference_2 = display_graph(in_second, "\t In second: ")
        found_difference = found_difference_1 or found_difference_2
        
                    # break;
    return found_difference

def compare_ttl_documents(ttl_doc1, ttl_doc2):
    # Check whether most recent document is identical to current version
    doc_graph = Graph()
    doc_graph.parse(ttl_doc1, format='turtle')
    same_doc_graph = Graph()

    # This is a fix as sometimes prefixes URIs are lost on the Prov Store 
    # if doc_graph.parse(ttl_doc2) is called directly
    try:
        logger.info(' Opening '+ttl_doc2)
        ttl_doc2_req = urllib2.urlopen(ttl_doc2)
        same_doc_graph.parse(data=ttl_doc2_req.read(), format='turtle')
    except ValueError:
        same_doc_graph.parse(ttl_doc2, format='turtle')

    found_difference = compare_graphs(same_doc_graph, doc_graph)

    # # Use isomorphic to ignore BNode
    # iso1 = to_isomorphic(same_doc_graph)
    # iso2 = to_isomorphic(doc_graph)

    # found_difference = False
    # if iso1 != iso2:

    #     in_both, in_first, in_second = graph_diff(iso1, iso2)

    #     # diff_graph = (in_first+in_second)
    #     found_difference_1 = display_graph(in_first, "\t In first: ")
    #     found_difference_2 = display_graph(in_second, "\t In second: ")
    #     found_difference = found_difference_1 or found_difference_2
        
    #                 # break;
    return found_difference