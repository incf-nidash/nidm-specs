"""
Create SPM example 005 stored in nidm/nidm-results/spm/example005 by using the 
class templates available in nidm/nidm-results/terms/templates

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""
import os
from create_example_from_templates import ExampleFromTemplate

def main():
	nidm_classes = {
		"InferenceUsedNonParam": dict(
			inference_id="niiri:inference_id_1",
			label="Inference",
			alternative_hyp="nidm:OneTailedTest",
			is_parametric="false",
			non_param_dist_id="niiri:non_parametric_dististribution_id"
			),
		"NonParametricDistribution": dict(
			non_param_dist_id="niiri:non_parametric_dististribution_id",
			label="Non-Parametric Distribution",
			n_perms="5000",
			exchangeability_blocks="4"
			)
	}

	NIDM_SPM_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'spm', "example005")
	ttl_file = os.path.join(NIDM_SPM_DIR, 'spm_nonparametric.ttl')
	example = ExampleFromTemplate(nidm_classes, ttl_file, False)
	example.create_example()
	
if __name__ == '__main__':
	main()