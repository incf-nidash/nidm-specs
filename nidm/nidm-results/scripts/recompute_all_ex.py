"""
Create SPM ans FSL examples stored in nidm/nidm-results/ by using the class 
templates available in nidm/nidm-results/terms/templates
@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""
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

def main():
	create_term_examples.main()
	create_spm_example.main()
	create_spm_example_001.main()
	create_spm_example_002.main()
	create_spm_example_003.main()
	create_spm_example_004.main()
	create_spm_example_005.main()
	create_fsl_example.main()
	create_fsl_example_001.main()
	create_fsl_example_002.main()
	create_fsl_example_003.main()

if __name__ == '__main__':
	main()	