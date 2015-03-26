"""
Create SPM example 005 stored in nidm/nidm-results/spm/example005 by using the 
class templates available in nidm/nidm-results/terms/templates

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""
import os
from create_example_from_templates import ExampleFromTemplate

RELPATH = os.path.dirname(os.path.abspath(__file__))

def main():
	nidm_classes = {
		"StatisticMap_PseudoT": dict(
			var_smoothing="[6 6 6]",
			statistic_map_id="niiri:statistic_map_id",
			label="Smoothed Variance T-Statistic Map: passive listening > rest",
			location="file://./SmoothedVarianceTStatistic.nii.gz",
			format="image/nifti",
			filename="SmoothedVarianceTStatistic.nii.gz",
			statistic_type="nidm:SmoothedVarianceTStatistic",
			stat_type_comment="",
			contrast_name="passive listening > rest",
			effect_dof="1",
			sha="799e9bbf8c15b35c0098bca4",
			coordinate_space_id="niiri:coordinate_space_id_1",
			contrast_est_id="niiri:contrast_estimation_id"
			),
		"InferenceUsedNonParam": dict(
			inference_id="niiri:inference_id_1",
			label="Inference",
			alternative_hyp="nidm:OneTailedTest",
			is_parametric="false",
			non_param_dist_id="niiri:non_parametric_null_dististribution_id",
			statistic_map_id="niiri:statistic_map_id"
			),
		"NonParametricDistribution": dict(
			non_param_dist_id="niiri:non_parametric_null_dististribution_id",
			label="Non-Parametric Null Distribution",
			n_perms="5000",
			exchangeability_blocks="4"
			),
		"CoordinateSpace": dict(
			coordinate_space_id="niiri:coordinate_space_id_1",
			label="Coordinate space 1",
			voxel_to_world_mapping="[[-3, 0, 0, 78],[0, 3, 0, -112],[0, 0, 3, -70],[0, 0, 0, 1]]",
			voxel_units="['mm', 'mm', 'mm']",
			voxel_size="[3, 3, 3]",
			coord_system="nidm:MNICoordinateSystem",
			number_of_dim="3",
			dimensions="[53,63,52]")
	}

	NIDM_SPM_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'spm', "example001")
	ttl_file = os.path.join(NIDM_SPM_DIR, 'spm_nonparametric.ttl')
	
	EXT_PATH = os.path.dirname(RELPATH)
	EXTENSION_TPL_DIR = os.path.join(EXT_PATH, "terms", "templates")

	example = ExampleFromTemplate(nidm_classes, ttl_file, False, EXTENSION_TPL_DIR)
	example.create_example()
	
if __name__ == '__main__':
	main()