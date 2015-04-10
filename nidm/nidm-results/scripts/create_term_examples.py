"""
Create examples for each NIDM class in nidm/nidm-results/terms/examples
by using the class templates available in nidm/nidm-results/terms/templates

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""
import os
from create_example_from_templates import ExampleFromTemplate

import sys

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)
# Append parent script directory to path
sys.path.append(os.path.join(NIDMRESULTSPATH, os.pardir, os.pardir, "scripts"))
from Constants import STATO_OLS_STR, STATO_OLS_LABEL, STATO_TSTATISTIC_STR, \
	STATO_TSTATISTIC_LABEL

def main():
	nidm_classes = {
		"DesignMatrix": dict(
			design_matrix_id='niiri:design_matrix_id', 
			label="Design Matrix", 
			location="file:///path/to/DesignMatrix.csv",
			format="text/csv", 
			filename="DesignMatrix.csv", 
			design_matrix_png_id="niiri:design_matrix_png_id"),
		"Image-DesignMatrix": dict(
			image_id="niiri:design_matrix_png_id",
			location="file://./DesignMatrix.png",
			filename="DesignMatrix.png",
			format="image/png"
			),
		"Data": dict(
			data_id='niiri:data_id',
			label="Data",
			scaling="true",
			target=100
			),
		"ErrorModel": dict(
			error_model_id="niiri:error_model_id",
			noise_distribution="nidm:GaussianDistribution",
			variance_homo="true",
			variance_spatial="nidm:SpatiallyLocalModel",
			dependence="nidm:IndependentError",
			dependence_spatial="nidm:SpatiallyLocalModel"
			),
		"ModelParametersEstimation": dict(
			model_pe_id="niiri:model_pe_id",
			label="Model parameters estimation",
			est_method=STATO_OLS_STR,
			est_method_comment=STATO_OLS_LABEL,
			software_id="niiri:software_id",
			design_matrix_id="niiri:design_matrix_id",
			data_matrix_id="niiri:data_id",
			error_model_id="niiri:error_model_id"
			),
		"ParameterEstimateMap": dict(
			beta_map_id="niiri:beta_map_id_1",
			label="Beta Map 1",
			location="file:///path/to/ParameterEstimate_0001.nii.gz",
			filename="ParameterEstimate_0001.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			param_est_id="niiri:model_pe_id"),
		"ResidualMeanSquaresMap": dict(
			residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
			label="Residual Mean Squares Map",
			location="file:///path/to/ResidualMeanSquares.nii.gz",
			filename="ResidualMeanSquares.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			param_est_id="niiri:model_pe_id"),
		"MaskMap": dict(
			mask_id="niiri:mask_id_2",
			user_defined="false",
			label="Mask",
			location="file:///path/to/Mask.nii.gz",
			filename="Mask.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			used_by_act_id="niiri:model_pe_id"),
		"ContrastWeights": dict(
			contrast_id="niiri:contrast_id",
			label="Contrast: Listening > Rest",
			value="[1, 0, 0]",
			statistic_type=STATO_TSTATISTIC_STR,
			stat_type_comment=STATO_TSTATISTIC_LABEL,
			contrast_name="listening > rest"),
		"ContrastEstimation": dict(
			contrast_estimation_id="niiri:contrast_estimation_id",
			label="Contrast estimation",
			software_id="niiri:software_id",
			mask_id="niiri:mask_id_2",
			residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
			design_matrix_id="niiri:design_matrix_id",
			contrast_id="niiri:contrast_id",
			param_est_map="niiri:beta_map_id_1"),
		"ContrastMap": dict(
			contrast_map_id="niiri:contrast_map_id",
			label="Contrast Map: listening > rest",
			location="file:///path/to/Contrast.nii.gz",
			format="image/nifti",
			filename="Contrast.nii.gz",
			contrast_name="listening > rest",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			contrast_est_id="niiri:contrast_estimation_id"),
		"ContrastStandardErrorMap": dict(
			contrast_standard_error_map_id="niiri:contrast_standard_error_map_id",
			label="Contrast Standard Error Map",
			location="file:///path/to/ContrastStandardError.nii.gz",
			format="image/nifti",
			filename="ContrastStandardError.nii.gz",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			contrast_est_id="niiri:contrast_estimation_id"),
		"StatisticMap_T": dict(
			statistic_map_id="niiri:statistic_map_id",
			label="Statistic Map: listening > rest",
			location="file:///path/to/TStatistic.nii.gz",
			format="image/nifti",
			filename="TStatistic.nii.gz",
			statistic_type=STATO_TSTATISTIC_STR,
			stat_type_comment=STATO_TSTATISTIC_LABEL,
			contrast_name="listening > rest",
			error_dof="72.9999999990787",
			effect_dof="1",
			sha="e43b6e01b0463fe7d40782137867a...",
			coordinate_space_id="niiri:coordinate_space_id_1",
			contrast_est_id="niiri:contrast_estimation_id"),
		"HeightThreshold_P": dict(
			height_threshold_id="niiri:height_threshold_id",
			label="Height Threshold: p<0.05 (FWE)",
			value="5.23529984739211",
			thresh_type="p-value FWE",
			p_unc="7.62276079258051e-07",
			p_fwe="0.05"
			),
		"ExtentThreshold": dict(
			extent_threshold_id="niiri:extent_threshold_id",
			label="Extent Threshold: k>=0",
			cluster_size_vox="0",
			cluster_size_resels="0",
			p_unc="1",
			p_fwe="1"
			),
		"SPM_ReselsPerVoxelMap": dict(
			resels_per_voxel_map_id="niiri:resels_per_voxel_map_id",
			label="Resels per Voxel Map",
			location="file:///path/to/ReselsPerVoxel.nii.gz",
			filename="ReselsPerVoxel.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			model_pe_id="niiri:model_pe_id"
			),
		"ClusterLabelsMap": dict(
			cluster_label_map_id="niiri:cluster_label_map_id",
			location="file:///path/to/ClusterLabels.nii.gz",
			filename="ClusterLabels.nii.gz",
			format="image/nifti"
			),
		"DisplayMaskMap": dict(
			display_map_id="niiri:display_map_id",
			label="Display Mask Map",
			location="file:///path/to/DisplayMask.nii.gz",
			filename="DisplayMask.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_2",
			sha="e43b6e01b0463fe7d40782137867a..."
			),
		"PeakDefinitionCriteria_MaxPeaks": dict(
			peak_definition_criteria_id="niiri:peak_definition_criteria_id",
			label="Peak Definition Criteria",
			max_num_peaks="3",
			min_dist_peaks="8.0"
			),
		"ClusterDefinitionCriteria": dict(
			cluster_definition_criteria_id="niiri:cluster_definition_criteria_id",
			label="Cluster Connectivity Criterion: 18",
			connectivity="nidm:voxel18connected"
			),
		"Inference": dict(
			inference_id="niiri:inference_id",
			label="Inference",
			alternative_hyp="nidm:OneTailedTest",
			stat_map_id="niiri:statistic_map_id", 
			height_thresh_id="niiri:height_threshold_id", 
			extent_thresh_id="niiri:extent_threshold_id", 
			inference_mask_id="niiri:mask_id_3", 
			display_mask_id="niiri:display_map_id", 
			mask_id="niiri:mask_id", 
			software_id="niiri:software_id",
			peak_def_id="niiri:peak_definition_criteria_id", 
			cluster_def_id="niiri:cluster_definition_criteria_id"
			),
		"ExcursionSetMap": dict(
			id="niiri:excursion_set_map_id",
			label="Excursion Set Map",
			location="file:///path/to/ExcursionSetMap.nii.gz",
			format="image/nifti",
			filename="ExcursionSetMap.nii.gz",
			cluster_label_map_id="niiri:cluster_label_map_id",
			max_intensity_projection_id="niiri:maximum_intensity_projection_id",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			num_of_clusters="8",
			p_value="8.95949980872501e-14",
			inference_id="niiri:inference_id"
			),
		"SignificantCluster": dict(
			cluster_id="niiri:significant_cluster_0001",
			label="Significant Cluster 0001",
			cluster_size_in_voxels="530",
			cluster_label_id="1",
			cluster_size_in_resels="23.1209189500945",
			p_value_unc="9.56276736481136e-52",
			p_value_fwe="0",
			p_value_fdr="7.65021389184909e-51",
			excursion_set_id="niiri:excursion_set_map_id"
			),
		"Peak_ValueP": dict(
			peak_id="niiri:peak_0001",
			label="Peak 0001",
			location="niiri:coordinate_0001",
			value="13.9346199035645",
			equiv_z="INF",
			p_uncorr="4.44089209850063e-16",
			p_value_fwe="0",
			p_value_fdr="6.3705194444993e-11",
			cluster_id="niiri:significant_cluster_0001"
			),
		"Coordinate": dict(
			coordinate_id="niiri:coordinate_0001",
			label="Coordinate: 0001",
			coord="[-60, -28, 13]"
			),
		"SearchSpaceMaskMap": dict(
			search_space_id="niiri:search_space_mask_id",
			location="file:///path/to/SearchSpaceMask.nii.gz",
			filename="SearchSpaceMask.nii.gz",
			label="Search Space Mask Map",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_2",
			expected_num_voxels="0.553331387916112",
			expected_num_clusters="0.0889172687960151",
			height_critical_fwe05="5.23529984739211",
			height_critical_fdr05="6.22537899017334",
			smallest_size_fwe05="1",
			smallest_size_fdr05="3",
			search_vol_voxels="65593",
			search_vol_units="1771011",
			resel_size="22.9229643140043",
			search_vol_resels="2552.68032521656",
			search_vol_resels_geom="[3, 72.3216126440484, 850.716735116472, 2552.68032521656]",
			noise_fwhm_in_voxels="[2.95881189165801, 2.96628446669584, 2.61180425626264]",
			noise_fwhm_in_units="[8.87643567497404, 8.89885340008753, 7.83541276878791]",
			random_field_station="false",
			sha="e43b6e01b0463fe7d40782137867a...",
			inference_id="niiri:inference_id"
			),
		"FSL_ClusterCenterOfGravity": dict(
			center_of_gravity_id="niiri:center_of_gravity_1",
			location="niiri:coordinate_0001",
			label="Center of gravity",
			cluster_id="niiri:significant_cluster_0001",
			),
		"FSL_ClusterMaximumStatistic": dict(
			peak_id="niiri:cluster_max_statistic_0001",
			label="Cluster Maximum Statistic",
			location="niiri:coordinate_0001",
			p_uncorr="0.00085796235",
			equiv_z="3.135447",
			cluster_id="niiri:significant_cluster_0001"
			),
		"CoordinateSpace": dict(
			coordinate_space_id="niiri:coordinate_space_id_1",
			label="Coordinate space 1",
			voxel_to_world_mapping="[[-3, 0, 0, 78],[0, 3, 0, -112],[0, 0, 3, -50],[0, 0, 0, 1]]",
			voxel_units="['mm', 'mm', 'mm']",
			voxel_size="[3, 3, 3]",
			coord_system="nidm:MNICoordinateSystem",
			number_of_dim="3",
			dimensions="[53,63,46]"),
		"Image": dict(
			image_id="niiri:maximum_intensity_projection_id",
			location="file:///path/to/MaximumIntensityProjection.png",
			filename="MaximumIntensityProjection.png",
			format="image/png"
			),
		"GrandMeanMap": dict(
			grand_mean_map_id="niiri:grand_mean_map_id",
			label="Grand Mean Map",
			location="file:///path/to/GrandMean.nii.gz",
			filename="GrandMean.nii.gz",
			format="image/nifti",
			masked_median="115",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			model_pe_id="niiri:model_pe_id"
			),
		"SPM_DriftModel": dict(
			id="niiri:drift_model_id",
			label="SPM's DCT Drift Model",
			cut_off="2"
			),
		"FSL_DriftModel": dict(
			id="niiri:drift_model_id",
			label="FSL's Gaussian Running Line Drift Model",
			cut_off="2"
			)
		}

	NIDM_TERMS_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'terms')
	EX_DIR = os.path.join(NIDM_TERMS_DIR, 'examples')
	example = ExampleFromTemplate(nidm_classes, EX_DIR, True)
	example.create_example()

if __name__ == '__main__':
	main()