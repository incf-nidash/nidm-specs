"""
Create FSL examples stored in nidm/nidm-results/fsl by using the class 
templates available in nidm/nidm-results/terms/templates

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""
import os
from create_example_from_templates import ExampleFromTemplate

def main():
	nidm_classes = {
		"DesignMatrix": dict(
			design_matrix_id='niiri:design_matrix_id', 
			label="Design Matrix", 
			location="file://path/to/DesignMatrix.csv",
			format="text/csv", 
			filename="DesignMatrix.csv", 
			design_matrix_png_id="niiri:design_matrix_png_id"),
		"Image-DesignMatrix": dict(
			image_id="niiri:design_matrix_png_id",
			location="file://path/to/DesignMatrix.png",
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
			variance_spatial="nidm:SpatiallyLocal",
			dependence="nidm:IndependentError",
			dependence_spatial="nidm:SpatiallyLocal"
			),
		"ModelParametersEstimation": dict(
			model_pe_id="niiri:model_pe_id",
			label="Model parameters estimation",
			est_method="nidm:OrdinaryLeastSquares",
			design_matrix_id="niiri:design_matrix_id",
			data_matrix_id="niiri:data_id",
			error_model_id="niiri:error_model_id",
			software_id="niiri:software_id"
			),
		"FSL_ParameterEstimateMap-1": dict(
			beta_map_id="niiri:beta_map_id_1",
			label="Parameter estimate 1",
			location="file://path/to/ParameterEstimate_0001.nii.gz",
			filename_1="pe1.nii.gz",
			filename_2="ParameterEstimate_0001.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="f51b6e01b0463fe7d40782137867a...",
			param_est_id="niiri:model_pe_id"),
		"FSL_ParameterEstimateMap-2": dict(
			beta_map_id="niiri:beta_map_id_2",
			label="Parameter estimate 2",
			location="file://path/to/ParameterEstimate_0002.nii.gz",
			filename_1="pe2.nii.gz",
			filename_2="ParameterEstimate_0002.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="p89b6e01b0463fe7d40782137867a...",
			param_est_id="niiri:model_pe_id"),
		"CoordinateSpace-1": dict(
			coordinate_space_id="niiri:coordinate_space_id_1",
			label="Coordinate space 1",
			voxel_to_world_mapping="[[-3, 0, 0, 81],[0, 3, 0, -115],[0, 0, 3, -53],[0, 0, 0, 1]]",
			voxel_units="['mm', 'mm', 'mm']",
			voxel_size="[3, 3, 3]",
			coord_system="nidm:IcbmMni152NonLinear6thGenerationCoordinateSystem",
			number_of_dim="3",
			dimensions="[53,63,46]"),
		"CoordinateSpace-2": dict(
			coordinate_space_id="niiri:coordinate_space_id_2",
			label="Coordinate space 2",
			voxel_to_world_mapping="[[-3, 0, 0, 81],[0, 3, 0, -115],[0, 0, 3, -53],[0, 0, 0, 1]]",
			voxel_units="['mm', 'mm', 'mm']",
			voxel_size="[3, 3, 3]",
			coord_system="nidm:IcbmMni152NonLinear6thGenerationCoordinateSystem",
			number_of_dim="3",
			dimensions="[53,63,46]"),
		"FSL_ResidualMeanSquaresMap": dict(
			residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
			label="Residual Mean Squares Map",
			location="file://path/to/ResidualMeanSquares.nii.gz",
			filename_1="ResidualMeanSquares.nii.gz",
			filename_2="sigmasquareds.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			param_est_id="niiri:model_pe_id"),
		"FSL_MaskMap": dict(
			mask_id="niiri:mask_id_1",
			label="Mask",
			location="file://path/to/Mask.nii.gz",
			filename_1="Mask.nii.gz", 
			filename_2="mask.nii.gz", 
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			param_est_id="niiri:model_pe_id"),
		"ContrastWeights": dict(
			contrast_id="niiri:contrast_id",
			label="Contrast weights: listening > rest",
			value="[1, 0, 0]",
			statistic_type="nidm:TStatistic",
			contrast_name="listening > rest"
			),
		"ContrastEstimation": dict(
			contrast_estimation_id="niiri:contrast_estimation_id",
			label="Contrast estimation",
			software_id="niiri:software_id",
			mask_id="niiri:mask_id_1",
			residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
			design_matrix_id="niiri:design_matrix_id",
			contrast_id="niiri:contrast_id",
			param_est_map="niiri:beta_map_id_1"
			),
		"ContrastEstUsedParamEst-1-2": dict(
			contrast_estimation_id="niiri:contrast_estimation_id",
			param_est_map="niiri:beta_map_id_2"
			),
		"FSL_ContrastMap": dict(
			contrast_map_id="niiri:contrast_map_id",
			label="Contrast Map: listening > rest",
			location="file://path/to/Contrast.nii.gz",
			format="image/nifti",
			filename_1="Contrast.nii.gz",
			filename_2="cope1.nii.gz",
			contrast_name="listening > rest",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="400a2f07d99ed9be06577e6ecc89222cf4b688c654bc89067da558e88b73b97dd1b25e6c98f2a735fa0a1409598cff7e6025bda55abb6b9f5ef65d8d307eeba8",
			contrast_est_id="niiri:contrast_estimation_id"),
		"ContrastStandardErrorMap": dict(
			contrast_standard_error_map_id="niiri:contrast_standard_error_map_id",
			label="Contrast Standard Error Map",
			location="file://path/to/ContrastStandardError.nii.gz",
			format="image/nifti",
			filename="ContrastStandardError.nii.gz",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			contrast_est_id="niiri:contrast_estimation_id"),
		"FSL_DerivedMap-ContrastVariance": dict(
			derived_from_map_id="niiri:contrast_variance_map_id",
			derived_map_type="fsl:ContrastVarianceMap",
			filename="varcope1.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			map_id="niiri:contrast_standard_error_map_id"
			),
		"FSL_StatisticMap": dict(
			statistic_map_id="niiri:statistic_map_id",
			label="Statistic Map: listening > rest",
			location="file://path/to/TStatistic_0001.nii.gz",
			format="image/nifti",
			filename_1="TStatistic_0001.nii.gz",
			filename_2="tstat1.nii.gz",
			statistic_type="nidm:TStatistic",
			contrast_name="listening > rest",
			error_dof="73.0",
			effect_dof="1",
			sha="400a2f07d99ed9be06577e6ecc89222cf4b688c654bc89067da558e88b73b97dd1b25e6c98f2a735fa0a1409598cff7e6025bda55abb6b9f5ef65d8d307eeba8",
			coordinate_space_id="niiri:coordinate_space_id_1",
			contrast_est_id="niiri:contrast_estimation_id"),
		"FSL_ZStatisticMap": dict(
			statistic_map_id="niiri:z_statistic_map_id",
			label="Z-Statistic Map: listening > rest",
			location="file://path/to/ZStatistic_0001.nii.gz",
			format="image/nifti",
			filename_1="ZStatistic_0001.nii.gz",
			filename_2="zstat1.nii.gz",
			statistic_type="nidm:ZStatistic",
			contrast_name="listening > rest",
			effect_dof="1",
			sha="400a2f07d99ed9be06577e6ecc89222cf4b688c654bc89067da558e88b73b97dd1b25e6c98f2a735fa0a1409598cff7e6025bda55abb6b9f5ef65d8d307eeba8",
			coordinate_space_id="niiri:coordinate_space_id_1",
			contrast_est_id="niiri:contrast_estimation_id"),
		"HeightThreshold": dict(
			height_threshold_id="niiri:height_threshold_id",
			label="Height Threshold: p<0.05 (FWE)",
			p_unc="0.000001",
			p_fwe="0.050000",
			value="5.235300",
			thresh_type="p-value FWE"
			),
		"FSL_ExtentThreshold_NoType": dict(
			extent_threshold_id="niiri:extent_threshold_id",
			label="Cluster Threshold",
			p_fwe="1.0"
			),
		"FSL_DisplayMaskMap": dict(
			display_map_id="niiri:display_map_id",
			label="Display Mask Map",
			location="file://path/to/DisplayMask.nii.gz",
			format="image/nifti",
			filename_1="DisplayMask.nii.gz",
			filename_2="mask.nii.gz",
			coordinate_space_id="niiri:coordinate_space_id_2",
			sha="e43b6e01b0463fe7d40782137867a..."
			),
		"PeakDefinitionCriteria": dict(
			peak_definition_criteria_id="niiri:peak_definition_criteria_id",
			label="Peak Definition Criteria",
			max_num_peaks="3",
			min_dist_peaks="8.0"
			),
		"ClusterDefinitionCriteria": dict(
			cluster_definition_criteria_id="niiri:cluster_definition_criteria_id",
			label="Cluster Connectivity Criterion: 18",
			connectivity="nidm:voxel18Connected"
			),
		"Inference": dict(
			inference_id="niiri:inference_id",
			label="Inference",
			alternative_hyp="nidm:OneTailedTest",
			stat_map_id="niiri:z_statistic_map_id", 
			height_thresh_id="niiri:height_threshold_id", 
			extent_thresh_id="niiri:extent_threshold_id", 
			display_mask_id="niiri:display_map_id", 
			peak_def_id="niiri:peak_definition_criteria_id", 
			cluster_def_id="niiri:cluster_definition_criteria_id",
			mask_id="niiri:mask_id_1",
			software_id="niiri:software_id"
			),
		"FSL_ExcursionSet": dict(
			excursion_set_id="niiri:excursion_set_id",
			label="Excursion Set",
			location="file://path/to/ExcursionSet.nii.gz",
			format="image/nifti",
			filename_1="ExcursionSet.nii.gz",
			filename_2="thresh_zstat1.nii.gz",
			cluster_label_map_id="niiri:cluster_label_map_id",
			png_id="niiri:excursion_set_png_id_1",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="400a2f07d99ed9be06577e6ecc89222cf4b688c654bc89067da558e88b73b97dd1b25e6c98f2a735fa0a1409598cff7e6025bda55abb6b9f5ef65d8d307eeba8",
			inference_id="niiri:inference_id"
			),
		"Image": dict(
			image_id="niiri:excursion_set_png_id_1",
			location="file://path/to/rendered_thresh_zstat1.png",
			filename="rendered_thresh_zstat1.png",
			format="image/png"
			),
		"FSL_Cluster-1": dict(
			cluster_id="niiri:cluster_0001",
			label="Cluster 0001",
			cluster_size_in_voxels="530",
			cluster_label_id="1",
			p_value_fwe="0.000000",
			excursion_set_id="niiri:excursion_set_id"
			),
		"FSL_CenterOfGravity-1": dict(
			center_of_gravity_id="niiri:center_of_gravity_1",
			label="Center of gravity 1",
			location="niiri:COG_coordinate_0001",
			cluster_id="niiri:cluster_0001"
			),
		"FSL_Coordinate-COG1": dict(
			coordinate_id="niiri:COG_coordinate_0001",
			label="Coordinate 1",
			coord_1="40.2",
			coord_2="16.4",
			coord_3="13.2",
			coord_1_in_vox="-30.8",
			coord_2_in_vox="-68.5",
			coord_3_in_vox="-13.4",
			),
		"FSL_Cluster-2": dict(
			cluster_id="niiri:cluster_0002",
			label="Cluster 0002",
			cluster_size_in_voxels="445",
			cluster_label_id="2",
			p_value_fwe="0.000000",
			excursion_set_id="niiri:excursion_set_id"
			),
		"FSL_CenterOfGravity-2": dict(
			center_of_gravity_id="niiri:center_of_gravity_2",
			label="Center of gravity 2",
			location="niiri:COG_coordinate_0002",
			cluster_id="niiri:cluster_0002"
			),
		"FSL_Coordinate-COG2": dict(
			coordinate_id="niiri:COG_coordinate_0002",
			label="Coordinate 2",
			coord_1="25.6",
			coord_2="12.8",
			coord_3="14.6",
			coord_1_in_vox="24.1",
			coord_2_in_vox="-77.1",
			coord_3_in_vox="-4.27",
			),
		"FSL_Peak_NoP_MaxCluster-1": dict(
			peak_id="niiri:peak_0001",
			label="Peak 1",
			location="niiri:coordinate_0001",
			equiv_z="6.14",
			cluster_id="niiri:cluster_0001"
			),
		"FSL_Coordinate-1": dict(
			coordinate_id="niiri:coordinate_0001",
			label="Coordinate 1",
			coord_1="-48.1",
			coord_2="-73.7",
			coord_3="-9.24",
			coord_1_in_vox="45",
			coord_2_in_vox="15",
			coord_3_in_vox="14",
			),
		"Peak_NoP-2": dict(
			peak_id="niiri:peak_0002",
			label="Peak 2",
			location="niiri:coordinate_0002",
			equiv_z="6.04",
			cluster_id="niiri:cluster_0001"
			),
		"FSL_Coordinate-2": dict(
			coordinate_id="niiri:coordinate_0002",
			label="Coordinate 2",
			coord_1="-38.1",
			coord_2="-53.4",
			coord_3="-18",
			coord_1_in_vox="42",
			coord_2_in_vox="21",
			coord_3_in_vox="13",
			),
		"Peak_NoP-3": dict(
			peak_id="niiri:peak_0003",
			label="Peak 3",
			location="niiri:coordinate_0003",
			equiv_z="5.75",
			cluster_id="niiri:cluster_0001"
			),
		"FSL_Coordinate-3": dict(
			coordinate_id="niiri:coordinate_0003",
			label="Coordinate 3",
			coord_1="-29.6",
			coord_2="-73.8",
			coord_3="-16.9",
			coord_1_in_vox="40",
			coord_2_in_vox="15",
			coord_3_in_vox="12",
			),
		"Peak_NoP-4": dict(
			peak_id="niiri:peak_0004",
			label="Peak 4",
			location="niiri:coordinate_0004",
			equiv_z="5.75",
			cluster_id="niiri:cluster_0001"
			),
		"FSL_Coordinate-4": dict(
			coordinate_id="niiri:coordinate_0004",
			label="Coordinate 4",
			coord_1="0.791",
			coord_2="-87.2",
			coord_3="3.23",
			coord_1_in_vox="39",
			coord_2_in_vox="13",
			coord_3_in_vox="12"
			),
		"FSL_Peak_NoP_MaxCluster-5": dict(
			peak_id="niiri:peak_0005",
			label="Peak 5",
			location="niiri:coordinate_0005",
			equiv_z="5.87",
			cluster_id="niiri:cluster_0002"
			),
		"FSL_Coordinate-5": dict(
			coordinate_id="niiri:coordinate_0005",
			label="Coordinate 5",
			coord_1="16.1",
			coord_2="-96.6",
			coord_3="5.82",
			coord_1_in_vox="32",
			coord_2_in_vox="10",
			coord_3_in_vox="16"
			),
		"Peak_NoP-6": dict(
			peak_id="niiri:peak_0006",
			label="Peak 6",
			location="niiri:coordinate_0006",
			equiv_z="5.65",
			cluster_id="niiri:cluster_0002"
			),
		"FSL_Coordinate-6": dict(
			coordinate_id="niiri:coordinate_0006",
			label="Coordinate 6",
			coord_1="-25.5",
			coord_2="-80.4",
			coord_3="-15.3",
			coord_1_in_vox="28",
			coord_2_in_vox="7",
			coord_3_in_vox="16"
			),
		"FSL_SearchSpaceMap": dict(
			search_space_id="niiri:search_space_id",
			location="file://path/to/SearchSpace.nii.gz",
			filename_1="SearchSpace.nii.gz",
			filename_2="mask.nii.gz",
			label="Search Space Map",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_2",
			search_vol_voxels="45359",
			resel_size="12.2251",
			dlh="0.384676",
			random_field_station="true",
			sha="400a2f07d99ed9be06577e6ecc89222cf4b688c654bc89067da558e88b73b97dd1b25e6c98f2a735fa0a1409598cff7e6025bda55abb6b9f5ef65d8d307eeba8",
			inference_id="niiri:inference_id"
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
			location="file://path/to/GrandMean.nii.gz",
			filename_1="GrandMean.nii.gz",
			filename_2="mean_func.nii.gz",
			format="image/nifti",
			masked_median="115",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a...",
			model_pe_id="niiri:model_pe_id"
			)
		}

	NIDM_FSL_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'fsl')
	ttl_file = os.path.join(NIDM_FSL_DIR, 'fsl_results.ttl')
	example = ExampleFromTemplate(nidm_classes, ttl_file, False)
	example.create_example()
