"""
Create SPM example 003 stored in nidm/nidm-results/spm/example003 by using the
class templates available in nidm/nidm-results/terms/templates

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
    STATO_TSTATISTIC_LABEL, NIDM_P_VALUE_UNCORRECTED_QNAME, \
    OBO_STATISTIC_QNAME, OBO_P_VALUE_FWER_QNAME


def main():
    nidm_classes = {
        "DesignMatrix": dict(
            design_matrix_id='niiri:design_matrix_id',
            label="Design Matrix",
            location="DesignMatrix.csv",
            format="text/csv",
            filename="DesignMatrix.csv",
            design_matrix_png_id="niiri:design_matrix_png_id"),
        "Image-DesignMatrix": dict(
            image_id="niiri:design_matrix_png_id",
            location="DesignMatrix.png",
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
            label="Beta Map 1",
            location="ParameterEstimate_0001.nii.gz",
            filename="ParameterEstimate_0001.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            param_est_id="niiri:model_pe_id"),
        "DerivedMap-PE1": dict(
            derived_from_map_id="niiri:beta_map_id_1_der",
            derived_map_type="nidm:NIDM_0000061",
            filename="beta_0001.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a",
            map_id="niiri:beta_map_id_1"
            ),
        "ParameterEstimateMap_Location-2": dict(
            beta_map_id="niiri:beta_map_id_2",
            label="Beta Map 2",
            location="ParameterEstimate_0002.nii.gz",
            filename="ParameterEstimate_0002.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            param_est_id="niiri:model_pe_id"),
        "DerivedMap-PE2": dict(
            derived_from_map_id="niiri:beta_map_id_2_der",
            derived_map_type="nidm:NIDM_0000061",
            filename="beta_0002.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a",
            map_id="niiri:beta_map_id_2"
            ),
        "ParameterEstimateMap_Location-3": dict(
            beta_map_id="niiri:beta_map_id_3",
            label="Beta Map 3",
            location="ParameterEstimate_0003.nii.gz",
            filename="ParameterEstimate_0003.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            param_est_id="niiri:model_pe_id"),
        "DerivedMap-PE3": dict(
            derived_from_map_id="niiri:beta_map_id_3_der",
            derived_map_type="nidm:NIDM_0000061",
            filename="beta_0003.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a",
            map_id="niiri:beta_map_id_3"
            ),
        "CoordinateSpace-1": dict(
            coordinate_space_id="niiri:coordinate_space_id_1",
            label="Coordinate space 1",
            voxel_to_world_mapping="[[-3, 0, 0, 78],[0, 3, 0, -112],[0, 0, 3, \
-50],[0, 0, 0, 1]]",
            voxel_units="[ \\\"mm\\\", \\\"mm\\\", \\\"mm\\\" ]",
            voxel_size="[ 3, 3, 3 ]",
            coord_system="nidm:NIDM_0000051",
            number_of_dim="3",
            dimensions="[ 53, 63, 46 ]"),
        "ResidualMeanSquaresMap": dict(
            residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
            label="Residual Mean Squares Map",
            location="ResidualMeanSquares.nii.gz",
            filename="ResidualMeanSquares.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            param_est_id="niiri:model_pe_id"),
        "MaskMap_Analysis": dict(  # The analysis mask
            mask_id="niiri:mask_id_1",
            label="Mask",
            location="Mask.nii.gz",
            filename="Mask.nii.gz",
            user_defined="false",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            generated_by_act_id="niiri:model_pe_id",
            # fixme: also used by niiri:contrast_estimation_id_2
            used_by_act_id="niiri:contrast_estimation_id"),
        "ContrastWeights": dict(
            contrast_id="niiri:contrast_id",
            label="Contrast: listening > reading",
            value="[1, -1, 0, 0]",
            statistic_type=STATO_TSTATISTIC_STR,
            stat_type_comment=STATO_TSTATISTIC_LABEL,
            contrast_name="listening > reading"
            ),
        "ContrastWeights-2": dict(
            contrast_id="niiri:contrast_id_2",
            label="Contrast: motor",
            value="[ 0, 0, 1 ]",
            statistic_type=STATO_TSTATISTIC_STR,
            stat_type_comment=STATO_TSTATISTIC_LABEL,
            contrast_name="motor"
            ),
        "ContrastEstimation": dict(
            contrast_estimation_id="niiri:contrast_estimation_id",
            label="Contrast estimation 1",
            software_id="niiri:software_id",
            mask_id="niiri:mask_id_1",
            residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
            design_matrix_id="niiri:design_matrix_id",
            contrast_id="niiri:contrast_id",
            param_est_map="niiri:beta_map_id_1"
            ),
        "ContrastEstUsedParamEst-Con1PE2": dict(
            contrast_estimation_id="niiri:contrast_estimation_id",
            param_est_map="niiri:beta_map_id_2"
            ),
        "ContrastEstimation-2": dict(
            contrast_estimation_id="niiri:contrast_estimation_id_2",
            label="Contrast estimation 2",
            software_id="niiri:software_id",
            mask_id="niiri:mask_id_1",
            residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
            design_matrix_id="niiri:design_matrix_id",
            contrast_id="niiri:contrast_id_2",
            param_est_map="niiri:beta_map_id_3"
            ),
        "ContrastEstUsedParamEst-Con2PE3": dict(
            contrast_estimation_id="niiri:contrast_estimation_id_2",
            param_est_map="niiri:beta_map_id_3"
            ),
        "ContrastMap": dict(
            contrast_map_id="niiri:contrast_map_id",
            label="Contrast Map: listening > reading",
            location="Contrast_0001.nii.gz",
            format="image/nifti",
            filename="Contrast_0001.nii.gz",
            contrast_name="listening > reading",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            contrast_est_id="niiri:contrast_estimation_id"),
        "ContrastMap-2": dict(
            contrast_map_id="niiri:contrast_map_id_2",
            label="Contrast Map: motor",
            location="Contrast_0002.nii.gz",
            format="image/nifti",
            filename="Contrast_0002.nii.gz",
            contrast_name="motor",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            contrast_est_id="niiri:contrast_estimation_id_2"),
        "DerivedMap-ContrastMap-2": dict(
            derived_from_map_id="niiri:contrast_map_id_2_der",
            derived_map_type="nidm:NIDM_0000002",
            filename="con_0002.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a",
            map_id="niiri:contrast_map_id_2"
            ),
        "ContrastStandardErrorMap": dict(
            contrast_standard_error_map_id="niiri:contrast_standard_error_map_\
id",
            label="Contrast 1 Standard Error Map",
            location="ContrastStandardError_0001.nii.gz",
            format="image/nifti",
            filename="ContrastStandardError_0001.nii.gz",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            contrast_est_id="niiri:contrast_estimation_id"),
        "ContrastStandardErrorMap-2": dict(
            contrast_standard_error_map_id="niiri:contrast_standard_error_map_\
id_2",
            label="Contrast 2 Standard Error Map",
            location="ContrastStandardError_0002.nii.gz",
            format="image/nifti",
            filename="ContrastStandardError_0002.nii.gz",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            contrast_est_id="niiri:contrast_estimation_id_2"),
        "StatisticMap_T": dict(
            statistic_map_id="niiri:statistic_map_id",
            label="Statistic Map: listening > reading",
            location="TStatistic_0001.nii.gz",
            format="image/nifti",
            filename="TStatistic_0001.nii.gz",
            statistic_type=STATO_TSTATISTIC_STR,
            stat_type_comment=STATO_TSTATISTIC_LABEL,
            contrast_name="listening > reading",
            error_dof="72.9999999990787",
            effect_dof="1",
            sha="e43b6e01b0463fe7d40782137867a",
            coordinate_space_id="niiri:coordinate_space_id_1",
            contrast_est_id="niiri:contrast_estimation_id"),
        "DerivedMap-StatMap": dict(
            derived_from_map_id="niiri:statistic_map_id_der",
            derived_map_type="nidm:NIDM_0000076",
            filename="spmT_0001.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a",
            map_id="niiri:statistic_map_id"
            ),
        "StatisticMap_T-2": dict(
            statistic_map_id="niiri:statistic_map_id_2",
            label="Statistic Map: motor",
            location="TStatistic_0002.nii.gz",
            format="image/nifti",
            filename="TStatistic_0002.nii.gz",
            statistic_type=STATO_TSTATISTIC_STR,
            stat_type_comment=STATO_TSTATISTIC_LABEL,
            contrast_name="motor",
            error_dof="72.9999999990787",
            effect_dof="1",
            sha="e43b6e01b0463fe7d40782137867a",
            coordinate_space_id="niiri:coordinate_space_id_1",
            contrast_est_id="niiri:contrast_estimation_id_2"),
        "DerivedMap-StatMap-2": dict(
            derived_from_map_id="niiri:statistic_map_id_2_der",
            derived_map_type="nidm:NIDM_0000076",
            filename="spmT_0002.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a",
            map_id="niiri:statistic_map_id_2"
            ),
        "HeightThreshold_equivThresh_equivThresh2": dict(
            height_threshold_id="niiri:height_threshold_id",
            thresh_type=NIDM_P_VALUE_UNCORRECTED_QNAME,
            label="Height Threshold: p<7.62276079258051e-07 (unc)",
            value="7.62276079258051e-07",
            equiv_thresh="niiri:height_threshold_id_2",
            equiv_thresh2="niiri:height_threshold_id_3"
            ),
        "HeightThreshold-2": dict(
            height_threshold_id="niiri:height_threshold_id_2",
            thresh_type=OBO_STATISTIC_QNAME,
            label="Height Threshold",
            value="5.23529984739211"
            ),
        "HeightThreshold-3": dict(
            height_threshold_id="niiri:height_threshold_id_3",
            thresh_type=OBO_P_VALUE_FWER_QNAME,
            label="Height Threshold",
            value="0.05",
            ),
        "ExtentThresholdStat_equivThresh_equivThresh2_clusterSizeResels": dict(
            extent_threshold_id="niiri:extent_threshold_id",
            label="Extent Threshold: k>=10",
            cluster_size_vox="10",
            cluster_size_resels="3.3",
            equiv_thresh="niiri:height_threshold_id_2",
            equiv_thresh2="niiri:height_threshold_id_3"
            ),
        "ExtentThreshold-2": dict(
            extent_threshold_id="niiri:extent_threshold_id_2",
            label="Extent Threshold",
            thresh_type=OBO_P_VALUE_FWER_QNAME,
            value="1",
            ),
        "ExtentThreshold-3": dict(
            extent_threshold_id="niiri:extent_threshold_id_3",
            label="Extent Threshold",
            thresh_type=NIDM_P_VALUE_UNCORRECTED_QNAME,
            value="1",
            ),
        "DisplayMaskMap": dict(
            display_map_id="niiri:display_map_id",
            label="Display Mask Map",
            user_defined="true",
            location="DisplayMask.nii.gz",
            filename="DisplayMask.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a"
            ),
        "PeakDefinitionCriteria_MaxPeaks": dict(
            peak_definition_criteria_id="niiri:peak_definition_criteria_id",
            label="Peak Definition Criteria",
            max_num_peaks="3",
            min_dist_peaks="8.0"
            ),
        "ClusterDefinitionCriteria": dict(
            cluster_definition_criteria_id="niiri:cluster_definition_criteria_\
id",
            label="Cluster Connectivity Criterion: 18",
            connectivity="nidm:NIDM_0000128"
            ),
        "ConjunctionInference": dict(
            conj_inference_id="niiri:inference_id",
            label="Conjunction Inference",
            alternative_hyp="nidm:NIDM_0000060",
            stat_map_id_1="niiri:statistic_map_id",
            stat_map_id_2="niiri:statistic_map_id_2",
            height_thresh_id="niiri:height_threshold_id",
            extent_thresh_id="niiri:extent_threshold_id",
            display_mask_id="niiri:display_map_id",
            peak_def_id="niiri:peak_definition_criteria_id",
            cluster_def_id="niiri:cluster_definition_criteria_id",
            mask_id="niiri:mask_id_1",
            software_id="niiri:software_id"
            ),
        "SearchSpaceMaskMap": dict(  # The "search space"
            search_space_id="niiri:search_space_mask_id",
            location="SearchSpaceMask.nii.gz",
            filename="SearchSpaceMask.nii.gz",
            label="Search Space Mask Map",
            format="image/nifti",
            user_defined="false",
            coordinate_space_id="niiri:coordinate_space_id_1",
            expected_num_voxels="4.02834655908613",
            expected_num_clusters="0.0512932943875478",
            height_critical_fwe05="4.85241745689539",
            height_critical_fdr05="5.7639536857605",
            smallest_size_fwe05="12",
            smallest_size_fdr05="29",
            search_vol_voxels="69306",
            search_vol_units="1871262",
            resel_size="132.907586178202",
            search_vol_resels="467.07642343881",
            search_vol_resels_geom="[7, 42.96312274763, 269.40914815306, \
467.07642343881]",
            noise_fwhm_in_voxels="[ 5.41278985910694, 5.43638957240286, \
4.51666658877481 ]",
            noise_fwhm_in_units="[ 16.2383695773208, 16.3091687172086, \
13.5499997663244 ]",
            random_field_station="true",
            sha="932fd9f0d55e9822748f4a9b35a0a7f0fe442f3e061e2eda48c2617a2938\
df50ea84deca8de0725641a0105b712a80a0c8931df9bdf3bef788b1041379d00875",
            inference_id="niiri:inference_id"
            ),
        "DerivedMap-Contrast": dict(
            derived_from_map_id="niiri:contrast_map_id_der",
            derived_map_type="nidm:NIDM_0000002",
            filename="con_0001.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a",
            map_id="niiri:contrast_map_id"
            ),
        "NIDMBundle": dict(
            bundle_id="niiri:spm_results_id",
            label="NIDM-Results",
            object_model="nidm:NIDM_0000027",
            version="1.1.0",
            time="2014-05-19T10:30:00.000+01:00",
            export_id="niiri:export_id"
            ),
        "SPM_ReselsPerVoxelMap": dict(
            resels_per_voxel_map_id="niiri:resels_per_voxel_map_id",
            label="Resels per Voxel Map",
            location="ReselsPerVoxel.nii.gz",
            filename="ReselsPerVoxel.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            model_pe_id="niiri:model_pe_id"
            ),
        "SPM_InferenceUsedRPVMap": dict(
            inference_id="niiri:inference_id",
            resels_per_voxel_map_id="niiri:resels_per_voxel_map_id"
        ),
        "DerivedMap-RPV": dict(
            derived_from_map_id="niiri:resels_per_voxel_map_id_der",
            derived_map_type="nidm:NIDM_0000144",
            filename="RPV.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a",
            map_id="niiri:resels_per_voxel_map_id"
            ),
        "SPM_Software": dict(
            software_id="niiri:software_id",
            software_type="nlx:nif-0000-00343",
            label="SPM",
            version="12b.5853"
            ),
        "GrandMeanMap": dict(
            grand_mean_map_id="niiri:grand_mean_map_id",
            label="Grand Mean Map",
            location="GrandMean.nii.gz",
            filename="GrandMean.nii.gz",
            format="image/nifti",
            masked_median="115",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            model_pe_id="niiri:model_pe_id"
            ),
        "ExporterSoftware": dict(
            software_id="niiri:exporter_id",
            software_type="nidm:NIDM_0000168",
            label="spm_results_nidm",
            version="12b.5858"
            ),
        "Export": dict(
            export_id="niiri:export_id",
            label="NIDM-Results export",
            exporter_id="niiri:exporter_id"
            ),
        "ExcursionSetMap": dict(
            id="niiri:excursion_set_map_id",
            label="Excursion Set Map",
            location="ExcursionSet.nii.gz",
            format="image/nifti",
            filename="ExcursionSet.nii.gz",
            cluster_label_map_id="niiri:cluster_label_map_id",
            max_intensity_projection_id="niiri:maximum_intensity_projection\
_id",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="d96b82761c299a66978893cab6034f3f8aed25d0a135636b0ffe79f4cf11b\
ecce86ba261f7aeb43717f5d0e47ad0b14cfb0402786251e3f2c507890c83b27652",
            num_of_clusters="5",
            p_value="2.83510681598e-09",
            inference_id="niiri:inference_id"
            ),
        "SupraThresholdCluster-1": dict(
            cluster_id="niiri:supra_threshold_cluster_0001",
            label="Supra-Threshold Cluster: 0001",
            cluster_size_in_voxels="839",
            cluster_label_id="1",
            cluster_size_in_resels="6.31265696809113",
            p_value_unc="3.55896824480477e-19",
            p_value_fwe="0",
            p_value_fdr="1.77948412240239e-18",
            excursion_set_id="niiri:excursion_set_map_id"
            ),
        "SupraThresholdCluster-2": dict(
            cluster_id="niiri:supra_threshold_cluster_0002",
            label="Supra-Threshold Cluster: 0002",
            cluster_size_in_voxels="695",
            cluster_label_id="2",
            cluster_size_in_resels="5.22919736927692",
            p_value_unc="5.34280282632073e-17",
            p_value_fwe="0",
            p_value_fdr="1.33570070658018e-16",
            excursion_set_id="niiri:excursion_set_map_id"
            ),
        "SupraThresholdCluster-3": dict(
            cluster_id="niiri:supra_threshold_cluster_0003",
            label="Supra-Threshold Cluster: 0003",
            cluster_size_in_voxels="37",
            cluster_label_id="3",
            cluster_size_in_resels="0.278388924695318",
            p_value_unc="0.00497953247554004",
            p_value_fwe="0.000255384009130943",
            p_value_fdr="0.00829922079256674",
            excursion_set_id="niiri:excursion_set_map_id"
            ),
        "SupraThresholdCluster-4": dict(
            cluster_id="niiri:supra_threshold_cluster_0004",
            label="Supra-Threshold Cluster: 0004",
            cluster_size_in_voxels="29",
            cluster_label_id="4",
            cluster_size_in_resels="0.218196724761195",
            p_value_unc="0.0110257032104773",
            p_value_fwe="0.000565384750377596",
            p_value_fdr="0.0137821290130967",
            excursion_set_id="niiri:excursion_set_map_id"
            ),
        "SupraThresholdCluster-5": dict(
            cluster_id="niiri:supra_threshold_cluster_0005",
            label="Supra-Threshold Cluster: 0005",
            cluster_size_in_voxels="12",
            cluster_label_id="5",
            cluster_size_in_resels="0.0902882999011843",
            p_value_unc="0.0818393184514307",
            p_value_fwe="0.00418900977248904",
            p_value_fdr="0.0818393184514307",
            excursion_set_id="niiri:excursion_set_map_id"
            ),
        "Peak_ValueP-1": dict(
            peak_id="niiri:peak_0001",
            label="Peak: 0001",
            location="niiri:coordinate_0001",
            value="17.5207633972168",
            equiv_z="INF",
            p_uncorr="4.44089209850063e-16",
            p_value_fwe="0",
            p_value_fdr="1.19156591713838e-11",
            cluster_id="niiri:supra_threshold_cluster_0001"
            ),
        "Coordinate-1": dict(
            coordinate_id="niiri:coordinate_0001",
            label="Coordinate: 0001",
            coord="[ -60, -25, 11 ]"
            ),
        "Peak_ValueP-2": dict(
            peak_id="niiri:peak_0002",
            label="Peak: 0002",
            location="niiri:coordinate_0002",
            value="13.0321407318",
            equiv_z="INF",
            p_uncorr="4.44089209850063e-16",
            p_value_fwe="0",
            p_value_fdr="1.19156591714e-11",
            cluster_id="niiri:supra_threshold_cluster_0001"
            ),
        "Coordinate-2": dict(
            coordinate_id="niiri:coordinate_0002",
            label="Coordinate: 0002",
            coord="[ -42, -31, 11 ]"
            ),
        "Peak_ValueP-3": dict(
            peak_id="niiri:peak_0003",
            label="Peak: 0003",
            location="niiri:coordinate_0003",
            value="10.2856016159058",
            equiv_z="INF",
            p_uncorr="4.44089209850063e-16",
            p_value_fwe="7.69451169446711e-12",
            p_value_fdr="6.84121260274992e-10",
            cluster_id="niiri:supra_threshold_cluster_0001"
            ),
        "Coordinate-3": dict(
            coordinate_id="niiri:coordinate_0003",
            label="Coordinate: 0003",
            coord="[ -66, -31, -1 ]"
            ),
        "Peak_ValueP-4": dict(
            peak_id="niiri:peak_0004",
            label="Peak: 0004",
            location="niiri:coordinate_0004",
            value="13.5425577163696",
            equiv_z="INF",
            p_uncorr="4.44089209850063e-16",
            p_value_fwe="0",
            p_value_fdr="1.19156591713838e-11",
            cluster_id="niiri:supra_threshold_cluster_0002"
            ),
        "Coordinate-4": dict(
            coordinate_id="niiri:coordinate_0004",
            label="Coordinate: 0004",
            coord="[ 63, -13, -4 ]"
            )        
        }

    NIDM_SPM_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'spm', "example003")
    ttl_file = os.path.join(NIDM_SPM_DIR, 'spm_results_conjunction.ttl')
    example = ExampleFromTemplate(nidm_classes, ttl_file, False)
    example.create_example()

if __name__ == '__main__':
    main()
