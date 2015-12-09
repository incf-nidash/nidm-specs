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
    STATO_ZSTATISTIC_STR, STATO_TSTATISTIC_LABEL, STATO_ZSTATISTIC_LABEL, \
    OBO_P_VALUE_FWER_QNAME, OBO_STATISTIC_QNAME


def main():
    nidm_classes = {
        "DesignMatrix_1stLevel": dict(
            design_matrix_id='niiri:design_matrix_id',
            label="Design Matrix",
            location="DesignMatrix.csv",
            format="text/csv",
            filename="DesignMatrix.csv",
            design_matrix_png_id="niiri:design_matrix_png_id",
            regressors="[\\\"Gen\\\", \\\"Gen*temporal_derivative\\\""
            ", \\\"Shad\\\", \\\"Shad*temporal_derivative\\\"]",
            hrf_basis="fsl:FSL_0000001",
            drift_model="niiri:drift_model_id"),
        "FSL_DriftModel": dict(
            id="niiri:drift_model_id",
            label="FSL's Gaussian Running Line Drift Model",
            cut_off="1908"
            ),
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
            target="10000"
            ),
        "ErrorModel": dict(
            error_model_id="niiri:error_model_id",
            noise_distribution="obo:STATO_0000227",
            variance_homo="true",
            variance_spatial="nidm:NIDM_0000073",
            dependence="obo:STATO_0000357",
            dependence_spatial="nidm:NIDM_0000074"
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
        "ParameterEstimateMap-1": dict(
            beta_map_id="niiri:beta_map_id_1",
            label="Parameter estimate 1",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            param_est_id="niiri:model_parameters_estimation_id"),
        "ParameterEstimateMap-2": dict(
            beta_map_id="niiri:beta_map_id_2",
            label="Parameter estimate 2",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            param_est_id="niiri:model_parameters_estimation_id"),
        "ParameterEstimateMap-3": dict(
            beta_map_id="niiri:beta_map_id_3",
            label="Parameter estimate 3",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            param_est_id="niiri:model_parameters_estimation_id"),
        "ParameterEstimateMap-4": dict(
            beta_map_id="niiri:beta_map_id_4",
            label="Parameter estimate 4",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            param_est_id="niiri:model_parameters_estimation_id"),
        "CoordinateSpace": dict(
            coordinate_space_id="niiri:coordinate_space_id_1",
            label="Coordinate space",
            voxel_to_world_mapping="[[ -3.5, 0, 0, 108.5], \
[ 0, 3.5, 0, -108.5], [ 0, 0, 3.5, -52.5], [ 0, 0, 0, 1]]",
            voxel_units="[ \\\"mm\\\", \\\"mm\\\", \\\"mm\\\" ]",
            voxel_size="[ 3.5, 3.5, 3.5 ]",
            coord_system="nidm:NIDM_0000077",
            number_of_dim="3",
            dimensions="[ 64, 64, 42 ]"),
        "ResidualMeanSquaresMap": dict(
            residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
            label="Residual Mean Squares Map",
            location="ResidualMeanSquares.nii.gz",
            filename="ResidualMeanSquares.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="1327a300eb1e20d42c67abb3c49a47b80ecabfebd13d0ba0aca0560e8bf43\
891f0e35a958c1afa84e041f62cf0038f58b4ab71f68b0b50d4153210aeed74f4ff",
            param_est_id="niiri:model_parameters_estimation_id"),
        "MaskMap_Analysis": dict(  # Analysis mask
            mask_id="niiri:mask_id_1",
            label="Mask",
            location="Mask.nii.gz",
            filename="Mask.nii.gz",
            user_defined="false",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="cc1a96a6111e5107eb08487e38e6d7f8164b9d1d3f1fc10948bdbcfaea642\
fe9bfae278c7fc372b65cac7232ea58fd8fb5914014e7b9a5d6200592b12b2a728b",
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
        "ContrastMap": dict(
            contrast_map_id="niiri:contrast_map_id_1",
            label="Contrast Map: Generation",
            location="Contrast.nii.gz",
            format="image/nifti",
            filename="Contrast.nii.gz",
            contrast_name="Generation",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="4c755c0ae6088f8001e0458f89e51fea0e2719b5dc747fed6f617ae12ad5c\
6a643e1afcb886bcabaaac7911f5e69086c1bd084af9f75dae75913d44a783151f6",
            contrast_est_id="niiri:contrast_estimation_id_1"),
        "ContrastStandardErrorMap": dict(
            contrast_standard_error_map_id="niiri:contrast_standard_error_map\
_id_1",
            label="Contrast Standard Error Map",
            location="ContrastStandardError.nii.gz",
            format="image/nifti",
            filename="ContrastStandardError.nii.gz",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="8529f3ff9f10da8f332ced9d579990321475c1498b56d79ede560ba2eccf6\
d68718757dc7af78eb1e86617a41e6c9f55161f756d184e2b0fb06c3d419dc99856",
            contrast_est_id="niiri:contrast_estimation_id_1"),
        "DerivedMap-ContrastVariance": dict(
            derived_from_map_id="niiri:d4de4b20b2d408cd8d825ac0edb6030a",
            derived_map_type="nidm:NIDM_0000135",
            filename="varcope1.nii.gz",
            format="image/nifti",
            sha="7d183bbacc0b99cd1db84174d32445457f532bca9f774fdcc53bc1d0faa5e\
7d250a1abf03864bd90b30f96f5a7516e0056104a729a565019b0f254a8a7bced1e",
            map_id="niiri:contrast_standard_error_map_id_1"
            ),
        "StatisticMap": dict(
            statistic_map_id="niiri:statistic_map_id_1",
            label="Statistic Map: Generation",
            location="TStatistic.nii.gz",
            format="image/nifti",
            filename="TStatistic.nii.gz",
            statistic_type=STATO_TSTATISTIC_STR,
            stat_type_comment=STATO_TSTATISTIC_LABEL,
            contrast_name="Generation",
            error_dof="102",
            effect_dof="1",
            sha="b6286d36e678c23622b5b0486f0efb5b274f9a5e2a3ee6aceb6a0338f7745\
fb8a4d8f72b8af22c4ffb40c860bfb65940c87b03a7336cdf1a665f9cb07a5c2527",
            coordinate_space_id="niiri:coordinate_space_id_1",
            contrast_est_id="niiri:contrast_estimation_id_1"),
        "StatisticMap-Z": dict(
            statistic_map_id="niiri:z_statistic_map_id_1",
            label="Z-Statistic Map: Generation",
            location="ZStatistic.nii.gz",
            format="image/nifti",
            filename="ZStatistic.nii.gz",
            statistic_type=STATO_ZSTATISTIC_STR,
            stat_type_comment=STATO_ZSTATISTIC_LABEL,
            contrast_name="Generation",
            effect_dof="1",
            error_dof="INF",
            sha="3a68a4e5963766af86d22a871a4dbca9568a46441a567855b3a84dbd47ea0\
1acea11ed77b37ce85078a219adaa92264296a4548c1ba39b11ff028e8fefd95d03",
            coordinate_space_id="niiri:coordinate_space_id_1",
            contrast_est_id="niiri:contrast_estimation_id_1"),
        "HeightThreshold": dict(
            height_threshold_id="niiri:height_threshold_id",
            thresh_type=OBO_STATISTIC_QNAME,
            label="Height Threshold: Z>2.3",
            value="2.3",
            ),
        "ExtentThreshold": dict(
            extent_threshold_id="niiri:extent_threshold_id",
            label="Extent Threshold: p<0.05 (FWE)",
            thresh_type=OBO_P_VALUE_FWER_QNAME,
            value="0.05",
            ),
        "PeakDefinitionCriteria": dict(
            peak_definition_criteria_id="niiri:peak_definition_criteria_id_1",
            label="Peak Definition Criteria",
            min_dist_peaks="0.0"
            ),
        "ClusterDefinitionCriteria": dict(
            cluster_definition_criteria_id="niiri:cluster_definition_criteria\
_id_1",
            label="Cluster Connectivity Criterion: 26",
            connectivity="nidm:NIDM_0000129"
            ),
        "Inference": dict(
            inference_id="niiri:inference_id_1",
            label="Inference: Generation",
            alternative_hyp="nidm:NIDM_0000060",
            stat_map_id="niiri:z_statistic_map_id_1",
            height_thresh_id="niiri:height_threshold_id",
            extent_thresh_id="niiri:extent_threshold_id",
            peak_def_id="niiri:peak_definition_criteria_id_1",
            cluster_def_id="niiri:cluster_definition_criteria_id_1",
            mask_id="niiri:mask_id_1",
            software_id="niiri:software_id"
            ),
        "FSL_ExcursionSetMap": dict(
            id="niiri:excursion_set_map_id_1",
            label="Excursion Set Map",
            location="ExcursionSet.nii.gz",
            format="image/nifti",
            filename="ExcursionSet.nii.gz",
            cluster_label_map_id="niiri:cluster_label_map_id",
            png_id="niiri:excursion_set_png_id_1",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="c74e3c47e4308f27423a195c7c3e70b64b8fd362d612a2543da76bced67f6\
66949b70272033ab3d4b7d0bbbfe22b7da13d56d25521664be0c96454fd180ee4cc",
            inference_id="niiri:inference_id_1"
            ),
        "Image": dict(
            image_id="niiri:excursion_set_png_id_1",
            location="rendered_thresh_zstat1.png",
            filename="rendered_thresh_zstat1.png",
            format="image/png"
            ),
        "FSL_SupraThresholdCluster-1": dict(
            cluster_id="niiri:supra_threshold_cluster_0001",
            label="Supra-Threshold Cluster 0001",
            cluster_size_in_voxels="81",
            cluster_label_id="1",
            cluster_size_in_resels="23.1209189500945",
            p_value_fwe="0.00894",
            excursion_set_id="niiri:excursion_set_map_id_1"
            ),
        "FSL_ClusterCenterOfGravity-1": dict(
            center_of_gravity_id="niiri:center_of_gravity_1",
            label="Center of gravity 1",
            location="niiri:COG_coordinate_0001",
            cluster_id="niiri:supra_threshold_cluster_0001"
            ),
        "FSL_Coordinate-COG1": dict(
            coordinate_id="niiri:COG_coordinate_0001",
            label="Coordinate 0001",
            coord="[ -5.8, 19.1, 38.5 ]",
            coord_in_vox="[ 32.3, 39.2, 31.0 ]",
            ),
        "FSL_SupraThresholdCluster-2": dict(
            cluster_id="niiri:supra_threshold_cluster_0002",
            label="Supra-Threshold Cluster 0002",
            cluster_size_in_voxels="117",
            cluster_label_id="2",
            cluster_size_in_resels="19.4128470430038",
            p_value_fwe="0.000621",
            excursion_set_id="niiri:excursion_set_map_id_1"
            ),
        "FSL_ClusterCenterOfGravity-2": dict(
            center_of_gravity_id="niiri:center_of_gravity_2",
            label="Center of gravity 2",
            location="niiri:COG_coordinate_0002",
            cluster_id="niiri:supra_threshold_cluster_0002"
            ),
        "FSL_Coordinate-COG2": dict(
            coordinate_id="niiri:COG_coordinate_0002",
            label="Coordinate 0002",
            coord="[ -56.9, -57.1, 9.86 ]",
            coord_in_vox="[ 47.1, 19.2, 19.7 ]",
            ),
        "FSL_SupraThresholdCluster-3": dict(
            cluster_id="niiri:supra_threshold_cluster_0003 ",
            label="Supra-Threshold Cluster 0003",
            cluster_size_in_voxels="499",
            cluster_label_id="3",
            cluster_size_in_resels="19.4128470430038",
            p_value_fwe="1.26e-12",
            excursion_set_id="niiri:excursion_set_map_id_1"
            ),
        "FSL_ClusterCenterOfGravity-3 ": dict(
            center_of_gravity_id="niiri:center_of_gravity_3 ",
            label="Center of gravity 3",
            location="niiri:COG_coordinate_0003 ",
            cluster_id="niiri:supra_threshold_cluster_0003 "
            ),
        "FSL_Coordinate-COG3 ": dict(
            coordinate_id="niiri:COG_coordinate_0003 ",
            label="Coordinate 0003",
            coord="[ -47.2, 17.3, 9.18 ]",
            coord_in_vox="[ 43.4, 40.3, 23.9 ]",
            ),
        "FSL_SupraThresholdCluster-4": dict(
            cluster_id="niiri:supra_threshold_cluster_0004 ",
            label="Supra-Threshold Cluster 0004",
            cluster_size_in_voxels="1203",
            cluster_label_id="4",
            p_value_fwe="8.02e-24",
            excursion_set_id="niiri:excursion_set_map_id_1"
            ),
        "FSL_ClusterCenterOfGravity-4  ": dict(
            center_of_gravity_id="niiri:center_of_gravity_4",
            label="Center of gravity 4",
            location="niiri:COG_coordinate_0004  ",
            cluster_id="niiri:supra_threshold_cluster_0004  "
            ),
        "FSL_Coordinate-COG4  ": dict(
            coordinate_id="niiri:COG_coordinate_0004  ",
            label="Coordinate 0004",
            coord="[ -7.38, -72.5, -8.5 ]",
            coord_in_vox="[ 34.0, 14.7, 14.0 ]",
            ),
        "Peak-M4-1": dict(
            peak_id="niiri:peak_0004_1",
            label="Peak 0004_1",
            p_uncorr="3.51932e-09",
            location="niiri:coordinate_0004_1",
            equiv_z="5.79",
            cluster_id="niiri:supra_threshold_cluster_0004"
            ),
        "FSL_Coordinate-4-1": dict(
            coordinate_id="niiri:coordinate_0004_1",
            label="Coordinate 0004_1",
            coord="[ -33.7, -66.7, -14.7 ]",
            coord_in_vox="[ 41, 17, 13 ]",
            ),
        "Peak-4-2": dict(
            peak_id="niiri:peak_0004_2",
            label="Peak 0004_2",
            p_uncorr="9.01048e-09",
            location="niiri:coordinate_0004_2",
            equiv_z="5.63",
            cluster_id="niiri:supra_threshold_cluster_0004"
            ),
        "FSL_Coordinate-4-2": dict(
            coordinate_id="niiri:coordinate_0004_2",
            label="Coordinate 0004_2",
            coord="[ -38.0, -53.9, -21.9 ]",
            coord_in_vox="[ 42, 21, 12 ]",
            ),
        "Peak-4-3": dict(
            peak_id="niiri:peak_0004_3",
            label="Peak 0004_3",
            p_uncorr="9.54787e-09",
            location="niiri:coordinate_0004_3",
            equiv_z="5.62",
            cluster_id="niiri:supra_threshold_cluster_0004"
            ),
        "FSL_Coordinate-4-3": dict(
            coordinate_id="niiri:coordinate_0004_3",
            label="Coordinate 0004_3",
            coord="[ 16.1, -96.6, 5.82 ]",
            coord_in_vox="[ 28, 7, 16 ]",
            ),
        "Peak-4-4": dict(
            peak_id="niiri:peak_0004_4",
            label="Peak 0004_4",
            p_uncorr="1.01163e-08",
            location="niiri:coordinate_0004_4",
            equiv_z="5.61",
            cluster_id="niiri:supra_threshold_cluster_0004"
            ),
        "FSL_Coordinate-4-4": dict(
            coordinate_id="niiri:coordinate_0004_4",
            label="Coordinate 0004_4",
            coord="[ -48.1, -73.7, -9.24 ]",
            coord_in_vox="[ 45, 15, 14 ]"
            ),
        "Peak-4-5": dict(
            peak_id="niiri:peak_0004_5",
            label="Peak 0004_5",
            p_uncorr="1.07176e-08",
            location="niiri:coordinate_0004_5",
            equiv_z="5.6",
            cluster_id="niiri:supra_threshold_cluster_0004"
            ),
        "FSL_Coordinate-4-5": dict(
            coordinate_id="niiri:coordinate_0004_5",
            label="Coordinate 0004_5",
            coord="[ -25.5, -80.4, -15.3 ]",
            coord_in_vox="[ 39, 13, 12 ]"
            ),
        "Peak-4-6": dict(
            peak_id="niiri:peak_0004_6",
            label="Peak 0004_6",
            p_uncorr="1.34887e-08",
            location="niiri:coordinate_0004_6",
            equiv_z="5.56",
            cluster_id="niiri:supra_threshold_cluster_0004"
            ),
        "FSL_Coordinate-4-6": dict(
            coordinate_id="niiri:coordinate_0004_6",
            label="Coordinate 0004_6",
            coord="[ 0.791, -87.2, 3.23 ]",
            coord_in_vox="[ 32, 10, 16 ]"
            ),
        "Peak-M3-1": dict(
            peak_id="niiri:peak_0003_1",
            label="Peak 0003_1",
            p_uncorr="1.01163e-08",
            location="niiri:coordinate_0003_1",
            equiv_z="5.61",
            cluster_id="niiri:supra_threshold_cluster_0003"
            ),
        "FSL_Coordinate-3-1": dict(
            coordinate_id="niiri:coordinate_0003_1",
            label="Coordinate 0003_1",
            coord="[ -38.3, 20.7, 13.2 ]",
            coord_in_vox="[ 41, 41, 25 ]"
            ),
        "Peak-3-2": dict(
            peak_id="niiri:peak_0003_2",
            label="Peak 0003_2",
            p_uncorr="1.52768e-07",
            location="niiri:coordinate_0003_2",
            equiv_z="5.12",
            cluster_id="niiri:supra_threshold_cluster_0003"
            ),
        "FSL_Coordinate-3-2": dict(
            coordinate_id="niiri:coordinate_0003_2",
            label="Coordinate 0003_2",
            coord="[ -45.5, 17.8, -6.65 ]",
            coord_in_vox="[ 43, 41, 20 ]"
            ),
        "Peak-3-3": dict(
            peak_id="niiri:peak_0003_3",
            label="Peak 0003_3",
            p_uncorr="1.82833e-06",
            location="niiri:coordinate_0003_3",
            equiv_z="4.63",
            cluster_id="niiri:supra_threshold_cluster_0003"
            ),
        "FSL_Coordinate-3-3": dict(
            coordinate_id="niiri:coordinate_0003_3",
            label="Coordinate 0003_3",
            coord="[ -63.4, 3.78, 0.366 ]",
            coord_in_vox="[ 48, 37, 21 ]"
            ),
        "Peak-3-4": dict(
            peak_id="niiri:peak_0003_4",
            label="Peak 0003_4",
            p_uncorr="9.77365e-06",
            location="niiri:coordinate_0003_4",
            equiv_z="4.27",
            cluster_id="niiri:supra_threshold_cluster_0003"
            ),
        "FSL_Coordinate-3-4": dict(
            coordinate_id="niiri:coordinate_0003_4",
            label="Coordinate 0003_4",
            coord="[ -57.4, 31.8, -2.12 ]",
            coord_in_vox="[ 46, 45, 22 ]"
            ),
        "Peak-3-5": dict(
            peak_id="niiri:peak_0003_5",
            label="Peak 0003_5",
            p_uncorr="1.22151e-05",
            location="niiri:coordinate_0003_5",
            equiv_z="4.22",
            cluster_id="niiri:supra_threshold_cluster_0003"
            ),
        "FSL_Coordinate-3-5": dict(
            coordinate_id="niiri:coordinate_0003_5",
            label="Coordinate 0003_5",
            coord="[ -34.0, 8.84, 28.3 ]",
            coord_in_vox="[ 40, 37, 28 ]"
            ),
        "Peak-3-6": dict(
            peak_id="niiri:peak_0003_6",
            label="Peak 0003_6",
            p_uncorr="1.89436e-05",
            location="niiri:coordinate_0003_6",
            equiv_z="4.12",
            cluster_id="niiri:supra_threshold_cluster_0003"
            ),
        "FSL_Coordinate-3-6": dict(
            coordinate_id="niiri:coordinate_0003_6",
            label="Coordinate 0003_6",
            coord="[ -53.3, 23.3, 12.2 ]",
            coord_in_vox="[ 45, 42, 25 ]"
            ),
        "Peak-M2-1": dict(
            peak_id="niiri:peak_0002_1",
            label="Peak 0002_1",
            p_uncorr="1.74205e-06",
            location="niiri:coordinate_0002_1",
            equiv_z="4.64",
            cluster_id="niiri:supra_threshold_cluster_0002"
            ),
        "FSL_Coordinate-2-1": dict(
            coordinate_id="niiri:coordinate_0002_1",
            label="Coordinate 0002_1",
            coord="[ -56.2, -61.9, 4.03 ]",
            coord_in_vox="[ 47, 18, 18 ]"
            ),
        "Peak-2-2": dict(
            peak_id="niiri:peak_0002_2",
            label="Peak 0002_2",
            p_uncorr="4.71165e-06",
            location="niiri:coordinate_0002_2",
            equiv_z="4.43",
            cluster_id="niiri:supra_threshold_cluster_0002"
            ),
        "FSL_Coordinate-2-2": dict(
            coordinate_id="niiri:coordinate_0002_2",
            label="Coordinate 0002_2",
            coord="[ -56.7, -53.1, 18.2 ]",
            coord_in_vox="[ 47, 20, 22 ]"
            ),
        "Peak-M1-1": dict(
            peak_id="niiri:peak_0001_1",
            label="Peak 0001_1",
            p_uncorr="2.01334e-06",
            location="niiri:coordinate_0001_1",
            equiv_z="4.61",
            cluster_id="niiri:supra_threshold_cluster_0001"
            ),
        "FSL_Coordinate-1-1": dict(
            coordinate_id="niiri:coordinate_0001_1",
            label="Coordinate 0001_1",
            coord="[ -8.35, 15.1, 39.6 ]",
            coord_in_vox="[ 33, 38, 31 ]"
            ),
        "Peak-1-2": dict(
            peak_id="niiri:peak_0001_2",
            label="Peak 0001_2",
            p_uncorr="0.000788846",
            location="niiri:coordinate_0001_2",
            equiv_z="3.16",
            cluster_id="niiri:supra_threshold_cluster_0001"
            ),
        "FSL_Coordinate-1-2": dict(
            coordinate_id="niiri:coordinate_0001_2",
            label="Coordinate 0001_2",
            coord="[ -9.14, 30.5, 23.7 ]",
            coord_in_vox="[ 33, 43, 28 ]"
            ),
        "Peak-1-3": dict(
            peak_id="niiri:peak_0001_3",
            label="Peak 0001_3",
            p_uncorr="0.00122277",
            location="niiri:coordinate_0001_3",
            equiv_z="3.03",
            cluster_id="niiri:supra_threshold_cluster_0001"
            ),
        "FSL_Coordinate-1-3": dict(
            coordinate_id="niiri:coordinate_0001_3",
            label="Coordinate 0001_3",
            coord="[ -19.6, 17.4, 34.7 ]",
            coord_in_vox="[ 36, 39, 30 ]"
            ),
        "Peak-1-4": dict(
            peak_id="niiri:peak_0001_4",
            label="Peak 0001_4",
            p_uncorr="0.00554262",
            location="niiri:coordinate_0001_4",
            equiv_z="2.54",
            cluster_id="niiri:supra_threshold_cluster_0001"
            ),
        "FSL_Coordinate-1-4": dict(
            coordinate_id="niiri:coordinate_0001_4",
            label="Coordinate 0001_4",
            coord="[ -9.64, 40.1, 17.3 ]",
            coord_in_vox="[ 33, 46, 27 ]"
            ),
        "FSL_SearchSpaceMaskMap": dict(
            search_space_id="niiri:search_space_mask_id",
            location="SearchSpaceMask.nii.gz",
            filename="SearchSpaceMask.nii.gz",
            label="Search Space Mask Map",
            user_defined="false",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            search_vol_voxels="45203",
            search_vol_units="1.93808e+06",
            search_vol_resels="3753.84",
            resel_size="12.0418",
            noise_roughness="0.384676",
            random_field_station="true",
            sha="cc1a96a6111e5107eb08487e38e6d7f8164b9d1d3f1fc10948bdbcfaea642\
fe9bfae278c7fc372b65cac7232ea58fd8fb5914014e7b9a5d6200592b12b2a728b",
            inference_id="niiri:inference_id_1",
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
        "GrandMeanMap": dict(
            grand_mean_map_id="niiri:grand_mean_map_id",
            label="Grand Mean Map",
            location="GrandMean.nii.gz",
            filename="GrandMean.nii.gz",
            format="image/nifti",
            masked_median="9597.36",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="7a2703cea740e27a5170fb19e4a09b5e815e4b7e477bc75958404d675aa40\
8f53f747892a2ef4472f933cf5f12cd21cea99d5f5e551938081636fb6d4049473e",
            model_pe_id="niiri:model_parameters_estimation_id"
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
            )
        }

    NIDM_FSL_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'fsl', "example001")
    ttl_file = os.path.join(NIDM_FSL_DIR, 'fsl_nidm.ttl')
    example = ExampleFromTemplate(nidm_classes, ttl_file, False)
    example.create_example()

if __name__ == '__main__':
    main()
