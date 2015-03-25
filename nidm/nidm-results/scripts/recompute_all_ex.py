"""
Create SPM ans FSL examples stored in nidm/nidm-results/ by using the class 
templates available in nidm/nidm-results/terms/templates
@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""
import logging
import os, sys

import create_term_examples
import create_spm_example
import create_spm_example_001
import create_spm_example_002
import create_spm_example_003
import create_spm_example_004
import create_spm_example_005
import create_fsl_example
import create_fsl_example_001
import create_fsl_example_002
import create_fsl_example_003

logging.basicConfig(filename='debug.log', level=logging.DEBUG, filemode='w')
logger = logging.getLogger(__name__)
RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDM_RES_PATH = os.path.dirname(RELPATH)

# Append non-parametric script directory to path
sys.path.append(os.path.join(NIDM_RES_PATH, "extensions", "non_parametric", \
	"scripts"))
import create_spm_example_nonparam

def main():
	logger.debug(" create_term_examples")
	create_term_examples.main()
	logger.debug(" create_spm_example")
	create_spm_example.main()
	logger.debug(" create_spm_example_001")
	create_spm_example_001.main()
	logger.debug(" create_spm_example_002")
	create_spm_example_002.main()
	logger.debug(" create_spm_example_003")
	create_spm_example_003.main()
	logger.debug(" create_spm_example_004")
	create_spm_example_004.main()
	logger.debug(" create_spm_example_005")
	create_spm_example_005.main()
	logger.debug(" create_fsl_example")
	create_fsl_example.main()
	logger.debug(" create_fsl_example_001")
	create_fsl_example_001.main()
	logger.debug(" create_fsl_example_002")
	create_fsl_example_002.main()
	logger.debug(" create_fsl_example_003")
	create_fsl_example_003.main()

	# Extensions
	create_spm_example_nonparam.main()

if __name__ == '__main__':
	main()	