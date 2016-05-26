#!/usr/bin/env python
'''Test that NIDM-Results terms README is consistent with nidm-results.owl

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>, Satrajit Ghosh
@copyright: University of Warwick 2014
'''
import unittest
import os
import sys
from nidmresults.test.test_commons import *
import difflib

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDM_RESULTS_PATH = os.path.dirname(RELPATH)

# Append parent script directory to path
RELPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(RELPATH, os.pardir, os.pardir, os.pardir, "scripts"))
from Constants import *


# Add scripts folder
path = os.path.join(NIDM_RESULTS_PATH, "scripts")
sys.path.append(path)

NIDM_RESULTS_TERMS_PATH = os.path.join(NIDM_RESULTS_PATH, "terms")

from UpdateTermReadme import UpdateTermReadme

class TestTermsReadmeMatchVocabulary(unittest.TestCase):

    def setUp(self):
        logger.info("Test: TestTermsReadmeMatchVocabulary")

    def test_check_consistency(self):
        readme_file = os.path.join(NIDM_RESULTS_TERMS_PATH, 'README.md')
        readme_file_open = open(readme_file, 'r')
        original_readme_txt = readme_file_open.read()
        readme_file_open.close()

        # Retreive owl file for NIDM-Results
        owl_file = os.path.join(NIDM_RESULTS_TERMS_PATH, 'nidm-results.owl')
        updateReadme = UpdateTermReadme(owl_file)
        updateReadme.update_readme(readme_file)

        readme_file_open = open(readme_file, 'r')
        updated_readme_txt = readme_file_open.read()
        readme_file_open.close()

        if not (updated_readme_txt == original_readme_txt):
            original_readme_lines = original_readme_txt.splitlines()
            updated_readme_lines = updated_readme_txt.splitlines()
            diff = difflib.unified_diff(original_readme_lines, updated_readme_lines)
            logger.debug('\n'.join(diff))

            error_msg = "Term README outdated, please update README.md using nidm/nidm-results/scripts/UpdateTermReadme.py"
            # Write back original text found in README           
            readme_file_open = open(readme_file, 'w')
            readme_file_open.write(original_readme_txt)
            readme_file_open.close()

            readme_file_open.close()
            raise Exception(error_msg)

if __name__ == '__main__':
    unittest.main()
