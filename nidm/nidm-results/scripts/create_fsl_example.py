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
from Constants import STATO_OLS_STR, STATO_OLS_LABEL, STATO_TSTATISTIC_STR, \
	STATO_ZSTATISTIC_STR, STATO_TSTATISTIC_LABEL, OBO_P_VALUE_FWER_QNAME, \
	NIDM_P_VALUE_UNCORRECTED_QNAME, OBO_STATISTIC_QNAME

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
			noise_distribution="obo:STATO_0000227",
			variance_homo="true",
			variance_spatial="nidm:NIDM_0000073",
			dependence="nidm:NIDM_0000048",
			dependence_spatial="nidm:NIDM_0000073"
			),
		"ModelParametersEstimation": dict(
			model_pe_id="niiri:model_pe_id",
			label="Model parameters estimation",
			est_method=STATO_OLS_STR,
			est_method_comment=STATO_OLS_LABEL,
			design_matrix_id="niiri:design_matrix_id",
			data_matrix_id="niiri:data_id",
			error_model_id="niiri:error_model_id",
			software_id="niiri:software_id"
			),
		"ParameterEstimateMap_Location-1": dict(
			beta_map_id="niiri:beta_map_id_1",
			label="Parameter estimate 1",
			location="file://path/to/ParameterEstimate_0001.nii.gz",
			filename="ParameterEstimate_0001.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="f51b6e01b0463fe7d40782137867a",
			param_est_id="niiri:model_pe_id"),
		"ParameterEstimateMap_Location-2": dict(
			beta_map_id="niiri:beta_map_id_2",
			label="Parameter estimate 2",
			location="file://path/to/ParameterEstimate_0002.nii.gz",
			filename="ParameterEstimate_0002.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="p89b6e01b0463fe7d40782137867a",
			param_est_id="niiri:model_pe_id"),
		"CoordinateSpace-1": dict(
			coordinate_space_id="niiri:coordinate_space_id_1",
			label="Coordinate space 1",
			voxel_to_world_mapping="[[-3, 0, 0, 81],[0, 3, 0, -115],[0, 0, 3, -53],[0, 0, 0, 1]]",
			voxel_units="[ \\\"mm\\\", \\\"mm\\\", \\\"mm\\\" ]",
			voxel_size="[ 3, 3, 3 ]",
			coord_system="nidm:NIDM_0000047",
			number_of_dim="3",
			dimensions="[ 53, 63, 46 ]"),
		"CoordinateSpace-2": dict(
			coordinate_space_id="niiri:coordinate_space_id_2",
			label="Coordinate space 2",
			voxel_to_world_mapping="[[-3, 0, 0, 81],[0, 3, 0, -115],[0, 0, 3, -53],[0, 0, 0, 1]]",
			voxel_units="[ \\\"mm\\\", \\\"mm\\\", \\\"mm\\\" ]",
			voxel_size="[ 3, 3, 3 ]",
			coord_system="nidm:NIDM_0000047",
			number_of_dim="3",
			dimensions="[ 53, 63, 46 ]"),
		"ResidualMeanSquaresMap": dict(
			residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
			label="Residual Mean Squares Map",
			location="file://path/to/ResidualMeanSquares.nii.gz",
			filename="ResidualMeanSquares.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a",
			param_est_id="niiri:model_pe_id"),
		"MaskMap_Analysis": dict( # The analysis mask
			mask_id="niiri:mask_id_1",
			label="Mask",
			location="file://path/to/Mask.nii.gz",
			filename="Mask.nii.gz", 
			user_defined="false",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a",
			generated_by_act_id="niiri:model_pe_id",
			used_by_act_id="niiri:contrast_estimation_id"),
		"ContrastWeights": dict(
			contrast_id="niiri:contrast_id",
			label="Contrast weights: listening > rest",
			value="[ 1, 0, 0 ]",
			statistic_type=STATO_TSTATISTIC_STR,
			stat_type_comment=STATO_TSTATISTIC_LABEL,
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
		"ContrastMap": dict(
			contrast_map_id="niiri:contrast_map_id",
			label="Contrast Map: listening > rest",
			location="file://path/to/Contrast.nii.gz",
			format="image/nifti",
			filename="Contrast.nii.gz",
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
			sha="e43b6e01b0463fe7d40782137867a",
			contrast_est_id="niiri:contrast_estimation_id"),
		"FSL_DerivedMap-ContrastVariance": dict(
			derived_from_map_id="niiri:contrast_variance_map_id",
			derived_map_type="nidm:NIDM_0000135",
			filename="varcope1.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a",
			map_id="niiri:contrast_standard_error_map_id"
			),
		"StatisticMap": dict(
			statistic_map_id="niiri:statistic_map_id",
			label="Statistic Map: listening > rest",
			location="file://path/to/TStatistic_0001.nii.gz",
			format="image/nifti",
			filename="TStatistic_0001.nii.gz",
			statistic_type=STATO_TSTATISTIC_STR,
			stat_type_comment=STATO_TSTATISTIC_LABEL,
			contrast_name="listening > rest",
			error_dof="73.0",
			effect_dof="1",
			sha="400a2f07d99ed9be06577e6ecc89222cf4b688c654bc89067da558e88b73b97dd1b25e6c98f2a735fa0a1409598cff7e6025bda55abb6b9f5ef65d8d307eeba8",
			coordinate_space_id="niiri:coordinate_space_id_1",
			contrast_est_id="niiri:contrast_estimation_id"),
		"StatisticMap-Z": dict(
			statistic_map_id="niiri:z_statistic_map_id",
			label="Z-Statistic Map: listening > rest",
			location="file://path/to/ZStatistic_0001.nii.gz",
			format="image/nifti",
			filename="ZStatistic_0001.nii.gz",
			statistic_type=STATO_ZSTATISTIC_STR,
			contrast_name="listening > rest",
			error_dof="INF",
			effect_dof="1",
			sha="400a2f07d99ed9be06577e6ecc89222cf4b688c654bc89067da558e88b73b97dd1b25e6c98f2a735fa0a1409598cff7e6025bda55abb6b9f5ef65d8d307eeba8",
			coordinate_space_id="niiri:coordinate_space_id_1",
			contrast_est_id="niiri:contrast_estimation_id"),

        "HeightThreshold_equivThresh_equivThresh2": dict(
            height_threshold_id="niiri:height_threshold_id",
            thresh_type=OBO_P_VALUE_FWER_QNAME,
            label="Height Threshold: p<0.05 (FWE)",
            value="0.05",
            equiv_thresh="niiri:height_threshold_id_2",
            equiv_thresh2="niiri:height_threshold_id_3"
            ),
        "HeightThreshold-2": dict(
            height_threshold_id="niiri:height_threshold_id_2",
            thresh_type=OBO_STATISTIC_QNAME,
            label="Height Threshold",
            value="5.235300"
            ),
        "HeightThreshold-3": dict(
            height_threshold_id="niiri:height_threshold_id_3",
            thresh_type=NIDM_P_VALUE_UNCORRECTED_QNAME,
            label="Height Threshold",
            value="0.000001",
            ),
        "ExtentThreshold": dict(
            extent_threshold_id="niiri:extent_threshold_id",
            label="Cluster Threshold",
            thresh_type=OBO_P_VALUE_FWER_QNAME,
            value="1",
            ),
		"DisplayMaskMap": dict(
			display_map_id="niiri:display_map_id",
			label="Display Mask Map",
			location="file://path/to/DisplayMask.nii.gz",
			format="image/nifti",
			user_defined="true",
			filename="DisplayMask.nii.gz",
			coordinate_space_id="niiri:coordinate_space_id_2",
			sha="e43b6e01b0463fe7d40782137867a"
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
			connectivity="nidm:NIDM_0000128"
			),
		"Inference": dict(
			inference_id="niiri:inference_id",
			label="Inference",
			alternative_hyp="nidm:NIDM_0000060",
			stat_map_id="niiri:z_statistic_map_id", 
			height_thresh_id="niiri:height_threshold_id", 
			extent_thresh_id="niiri:extent_threshold_id", 
			display_mask_id="niiri:display_map_id", 
			peak_def_id="niiri:peak_definition_criteria_id", 
			cluster_def_id="niiri:cluster_definition_criteria_id",
			mask_id="niiri:mask_id_1",
			software_id="niiri:software_id"
			),
		"FSL_ExcursionSetMap": dict(
			id="niiri:excursion_set_map_id",
			label="Excursion Set Map",
			location="file://path/to/ExcursionSet.nii.gz",
			format="image/nifti",
			filename="ExcursionSet.nii.gz",
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
		"FSL_SupraThresholdCluster-1": dict(
			cluster_id="niiri:supra_threshold_cluster_0001",
			label="Supra-Threshold Cluster 0001",
			cluster_size_in_voxels="530",
			cluster_label_id="1",
			p_value_fwe="0.000000",
			excursion_set_id="niiri:excursion_set_map_id"
			),
		"FSL_ClusterCenterOfGravity-1": dict(
			center_of_gravity_id="niiri:center_of_gravity_1",
			label="Center of gravity 1",
			location="niiri:COG_coordinate_0001",
			cluster_id="niiri:supra_threshold_cluster_0001"
			),
		"FSL_Coordinate-COG1": dict(
			coordinate_id="niiri:COG_coordinate_0001",
			label="Coordinate 1",
			coord="[ 40.2, 16.4, 13.2 ]",
			coord_in_vox="[ -30.8, -68.5, -13.4 ]",
			),
		"FSL_SupraThresholdCluster-2": dict(
			cluster_id="niiri:supra_threshold_cluster_0002",
			label="Supra-Threshold Cluster 0002",
			cluster_size_in_voxels="445",
			cluster_label_id="2",
			p_value_fwe="0.000000",
			excursion_set_id="niiri:excursion_set_map_id"
			),
		"FSL_ClusterCenterOfGravity-2": dict(
			center_of_gravity_id="niiri:center_of_gravity_2",
			label="Center of gravity 2",
			location="niiri:COG_coordinate_0002",
			cluster_id="niiri:supra_threshold_cluster_0002"
			),
		"FSL_Coordinate-COG2": dict(
			coordinate_id="niiri:COG_coordinate_0002",
			label="Coordinate 2",
			coord="[ 25.6, 12.8, 14.6 ]",
			coord_in_vox="[ 24.1, -77.1, -4.27 ]"
			),
		"Peak-M1": dict(
			peak_id="niiri:peak_0001",
			label="Peak 1",
			p_uncorr="4.126074e-10",
			location="niiri:coordinate_0001",
			equiv_z="6.14",
			cluster_id="niiri:supra_threshold_cluster_0001"
			),
		"FSL_Coordinate-1": dict(
			coordinate_id="niiri:coordinate_0001",
			label="Coordinate 1",
			coord="[ -48.1, -73.7, -9.24 ]",
			coord_in_vox="[ 45, 15, 14 ]",
			),
		"Peak-2": dict(
			peak_id="niiri:peak_0002",
			label="Peak 2",
			p_uncorr="7.705712e-10",
			location="niiri:coordinate_0002",
			equiv_z="6.04",
			cluster_id="niiri:supra_threshold_cluster_0001"
			),
		"FSL_Coordinate-2": dict(
			coordinate_id="niiri:coordinate_0002",
			label="Coordinate 2",
			coord="[ -38.1, -53.4, -18 ]",
			coord_in_vox="[ 42, 21, 13 ]",
			),
		"Peak-3": dict(
			peak_id="niiri:peak_0003",
			label="Peak 3",
			p_uncorr="4.462172e-09",
			location="niiri:coordinate_0003",
			equiv_z="5.75",
			cluster_id="niiri:supra_threshold_cluster_0001"
			),
		"FSL_Coordinate-3": dict(
			coordinate_id="niiri:coordinate_0003",
			label="Coordinate 3",
			coord="[ -29.6, -73.8, -16.9 ]",
			coord_in_vox="[ 40, 15, 12 ]",
			),
		"Peak-4": dict(
			peak_id="niiri:peak_0004",
			label="Peak 4",
			p_uncorr="4.462172e-09",
			location="niiri:coordinate_0004",
			equiv_z="5.75",
			cluster_id="niiri:supra_threshold_cluster_0001"
			),
		"FSL_Coordinate-4": dict(
			coordinate_id="niiri:coordinate_0004",
			label="Coordinate 4",
			coord="[ 0.791, -87.2, 3.23 ]",
			coord_in_vox="[ 39, 13, 12 ]"
			),
		"Peak-M5": dict(
			peak_id="niiri:peak_0005",
			label="Peak 5",
			p_uncorr="2.178976e-09",
			location="niiri:coordinate_0005",
			equiv_z="5.87",
			cluster_id="niiri:supra_threshold_cluster_0002"
			),
		"FSL_Coordinate-5": dict(
			coordinate_id="niiri:coordinate_0005",
			label="Coordinate 5",
			coord="[ 16.1, -96.6, 5.82 ]",
			coord_in_vox="[ 32, 10, 16 ]"
			),
		"Peak-6": dict(
			peak_id="niiri:peak_0006",
			label="Peak 6",
			p_uncorr="8.022392e-09",
			location="niiri:coordinate_0006",
			equiv_z="5.65",
			cluster_id="niiri:supra_threshold_cluster_0002"
			),
		"FSL_Coordinate-6": dict(
			coordinate_id="niiri:coordinate_0006",
			label="Coordinate 6",
			coord="[ -25.5, -80.4, 15.3 ]",
			coord_in_vox="[ 28, 7, 16 ]"
			),
		"FSL_SearchSpaceMaskMap": dict(
			search_space_id="niiri:search_space_mask_id",
			location="file://path/to/SearchSpaceMask.nii.gz",
			filename="SearchSpaceMask.nii.gz",
			label="Search Space Mask Map",
			user_defined="false",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_2",
			search_vol_voxels="45359",
            search_vol_units="1.93808e+06",
            search_vol_resels="3753.84",			
			resel_size="12.2251",
			noise_roughness="0.384676",
			random_field_station="true",
			sha="400a2f07d99ed9be06577e6ecc89222cf4b688c654bc89067da558e88b73b97dd1b25e6c98f2a735fa0a1409598cff7e6025bda55abb6b9f5ef65d8d307eeba8",
			inference_id="niiri:inference_id",
            noise_fwhm_in_voxels="[2.38803, 2.43263, 2.07288]",
            noise_fwhm_in_units="[8.35811, 8.5142, 7.2551]"
			),
		"NIDMBundle": dict(
			bundle_id="niiri:fsl_results_id",
			label="NIDM-Results",
			object_model="nidm:NIDM_0000027",
			version="1.1.0",
			time="2014-05-19T10:30:00.000+01:00",
			export_id="niiri:export_id"
			),
		"FSL_Software": dict(
			software_id="niiri:software_id",
			software_type="nlx:birnlex_2067",
			label="FSL",
			version="5.0.x",
			feat_version="6.00"
			),
		"ExporterSoftware": dict(
			software_id="niiri:exporter_id",
			software_type="nidm:NIDM_0000167",
			label="nidmfsl",
			version="0.2.0"
			),
		"Export": dict(
			export_id="niiri:export_id",
			label="NIDM-Results export",
			exporter_id="niiri:exporter_id"
			),
		"GrandMeanMap": dict(
			grand_mean_map_id="niiri:grand_mean_map_id",
			label="Grand Mean Map",
			location="file://path/to/GrandMean.nii.gz",
			filename="GrandMean.nii.gz",
			format="image/nifti",
			masked_median="115",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a",
			model_pe_id="niiri:model_pe_id"
			)
		}

	NIDM_FSL_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'fsl')
	ttl_file = os.path.join(NIDM_FSL_DIR, 'fsl_results.ttl')
	example = ExampleFromTemplate(nidm_classes, ttl_file, False)
	example.create_example()
	
if __name__ == '__main__':
	main()