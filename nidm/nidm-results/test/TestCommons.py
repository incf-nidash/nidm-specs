#!/usr/bin/env python
'''Common functions for test procedures

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>, Satrajit Ghosh
@copyright: University of Warwick 2014
'''

import os
import re
import urllib2, urllib
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
                                os.path.join('spm', 'example003', 'spm_inference_activities.provn'),
                                os.path.join('spm', 'example003', 'spm_results_conjunction.provn'),
                                os.path.join('fsl', 'fsl_results.provn')
                            ]))

# If True turtle file will be downloaded from the prov store using the address specified in the README. 
# If False the turtle version will be retreived on the fly using the prov translator. By default set to True
# to check as README should be up to date but setting to False can be useful for local testing.
ttl_from_readme = False

def get_turtle(provn_file):
    logger.info(' provn file '+provn_file)

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