"""
Create FSL examples stored in nidm/nidm-results/fsl by using the class 
templates available in nidm/nidm-results/terms/templates

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
from Constants import STATO_GLS_STR, STATO_GLS_LABEL, STATO_TSTATISTIC_STR, \
	STATO_ZSTATISTIC_STR, STATO_TSTATISTIC_LABEL, STATO_ZSTATISTIC_LABEL

def main():
	nidm_classes = {
		"DesignMatrix": dict(
			design_matrix_id='niiri:design_matrix_id', 
			label="Design Matrix", 
			location="file://./DesignMatrix.csv",
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
			target="10000"
			),
		"ErrorModel": dict(
			error_model_id="niiri:error_model_id",
			noise_distribution="nidm:GaussianDistribution",
			variance_homo="true",
			variance_spatial="nidm:SpatiallyLocalModel",
			dependence="nidm:SeriallyCorrelatedError",
			dependence_spatial="nidm:SpatiallyRegularizedModel"
			),
		"ModelParametersEstimation": dict(
			model_pe_id="niiri:model_parameters_estimation_id",
			label="Model Parameters Estimation",
			est_method=STATO_GLS_STR,
			est_method_comment=STATO_GLS_LABEL,
			design_matrix_id="niiri:design_matrix_id",
			data_matrix_id="niiri:data_id",
			error_model_id="niiri:error_model_id",
			software_id="niiri:software_id"
			),
		"FSL_ParameterEstimateMapNoLocation-1": dict(
			beta_map_id="niiri:beta_map_id_1",
			label="Parameter estimate 1",
			filename="pe1.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			param_est_id="niiri:model_parameters_estimation_id"),
		"FSL_ParameterEstimateMapNoLocation-2": dict(
			beta_map_id="niiri:beta_map_id_2",
			label="Parameter estimate 2",
			filename="pe2.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			param_est_id="niiri:model_parameters_estimation_id"),
		"FSL_ParameterEstimateMapNoLocation-3": dict(
			beta_map_id="niiri:beta_map_id_3",
			label="Parameter estimate 3",
			filename="pe3.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			param_est_id="niiri:model_parameters_estimation_id"),
		"FSL_ParameterEstimateMapNoLocation-4": dict(
			beta_map_id="niiri:beta_map_id_4",
			label="Parameter estimate 4",
			filename="pe4.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			param_est_id="niiri:model_parameters_estimation_id"),
		"CoordinateSpace": dict(
			coordinate_space_id="niiri:coordinate_space_id_1",
			label="Coordinate space",
			voxel_to_world_mapping="[[ -3.5, 0, 0, 108.5], [ 0, 3.5, 0, -108.5], [ 0, 0, 3.5, -52.5], [ 0, 0, 0, 1]]",
			voxel_units="['mm', 'mm', 'mm']",
			voxel_size="[3.5, 3.5, 3.5]",
			coord_system="nidm:SubjectCoordinateSystem",
			number_of_dim="3",
			dimensions="[64, 64, 42]"),
		"FSL_ResidualMeanSquaresMap": dict(
			residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
			label="Residual Mean Squares Map",
			location="file://./ResidualMeanSquares.nii.gz",
			filename_1="ResidualMeanSquares.nii.gz",
			filename_2="sigmasquareds.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="1327a300eb1e20d42c67abb3c49a47b80ecabfebd13d0ba0aca0560e8bf43891f0e35a958c1afa84e041f62cf0038f58b4ab71f68b0b50d4153210aeed74f4ff",
			param_est_id="niiri:model_parameters_estimation_id"),
		"MaskMap_Analysis_fileName": dict( # Analysis mask
			mask_id="niiri:mask_id_1",
			label="Mask",
			location="file://./Mask.nii.gz",
			filename="Mask.nii.gz", 
			filename_2="mask.nii.gz", 
			user_defined="false",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="cc1a96a6111e5107eb08487e38e6d7f8164b9d1d3f1fc10948bdbcfaea642fe9bfae278c7fc372b65cac7232ea58fd8fb5914014e7b9a5d6200592b12b2a728b",
			generated_by_act_id="niiri:model_parameters_estimation_id",
			used_by_act_id="niiri:contrast_estimation_id_1"),
		"ContrastWeights": dict(
			contrast_id="niiri:contrast_id_1",
			label="Contrast Weights: Generation",
			value="[1, 0, 0, 0]",
			statistic_type=STATO_TSTATISTIC_STR,
			stat_type_comment=STATO_TSTATISTIC_LABEL,
			contrast_name="Generation"
			),
		"ContrastEstimation": dict(
			contrast_estimation_id="niiri:contrast_estimation_id_1",
			label="Contrast estimation: Generation",
			software_id="niiri:software_id",
			mask_id="niiri:mask_id_1",
			residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
			design_matrix_id="niiri:design_matrix_id",
			contrast_id="niiri:contrast_id_1",
			param_est_map="niiri:beta_map_id_1"
			),
		"FSL_ContrastMap": dict(
			contrast_map_id="niiri:contrast_map_id_1",
			label="Contrast Map: Generation",
			location="file://./Contrast.nii.gz",
			format="image/nifti",
			filename_1="Contrast.nii.gz",
			filename_2="cope1.nii.gz",
			contrast_name="Generation",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="4c755c0ae6088f8001e0458f89e51fea0e2719b5dc747fed6f617ae12ad5c6a643e1afcb886bcabaaac7911f5e69086c1bd084af9f75dae75913d44a783151f6",
			contrast_est_id="niiri:contrast_estimation_id_1"),
		"ContrastStandardErrorMap": dict(
			contrast_standard_error_map_id="niiri:contrast_standard_error_map_id_1",
			label="Contrast Standard Error Map",
			location="file://./ContrastStandardError.nii.gz",
			format="image/nifti",
			filename="ContrastStandardError.nii.gz",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="8529f3ff9f10da8f332ced9d579990321475c1498b56d79ede560ba2eccf6d68718757dc7af78eb1e86617a41e6c9f55161f756d184e2b0fb06c3d419dc99856",
			contrast_est_id="niiri:contrast_estimation_id_1"),
		"DerivedMap-ContrastVariance": dict(
			derived_from_map_id="niiri:d4de4b20b2d408cd8d825ac0edb6030a",
			derived_map_type="fsl:ContrastVarianceMap",
			filename="varcope1.nii.gz",
			format="image/nifti",
			sha="7d183bbacc0b99cd1db84174d32445457f532bca9f774fdcc53bc1d0faa5e7d250a1abf03864bd90b30f96f5a7516e0056104a729a565019b0f254a8a7bced1e",
			map_id="niiri:contrast_standard_error_map_id_1"
			),
		"FSL_StatisticMap": dict(
			statistic_map_id="niiri:statistic_map_id_1",
			label="Statistic Map: Generation",
			location="file://./TStatistic.nii.gz",
			format="image/nifti",
			filename_1="TStatistic.nii.gz",
			filename_2="tstat1.nii.gz",
			statistic_type=STATO_TSTATISTIC_STR,
			stat_type_comment=STATO_TSTATISTIC_LABEL,
			contrast_name="Generation",
			error_dof="102",
			effect_dof="1",
			sha="b6286d36e678c23622b5b0486f0efb5b274f9a5e2a3ee6aceb6a0338f7745fb8a4d8f72b8af22c4ffb40c860bfb65940c87b03a7336cdf1a665f9cb07a5c2527",
			coordinate_space_id="niiri:coordinate_space_id_1",
			contrast_est_id="niiri:contrast_estimation_id_1"),
		"FSL_StatisticMap-Z": dict(
			statistic_map_id="niiri:z_statistic_map_id_1",
			label="Z-Statistic Map: Generation",
			location="file://./ZStatistic.nii.gz",
			format="image/nifti",
			filename_1="ZStatistic.nii.gz",
			filename_2="zstat1.nii.gz",
			statistic_type=STATO_ZSTATISTIC_STR,
			stat_type_comment=STATO_ZSTATISTIC_LABEL,
			contrast_name="Generation",
			effect_dof="1",
			error_dof="INF",
			sha="3a68a4e5963766af86d22a871a4dbca9568a46441a567855b3a84dbd47ea01acea11ed77b37ce85078a219adaa92264296a4548c1ba39b11ff028e8fefd95d03",
			coordinate_space_id="niiri:coordinate_space_id_1",
			contrast_est_id="niiri:contrast_estimation_id_1"),
		"HeightThreshold_Value": dict(
			height_threshold_id="niiri:height_threshold_id",
			label="Height Threshold: Z>2.3",
			value="2.3",
			thresh_type="Z-Statistic"
			),
		"FSL_ExtentThreshold": dict(
			extent_threshold_id="niiri:extent_threshold_id",
			label="Extent Threshold: p<0.05 (FWE)",
			thresh_type="p-value FWE",
			p_fwe="0.05"
			),
		"DisplayMaskMap_fileName": dict(
			display_map_id="niiri:display_map_id_1",
			label="Display Mask Map",
			location="file://./DisplayMask.nii.gz",
			format="image/nifti",
			user_defined="true",
			filename="DisplayMask.nii.gz",
			filename_2="mask.nii.gz",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="cc1a96a6111e5107eb08487e38e6d7f8164b9d1d3f1fc10948bdbcfaea642fe9bfae278c7fc372b65cac7232ea58fd8fb5914014e7b9a5d6200592b12b2a728b"
			),
		"PeakDefinitionCriteria": dict(
			peak_definition_criteria_id="niiri:peak_definition_criteria_id_1",
			label="Peak Definition Criteria",
			min_dist_peaks="0.0"
			),
		"ClusterDefinitionCriteria": dict(
			cluster_definition_criteria_id="niiri:cluster_definition_criteria_id_1",
			label="Cluster Connectivity Criterion: 26",
			connectivity="nidm:voxel26connected"
			),
		"Inference": dict(
			inference_id="niiri:inference_id_1",
			label="Inference: Generation",
			alternative_hyp="nidm:OneTailedTest",
			stat_map_id="niiri:z_statistic_map_id_1", 
			height_thresh_id="niiri:height_threshold_id", 
			extent_thresh_id="niiri:extent_threshold_id", 
			display_mask_id="niiri:display_map_id_1", 
			peak_def_id="niiri:peak_definition_criteria_id_1", 
			cluster_def_id="niiri:cluster_definition_criteria_id_1",
			mask_id="niiri:mask_id_1",
			software_id="niiri:software_id"
			),
		"FSL_ExcursionSetMap": dict(
			id="niiri:excursion_set_map_id_1",
			label="Excursion Set Map",
			location="file://./ExcursionSetMap.nii.gz",
			format="image/nifti",
			filename_1="ExcursionSetMap.nii.gz",
			filename_2="thresh_zstat1.nii.gz",
			cluster_label_map_id="niiri:cluster_label_map_id",
			png_id="niiri:excursion_set_png_id_1",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="c74e3c47e4308f27423a195c7c3e70b64b8fd362d612a2543da76bced67f666949b70272033ab3d4b7d0bbbfe22b7da13d56d25521664be0c96454fd180ee4cc",
			inference_id="niiri:inference_id_1"
			),
		"Image": dict(
			image_id="niiri:excursion_set_png_id_1",
			location="file://./rendered_thresh_zstat1.png",
			filename="rendered_thresh_zstat1.png",
			format="image/png"
			),
		"FSL_SignificantCluster-1": dict(
			cluster_id="niiri:significant_cluster_0001",
			label="Significant Cluster 0001",
			cluster_size_in_voxels="81",
			cluster_label_id="1",
			cluster_size_in_resels="23.1209189500945",
			p_value_fwe="0.00894",
			excursion_set_id="niiri:excursion_set_map_id_1"
			),
		"FSL_CenterOfGravity-1": dict(
			center_of_gravity_id="niiri:center_of_gravity_1",
			label="Center of gravity 1",
			location="niiri:COG_coordinate_0001",
			cluster_id="niiri:significant_cluster_0001"
			),
		"FSL_Coordinate-COG1": dict(
			coordinate_id="niiri:COG_coordinate_0001",
			label="Coordinate 0001",
			coord_1="-5.8",
			coord_2="19.1",
			coord_3="38.5",
			coord_1_in_vox="32.3",
			coord_2_in_vox="39.2",
			coord_3_in_vox="31",
			),
		"FSL_SignificantCluster-2": dict(
			cluster_id="niiri:significant_cluster_0002",
			label="Significant Cluster 0002",
			cluster_size_in_voxels="117",
			cluster_label_id="2",
			cluster_size_in_resels="19.4128470430038",
			p_value_fwe="0.000621",
			excursion_set_id="niiri:excursion_set_map_id_1"
			),
		"FSL_CenterOfGravity-2": dict(
			center_of_gravity_id="niiri:center_of_gravity_2",
			label="Center of gravity 2",
			location="niiri:COG_coordinate_0002",
			cluster_id="niiri:significant_cluster_0002"
			),
		"FSL_Coordinate-COG2": dict(
			coordinate_id="niiri:COG_coordinate_0002",
			label="Coordinate 0002",
			coord_1="-56.9",
			coord_2="-57.1",
			coord_3="9.86",
			coord_1_in_vox="47.1",
			coord_2_in_vox="19.2",
			coord_3_in_vox="19.7",
			),
		"FSL_SignificantCluster-3": dict(
			cluster_id="niiri:significant_cluster_0003 ",
			label="Significant Cluster 0003",
			cluster_size_in_voxels="499",
			cluster_label_id="3",
			cluster_size_in_resels="19.4128470430038",
			p_value_fwe="1.26e-12",
			excursion_set_id="niiri:excursion_set_map_id_1"
			),
		"FSL_CenterOfGravity-3 ": dict(
			center_of_gravity_id="niiri:center_of_gravity_3 ",
			label="Center of gravity 3",
			location="niiri:COG_coordinate_0003 ",
			cluster_id="niiri:significant_cluster_0003 "
			),
		"FSL_Coordinate-COG3 ": dict(
			coordinate_id="niiri:COG_coordinate_0003 ",
			label="Coordinate 0003",
			coord_1="-47.2",
			coord_2="17.3",
			coord_3="9.18",
			coord_1_in_vox="43.4",
			coord_2_in_vox="40.3",
			coord_3_in_vox="23.9",
			),
		"FSL_SignificantCluster-4": dict(
			cluster_id="niiri:significant_cluster_0004 ",
			label="Significant Cluster 0004",
			cluster_size_in_voxels="1203",
			cluster_label_id="4",
			p_value_fwe="8.02e-24",
			excursion_set_id="niiri:excursion_set_map_id_1"
			),
		"FSL_CenterOfGravity-4  ": dict(
			center_of_gravity_id="niiri:center_of_gravity_4",
			label="Center of gravity 4",
			location="niiri:COG_coordinate_0004  ",
			cluster_id="niiri:significant_cluster_0004  "
			),
		"FSL_Coordinate-COG4  ": dict(
			coordinate_id="niiri:COG_coordinate_0004  ",
			label="Coordinate 0004",
			coord_1="-7.38",
			coord_2="-72.5",
			coord_3="-8.5",
			coord_1_in_vox="34",
			coord_2_in_vox="14.7",
			coord_3_in_vox="14",
			),
		"FSL_ClusterMaximumStatistic-4-1": dict(
			peak_id="niiri:peak_0004_1",
			label="Peak 0004_1",
			p_uncorr="3.51932e-09",
			location="niiri:coordinate_0004_1",
			equiv_z="5.79",
			cluster_id="niiri:significant_cluster_0004"
			),
		"FSL_Coordinate-4-1": dict(
			coordinate_id="niiri:coordinate_0004_1",
			label="Coordinate 0004_1",
			coord_1="-33.7",
			coord_2="-66.7",
			coord_3="-14.7",
			coord_1_in_vox="41",
			coord_2_in_vox="17",
			coord_3_in_vox="13",
			),
		"Peak-4-2": dict(
			peak_id="niiri:peak_0004_2",
			label="Peak 0004_2",
			p_uncorr="9.01048e-09",
			location="niiri:coordinate_0004_2",
			equiv_z="5.63",
			cluster_id="niiri:significant_cluster_0004"
			),
		"FSL_Coordinate-4-2": dict(
			coordinate_id="niiri:coordinate_0004_2",
			label="Coordinate 0004_2",
			coord_1="-38",
			coord_2="-53.9",
			coord_3="-21.9",
			coord_1_in_vox="42",
			coord_2_in_vox="21",
			coord_3_in_vox="12",
			),
		"Peak-4-3": dict(
			peak_id="niiri:peak_0004_3",
			label="Peak 0004_3",
			p_uncorr="9.54787e-09",
			location="niiri:coordinate_0004_3",
			equiv_z="5.62",
			cluster_id="niiri:significant_cluster_0004"
			),
		"FSL_Coordinate-4-3": dict(
			coordinate_id="niiri:coordinate_0004_3",
			label="Coordinate 0004_3",
			coord_1="16.1",
			coord_2="-96.6",
			coord_3="5.82",
			coord_1_in_vox="28",
			coord_2_in_vox="7",
			coord_3_in_vox="16",
			),
		"Peak-4-4": dict(
			peak_id="niiri:peak_0004_4",
			label="Peak 0004_4",
			p_uncorr="1.01163e-08",
			location="niiri:coordinate_0004_4",
			equiv_z="5.61",
			cluster_id="niiri:significant_cluster_0004"
			),
		"FSL_Coordinate-4-4": dict(
			coordinate_id="niiri:coordinate_0004_4",
			label="Coordinate 0004_4",
			coord_1="-48.1",
			coord_2="-73.7",
			coord_3="-9.24",
			coord_1_in_vox="45",
			coord_2_in_vox="15",
			coord_3_in_vox="14"
			),
		"Peak-4-5": dict(
			peak_id="niiri:peak_0004_5",
			label="Peak 0004_5",
			p_uncorr="1.07176e-08",
			location="niiri:coordinate_0004_5",
			equiv_z="5.6",
			cluster_id="niiri:significant_cluster_0004"
			),
		"FSL_Coordinate-4-5": dict(
			coordinate_id="niiri:coordinate_0004_5",
			label="Coordinate 0004_5",
			coord_1="-25.5",
			coord_2="-80.4",
			coord_3="-15.3",
			coord_1_in_vox="39",
			coord_2_in_vox="13",
			coord_3_in_vox="12"
			),
		"Peak-4-6": dict(
			peak_id="niiri:peak_0004_6",
			label="Peak 0004_6",
			p_uncorr="1.34887e-08",
			location="niiri:coordinate_0004_6",
			equiv_z="5.56",
			cluster_id="niiri:significant_cluster_0004"
			),
		"FSL_Coordinate-4-6": dict(
			coordinate_id="niiri:coordinate_0004_6",
			label="Coordinate 0004_6",
			coord_1="0.791",
			coord_2="-87.2",
			coord_3="3.23",
			coord_1_in_vox="32",
			coord_2_in_vox="10",
			coord_3_in_vox="16"
			),
		"FSL_ClusterMaximumStatistic-3-1": dict(
			peak_id="niiri:peak_0003_1",
			label="Peak 0003_1",
			p_uncorr="1.01163e-08",
			location="niiri:coordinate_0003_1",
			equiv_z="5.61",
			cluster_id="niiri:significant_cluster_0003"
			),
		"FSL_Coordinate-3-1": dict(
			coordinate_id="niiri:coordinate_0003_1",
			label="Coordinate 0003_1",
			coord_1="-38.3",
			coord_2="20.7",
			coord_3="13.2",
			coord_1_in_vox="41",
			coord_2_in_vox="41",
			coord_3_in_vox="25"
			),
		"Peak-3-2": dict(
			peak_id="niiri:peak_0003_2",
			label="Peak 0003_2",
			p_uncorr="1.52768e-07",
			location="niiri:coordinate_0003_2",
			equiv_z="5.12",
			cluster_id="niiri:significant_cluster_0003"
			),
		"FSL_Coordinate-3-2": dict(
			coordinate_id="niiri:coordinate_0003_2",
			label="Coordinate 0003_2",
			coord_1="-45.5",
			coord_2="17.8",
			coord_3="-6.65",
			coord_1_in_vox="43",
			coord_2_in_vox="41",
			coord_3_in_vox="20"
			),
		"Peak-3-3": dict(
			peak_id="niiri:peak_0003_3",
			label="Peak 0003_3",
			p_uncorr="1.82833e-06",
			location="niiri:coordinate_0003_3",
			equiv_z="4.63",
			cluster_id="niiri:significant_cluster_0003"
			),
		"FSL_Coordinate-3-3": dict(
			coordinate_id="niiri:coordinate_0003_3",
			label="Coordinate 0003_3",
			coord_1="-63.4",
			coord_2="3.78",
			coord_3="0.366",
			coord_1_in_vox="48",
			coord_2_in_vox="37",
			coord_3_in_vox="21"
			),
		"Peak-3-4": dict(
			peak_id="niiri:peak_0003_4",
			label="Peak 0003_4",
			p_uncorr="9.77365e-06",
			location="niiri:coordinate_0003_4",
			equiv_z="4.27",
			cluster_id="niiri:significant_cluster_0003"
			),
		"FSL_Coordinate-3-4": dict(
			coordinate_id="niiri:coordinate_0003_4",
			label="Coordinate 0003_4",
			coord_1="-57.4",
			coord_2="31.8",
			coord_3="-2.12",
			coord_1_in_vox="46",
			coord_2_in_vox="45",
			coord_3_in_vox="22"
			),
		"Peak-3-5": dict(
			peak_id="niiri:peak_0003_5",
			label="Peak 0003_5",
			p_uncorr="1.22151e-05",
			location="niiri:coordinate_0003_5",
			equiv_z="4.22",
			cluster_id="niiri:significant_cluster_0003"
			),
		"FSL_Coordinate-3-5": dict(
			coordinate_id="niiri:coordinate_0003_5",
			label="Coordinate 0003_5",
			coord_1="-34",
			coord_2="8.84",
			coord_3="28.3",
			coord_1_in_vox="40",
			coord_2_in_vox="37",
			coord_3_in_vox="28"
			),
		"Peak-3-6": dict(
			peak_id="niiri:peak_0003_6",
			label="Peak 0003_6",
			p_uncorr="1.89436e-05",
			location="niiri:coordinate_0003_6",
			equiv_z="4.12",
			cluster_id="niiri:significant_cluster_0003"
			),
		"FSL_Coordinate-3-6": dict(
			coordinate_id="niiri:coordinate_0003_6",
			label="Coordinate 0003_6",
			coord_1="-53.3",
			coord_2="23.3",
			coord_3="12.2",
			coord_1_in_vox="45",
			coord_2_in_vox="42",
			coord_3_in_vox="25"
			),
		"FSL_ClusterMaximumStatistic-2-1": dict(
			peak_id="niiri:peak_0002_1",
			label="Peak 0002_1",
			p_uncorr="1.74205e-06",
			location="niiri:coordinate_0002_1",
			equiv_z="4.64",
			cluster_id="niiri:significant_cluster_0002"
			),
		"FSL_Coordinate-2-1": dict(
			coordinate_id="niiri:coordinate_0002_1",
			label="Coordinate 0002_1",
			coord_1="-56.2",
			coord_2="-61.9",
			coord_3="4.03",
			coord_1_in_vox="47",
			coord_2_in_vox="18",
			coord_3_in_vox="18"
			),
		"Peak-2-2": dict(
			peak_id="niiri:peak_0002_2",
			label="Peak 0002_2",
			p_uncorr="4.71165e-06",
			location="niiri:coordinate_0002_2",
			equiv_z="4.43",
			cluster_id="niiri:significant_cluster_0002"
			),
		"FSL_Coordinate-2-2": dict(
			coordinate_id="niiri:coordinate_0002_2",
			label="Coordinate 0002_2",
			coord_1="-56.7",
			coord_2="-53.1",
			coord_3="18.2",
			coord_1_in_vox="47",
			coord_2_in_vox="20",
			coord_3_in_vox="22"
			),
		"FSL_ClusterMaximumStatistic-1-1": dict(
			peak_id="niiri:peak_0001_1",
			label="Peak 0001_1",
			p_uncorr="2.01334e-06",
			location="niiri:coordinate_0001_1",
			equiv_z="4.61",
			cluster_id="niiri:significant_cluster_0001"
			),
		"FSL_Coordinate-1-1": dict(
			coordinate_id="niiri:coordinate_0001_1",
			label="Coordinate 0001_1",
			coord_1="-8.35",
			coord_2="15.1",
			coord_3="39.6",
			coord_1_in_vox="33",
			coord_2_in_vox="38",
			coord_3_in_vox="31"
			),
		"Peak-1-2": dict(
			peak_id="niiri:peak_0001_2",
			label="Peak 0001_2",
			p_uncorr="0.000788846",
			location="niiri:coordinate_0001_2",
			equiv_z="3.16",
			cluster_id="niiri:significant_cluster_0001"
			),
		"FSL_Coordinate-1-2": dict(
			coordinate_id="niiri:coordinate_0001_2",
			label="Coordinate 0001_2",
			coord_1="-9.14",
			coord_2="30.5",
			coord_3="23.7",
			coord_1_in_vox="33",
			coord_2_in_vox="43",
			coord_3_in_vox="28"
			),
		"Peak-1-3": dict(
			peak_id="niiri:peak_0001_3",
			label="Peak 0001_3",
			p_uncorr="0.00122277",
			location="niiri:coordinate_0001_3",
			equiv_z="3.03",
			cluster_id="niiri:significant_cluster_0001"
			),
		"FSL_Coordinate-1-3": dict(
			coordinate_id="niiri:coordinate_0001_3",
			label="Coordinate 0001_3",
			coord_1="-19.6",
			coord_2="17.4",
			coord_3="34.7",
			coord_1_in_vox="36",
			coord_2_in_vox="39",
			coord_3_in_vox="30"
			),
		"Peak-1-4": dict(
			peak_id="niiri:peak_0001_4",
			label="Peak 0001_4",
			p_uncorr="0.00554262",
			location="niiri:coordinate_0001_4",
			equiv_z="2.54",
			cluster_id="niiri:significant_cluster_0001"
			),
		"FSL_Coordinate-1-4": dict(
			coordinate_id="niiri:coordinate_0001_4",
			label="Coordinate 0001_4",
			coord_1="-9.64",
			coord_2="40.1",
			coord_3="17.3",
			coord_1_in_vox="33",
			coord_2_in_vox="46",
			coord_3_in_vox="27"
			),
		"FSL_SearchSpaceMaskMap": dict(
			search_space_id="niiri:search_space_mask_id",
			location="file://./SearchSpace.nii.gz",
			filename_1="SearchSpaceMask.nii.gz",
			filename_2="mask.nii.gz",
			label="Search Space Mask Map",
			user_defined="false",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			search_vol_voxels="45203",
			resel_size="12.0418",
			dlh="0.384676",
			random_field_station="true",
			sha="cc1a96a6111e5107eb08487e38e6d7f8164b9d1d3f1fc10948bdbcfaea642fe9bfae278c7fc372b65cac7232ea58fd8fb5914014e7b9a5d6200592b12b2a728b",
			inference_id="niiri:inference_id_1"
			),
		"NIDMBundle": dict(
			bundle_id="niiri:fsl_results_id",
			label="FSL Results",
			object_model="nidm:FSLResults",
			version="0.2.0",
			time="2014-05-19T10:30:00.000+01:00"
			),
		"FSL_Software": dict(
			software_id="niiri:software_id",
			software_type="nidm:FSL",
			label="FSL",
			version="fsl-5_0_x",
			feat_version="6.00"
			),
		"FSL_GrandMeanMap": dict(
			grand_mean_map_id="niiri:grand_mean_map_id",
			label="Grand Mean Map",
			location="file://./GrandMean.nii.gz",
			filename_1="GrandMean.nii.gz",
			filename_2="mean_func.nii.gz",
			format="image/nifti",
			masked_median="9597.36",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="7a2703cea740e27a5170fb19e4a09b5e815e4b7e477bc75958404d675aa408f53f747892a2ef4472f933cf5f12cd21cea99d5f5e551938081636fb6d4049473e",
			model_pe_id="niiri:model_parameters_estimation_id"
			)
		}

	NIDM_FSL_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'fsl', "example001")
	ttl_file = os.path.join(NIDM_FSL_DIR, 'fsl_nidm.ttl')
	example = ExampleFromTemplate(nidm_classes, ttl_file, False)
	example.create_example()

if __name__ == '__main__':
	main()
