#!/usr/bin/env python
'''Common functions for test procedures

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>, Satrajit Ghosh
@copyright: University of Warwick 2014
'''

import os
import sys
import re
import vcr
import urllib2
import rdflib
from rdflib.graph import Graph
from rdflib.compare import *
import logging
import signal
import socket
import ssl
import glob

RELPATH = os.path.dirname(os.path.abspath(__file__))

NIDM_RESULTS_PATH = os.path.join(RELPATH, os.pardir)
NIDM_PATH = os.path.join(NIDM_RESULTS_PATH, os.pardir, os.pardir)

# Append parent script directory to path
sys.path.append(os.path.join(NIDM_PATH, "scripts"))
from Constants import NIDM_SOFTWARE_VERSION, FSL_FEAT_VERSION

# Save debug info in a log file (debug.log)
logging.basicConfig(filename='debug.log', level=logging.DEBUG, filemode='w')
logger = logging.getLogger(__name__)
logger.info(' ---------- Debug log ----------')

# Complete examples (used for test queries)
import_test_filenames = set(
    glob.glob(os.path.join(NIDM_RESULTS_PATH, 'spm', '*.ttl')) +
    glob.glob(os.path.join(NIDM_RESULTS_PATH, 'spm', '*', '*.ttl')) +
    glob.glob(os.path.join(NIDM_RESULTS_PATH, 'fsl', '*', '*.ttl')) +
    glob.glob(os.path.join(NIDM_RESULTS_PATH, 'fsl', '*.ttl')) +
    glob.glob(os.path.join(NIDM_RESULTS_PATH, 'afni', '*', '*.ttl')))

# All examples
example_filenames = import_test_filenames.union(set(glob.glob(
    os.path.join(NIDM_RESULTS_PATH, 'test', 'ground_truth', '*', '*.ttl'))))

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

        MAX_RETRY = 15
        retry = 0
        while retry <= MAX_RETRY:
            try:
                logger.info(' urllib2 open ')
                with vcr.use_cassette(
                    os.path.join(NIDM_PATH, 'vcr_cassettes/synopsis.yaml'),
                    record_mode='new_episodes',
                    match_on=['method', 'scheme', 'host', 'port', 'path',
                                  'query', 'body']):
                    response = urllib2.urlopen(req, timeout=10)
            except (socket.timeout, urllib2.URLError, ssl.SSLError):
                # On timeout retry
                retry = retry + 1 
                logger.info('Retry #'+str(retry))
                continue
            break

        if retry > MAX_RETRY:
            raise Exception("Too many retry ("+str(retry)+")")

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
            if p != NIDM_SOFTWARE_VERSION:
                if p != FSL_FEAT_VERSION:
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
                                                    
                        logger.debug("\t"+prefix_msg+' s='+s_str+\
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

class TimeoutError(Exception):
    """Base class for timeout exceptions in this module."""
    pass

def _get_ttl_doc_content(doc):
    logger.info(' Opening '+doc)

    def _raise_timeout(*args):
        raise TimeoutError("end of time")

    if doc.startswith("http"):      
        # Number of retry
        MAX_RETRY = 15
        # Timeout after 5s
        TIMEOUT = 5

        retry = 0
        while retry <= MAX_RETRY:
            try:
                logger.info(' urllib2 open ')
                with vcr.use_cassette(
                        os.path.join(NIDM_PATH, 'vcr_cassettes/synopsis.yaml'),
                        record_mode='new_episodes'):
                    ttl_doc_req = urllib2.urlopen(doc, timeout=TIMEOUT)

                # There is no mechanism to handle timeout on read() in urllib2, 
                # so we need to use a timer
                signal.signal(signal.SIGALRM, _raise_timeout)                
                signal.alarm(TIMEOUT)
                logger.info(' urllib2 read ')
                doc_content = ttl_doc_req.read()
                signal.alarm(0)

            except (socket.timeout, TimeoutError, urllib2.URLError):
                # On timeout retry
                retry = retry + 1 
                logger.info(' Retry #'+str(retry))
                continue
            break

        if retry > MAX_RETRY:
            raise Exception("Too many retry ("+str(retry)+")")

    else:
        # Document locally on disk
        logger.info(' file read ')
        fid = open(doc)
        doc_content = fid.read()

    logger.info('*** ------- > read')
    return doc_content


def compare_ttl_documents(ttl_doc1, ttl_doc2):
    # Check whether most recent document is identical to current version
    doc_graph = Graph()
    doc1 = _get_ttl_doc_content(ttl_doc1)
    doc_graph.parse(data=doc1, format='turtle')
    
    same_doc_graph = Graph()
    doc2 = _get_ttl_doc_content(ttl_doc2)
    same_doc_graph.parse(data=doc2, format='turtle')

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