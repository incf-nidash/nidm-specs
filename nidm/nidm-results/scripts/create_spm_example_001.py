"""
Create SPM example 001 stored in nidm/nidm-results/spm/example001 by using the
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
from Constants import STATO_GLS_STR, STATO_GLS_LABEL, STATO_TSTATISTIC_STR, \
    STATO_TSTATISTIC_LABEL, OBO_P_VALUE_FWER_QNAME, OBO_STATISTIC_QNAME, \
    NIDM_P_VALUE_UNCORRECTED_QNAME


def main():
    nidm_classes = {
        "DesignMatrix_1stLevel": dict(
            design_matrix_id='niiri:design_matrix_id',
            label="Design Matrix",
            location="DesignMatrix.csv",
            format="text/csv",
            filename="DesignMatrix.csv",
            design_matrix_png_id="niiri:design_matrix_png_id",
            regressors='[\\\"Sn(1) active*bf(1)\\\", \\\"Sn(1) constant\\\"]',
            hrf_basis="spm:SPM_0000004",
            drift_model="niiri:drift_model_id"),
        "SPM_DriftModel": dict(
            id="niiri:drift_model_id",
            label="SPM's DCT Drift Model",
            cut_off="128"
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
            target=100
            ),
        "ErrorModel": dict(
            error_model_id="niiri:error_model_id",
            noise_distribution="obo:STATO_0000227",
            variance_homo="true",
            variance_spatial="nidm:NIDM_0000073",
            dependence="obo:STATO_0000357",
            dependence_spatial="nidm:NIDM_0000072"
            ),
        "ModelParametersEstimation": dict(
            model_pe_id="niiri:model_pe_id",
            label="Model parameters estimation",
            est_method=STATO_GLS_STR,
            est_method_comment=STATO_GLS_LABEL,
            design_matrix_id="niiri:design_matrix_id",
            data_matrix_id="niiri:data_id",
            error_model_id="niiri:error_model_id",
            software_id="niiri:software_id"
            ),
        "ParameterEstimateMap-1": dict(
            beta_map_id="niiri:beta_map_id_1",
            label="Beta Map 1",
            coordinate_space_id="niiri:coordinate_space_id_1",
            param_est_id="niiri:model_pe_id"),
        "DerivedMap-PE1": dict(
            derived_from_map_id="niiri:beta_map_id_1_der",
            derived_map_type="nidm:NIDM_0000061",
            filename="beta_0001.nii",
            format="image/nifti",
            sha="fab2573099693215bac756bc796fbc983524473dec5c1b2d66fb83694c174\
12731df7f574094cb6c4a77994af7be11ed9aa545090fbe8ec6565a5c3c3dae8f0f",
            map_id="niiri:beta_map_id_1"
            ),
        "ParameterEstimateMap-2": dict(
            beta_map_id="niiri:beta_map_id_2",
            label="Beta Map 2",
            coordinate_space_id="niiri:coordinate_space_id_1",
            param_est_id="niiri:model_pe_id"),
        "CoordinateSpace-1": dict(
            coordinate_space_id="niiri:coordinate_space_id_1",
            label="Coordinate space 1",
            voxel_to_world_mapping="[[-3, 0, 0, 78],[0, 3, 0, -112],[0, 0, 3, \
-70],[0, 0, 0, 1]]",
            voxel_units="[ \\\"mm\\\", \\\"mm\\\", \\\"mm\\\" ]",
            voxel_size="[ 3, 3, 3 ]",
            coord_system="nidm:NIDM_0000051",
            number_of_dim="3",
            dimensions="[ 53, 63, 52 ]"),
        "ResidualMeanSquaresMap": dict(
            residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
            label="Residual Mean Squares Map",
            location="ResidualMeanSquares.nii.gz",
            filename="ResidualMeanSquares.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="84cd0e608b8763307a1166b88761291e552838d85b58334a69a286060f648\
9a3b0929a940c3ccac883803455118787ea32e0bb5a6d236a5d6e9e8b6a9f918a6b",
            param_est_id="niiri:model_pe_id"),
        "DerivedMap-RMSMap": dict(
            derived_from_map_id="niiri:residual_mean_squares_map_id_der",
            derived_map_type="nidm:NIDM_0000066",
            filename="ResMS.nii",
            format="image/nifti",
            sha="1635e0ae420cac1b5989fbc753b95f504dd957ff2986367fc4cd13ff35c44\
b4ee60994a9cdcab93a7d247fc5a8decb7578fa4c553b0ac905af8c7041db9b4acd",
            map_id="niiri:residual_mean_squares_map_id"
            ),
        "MaskMap_Analysis": dict(  # The "analysis mask"
            mask_id="niiri:mask_id_1",
            label="Mask",
            location="Mask.nii.gz",
            user_defined="false",
            filename="Mask.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="932fd9f0d55e9822748f4a9b35a0a7f0fe442f3e061e2eda48c2617a2938d\
f50ea84deca8de0725641a0105b712a80a0c8931df9bdf3bef788b1041379d00875",
            generated_by_act_id="niiri:model_pe_id",
            used_by_act_id="niiri:contrast_estimation_id"),
        "DerivedMap-Mask2": dict(  # The "analysis mask" (derived)
            derived_from_map_id="niiri:mask_id_1_der",
            derived_map_type="nidm:NIDM_0000054",
            filename="mask.nii",
            format="image/nifti",
            sha="fbc254cab29db5532feccce554ec9d3c845197eca9013ec9f0efd5d8d56e3\
aa008ccee4038fb3651d30447fa0f316938b07c3ad961b623458dcd9b46968a8e11",
            map_id="niiri:mask_id_1"
            ),
        "ContrastWeights": dict(
            contrast_id="niiri:contrast_id",
            label="Contrast: passive listening > rest",
            value="[1, 0]",
            statistic_type=STATO_TSTATISTIC_STR,
            stat_type_comment=STATO_TSTATISTIC_LABEL,
            contrast_name="passive listening > rest"
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
        "ContrastEstUsedParamEst-Con1PE2": dict(
            contrast_estimation_id="niiri:contrast_estimation_id",
            param_est_map="niiri:beta_map_id_2"
            ),
        "ContrastMap": dict(
            contrast_map_id="niiri:contrast_map_id",
            label="Contrast Map: passive listening > rest",
            location="Contrast.nii.gz",
            format="image/nifti",
            filename="Contrast.nii.gz",
            contrast_name="passive listening > rest",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="f0720b732aaf19c2ec42d0469f8308beb3aa978baf65c7dce6476a0d8e5b2\
f38c4fa9609f045a536678440feebce9a047e3bd6d59fdb8fb64baae058690bbda2",
            contrast_est_id="niiri:contrast_estimation_id"),
        "ContrastStandardErrorMap": dict(
            contrast_standard_error_map_id="niiri:contrast_standard_error_map_\
id",
            label="Contrast Standard Error Map",
            location="ContrastStandardError.nii.gz",
            format="image/nifti",
            filename="ContrastStandardError.nii.gz",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="f4e3616579fe8b0812469409b1501e391bb17ca6e364f37d622b37fa9014c\
f1dd89befece07e73cf5bca5b3116f55ac4496751ca990db85e8377001a4be941b2",
            contrast_est_id="niiri:contrast_estimation_id"),
        "StatisticMap_T": dict(
            statistic_map_id="niiri:statistic_map_id",
            label="Statistic Map: passive listening > rest",
            location="TStatistic.nii.gz",
            format="image/nifti",
            filename="TStatistic.nii.gz",
            statistic_type=STATO_TSTATISTIC_STR,
            stat_type_comment=STATO_TSTATISTIC_LABEL,
            contrast_name="passive listening > rest",
            error_dof="84.0",
            effect_dof="1",
            sha="799e9bbf8c15b35c0098bca468846bf2cd895a3366382b5ceaa953f1e9e57\
6955341a7c86e13e6fe9359da4ff1496a609f55ce9ecff8da2e461365372f2506d6",
            coordinate_space_id="niiri:coordinate_space_id_1",
            contrast_est_id="niiri:contrast_estimation_id"),
        "DerivedMap-StatMap": dict(
            derived_from_map_id="niiri:statistic_map_id_der",
            derived_map_type="nidm:NIDM_0000076",
            filename="spmT_0001.nii",
            format="image/nifti",
            sha="55951f31f0ede7e88eca5cd4793df3f630aba21bc90fb81e3695db060c7d\
4c0b0ccf0b51fd8958c32ea3253d3122e9b31a54262bf910f8b5b646054ceb9a5825",
            map_id="niiri:statistic_map_id"
            ),
        "HeightThreshold_equivThresh_equivThresh2": dict(
            height_threshold_id="niiri:height_threshold_id",
            thresh_type=OBO_P_VALUE_FWER_QNAME,
            label="Height Threshold: p<0.05 (FWE)",
            value="0.0499999999999976",
            equiv_thresh="niiri:height_threshold_id_2",
            equiv_thresh2="niiri:height_threshold_id_3"
            ),
        "HeightThreshold-2": dict(
            height_threshold_id="niiri:height_threshold_id_2",
            thresh_type=OBO_STATISTIC_QNAME,
            label="Height Threshold",
            value="4.85241745689539"
            ),
        "HeightThreshold-3": dict(
            height_threshold_id="niiri:height_threshold_id_3",
            thresh_type=NIDM_P_VALUE_UNCORRECTED_QNAME,
            label="Height Threshold",
            value="2.7772578456986e-06",
            ),
        "ExtentThresholdStat_equivThresh_equivThresh2_clusterSizeResels": dict(
            extent_threshold_id="niiri:extent_threshold_id",
            label="Extent Threshold: k>=0",
            cluster_size_vox="0",
            cluster_size_resels="0",
            equiv_thresh="niiri:extent_threshold_id_2",
            equiv_thresh2="niiri:extent_threshold_id_3"
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
        "PeakDefinitionCriteria_MaxPeaks": dict(
            peak_definition_criteria_id="niiri:peak_definition_criteria_id",
            label="Peak Definition Criteria",
            max_num_peaks="3",
            min_dist_peaks="8.0"
            ),
        "ClusterDefinitionCriteria": dict(
            cluster_definition_criteria_id="niiri:cluster_definition_criteria\
_id",
            label="Cluster Connectivity Criterion: 18",
            connectivity="nidm:NIDM_0000128"
            ),
        "Inference": dict(
            inference_id="niiri:inference_id",
            label="Inference",
            alternative_hyp="nidm:NIDM_0000060",
            stat_map_id="niiri:statistic_map_id",
            height_thresh_id="niiri:height_threshold_id",
            extent_thresh_id="niiri:extent_threshold_id",
            Inference_mask_id="niiri:sub_volume_id",
            peak_def_id="niiri:peak_definition_criteria_id",
            cluster_def_id="niiri:cluster_definition_criteria_id",
            mask_id="niiri:mask_id_1",
            software_id="niiri:software_id"
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
            ),
        "Peak_ValueP-5": dict(
            peak_id="niiri:peak_0005",
            label="Peak: 0005",
            location="niiri:coordinate_0005",
            value="12.4728717803955",
            equiv_z="INF",
            p_uncorr="4.44089209850063e-16",
            p_value_fwe="0",
            p_value_fdr="1.19156591713838e-11",
            cluster_id="niiri:supra_threshold_cluster_0002"
            ),
        "Coordinate-5": dict(
            coordinate_id="niiri:coordinate_0005",
            label="Coordinate: 0005",
            coord="[ 60, -22, 11 ]"
            ),
        "Peak_ValueP-6": dict(
            peak_id="niiri:peak_0006",
            label="Peak: 0006",
            location="niiri:coordinate_0006",
            value="9.72103404998779",
            equiv_z="INF",
            p_uncorr="1.22124532708767e-15",
            p_value_fwe="6.9250605250204e-11",
            p_value_fdr="6.52169693024352e-09",
            cluster_id="niiri:supra_threshold_cluster_0002"
            ),
        "Coordinate-6": dict(
            coordinate_id="niiri:coordinate_0006",
            label="Coordinate: 0006",
            coord="[ 57, -40, 5 ]"
            ),
        "Peak_ValueP-7": dict(
            peak_id="niiri:peak_0007",
            label="Peak: 0007",
            location="niiri:coordinate_0007",
            value="6.55745935440063",
            equiv_z="5.87574033699266",
            p_uncorr="2.10478867668229e-09",
            p_value_fwe="9.17574302586877e-05",
            p_value_fdr="0.00257605396646668",
            cluster_id="niiri:supra_threshold_cluster_0003"
            ),
        "Coordinate-7": dict(
            coordinate_id="niiri:coordinate_0007",
            label="Coordinate: 0007",
            coord="[ 36, -28, -13 ]"
            ),
        "Peak_ValueP-8": dict(
            peak_id="niiri:peak_0008",
            label="Peak: 0008",
            location="niiri:coordinate_0008",
            value="6.19558477401733",
            equiv_z="5.60645028016544",
            p_uncorr="1.0325913235576e-08",
            p_value_fwe="0.000382453907303626",
            p_value_fdr="0.00949154522981781",
            cluster_id="niiri:supra_threshold_cluster_0004"
            ),
        "Coordinate-8": dict(
            coordinate_id="niiri:coordinate_0008",
            label="Coordinate: 0008",
            coord="[ -33, -31, -16 ]"
            ),
        "Peak_ValueP-9": dict(
            peak_id="niiri:peak_0009",
            label="Peak: 0009",
            location="niiri:coordinate_0009",
            value="5.27320194244385",
            equiv_z="4.88682085490477",
            p_uncorr="5.12386299833523e-07",
            p_value_fwe="0.0119099090973821",
            p_value_fdr="0.251554254717758",
            cluster_id="niiri:supra_threshold_cluster_0005"
            ),
        "Coordinate-9": dict(
            coordinate_id="niiri:coordinate_0009",
            label="Coordinate: 0009",
            coord="[ 45, -40, 32 ]"
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
        "DerivedMap": dict(
            derived_from_map_id="niiri:contrast_map_id_der",
            derived_map_type="nidm:NIDM_0000002",
            filename="con_0001.nii",
            format="image/nifti",
            sha="277dd1da13d391c33c172fb8c71060008cc66e173de6362eb857b0055b41e\
9bae57911f7ec4b45659905103b1139ebf3da0c2d04cf105bbce0cdc3004b643c22",
            map_id="niiri:contrast_map_id"
            ),
        "DerivedMap-2": dict(
            derived_from_map_id="niiri:beta_map_id_2_der",
            derived_map_type="nidm:NIDM_0000061",
            filename="beta_0002.nii",
            format="image/nifti",
            sha="3f72b788762d9ab2c7ddb5e4d446872694ee42fc8897fe5317b54efb7924f\
784da6499065db897a49595d8763d1893ad65ad102b0c88f2e72e2d028173343008",
            map_id="niiri:beta_map_id_2"
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
            sha="2025dc6c33708b80708c2eba3215fb1149df236fb558a8e8f8f6cf34595fb\
54734fe5e436db3e192a424d99699dd7feb2f4a9020ceae8e7bcbd881b17825256a",
            model_pe_id="niiri:model_pe_id"
            ),
        "SPM_InferenceUsedRPVMap": dict(
            inference_id="niiri:inference_id",
            resels_per_voxel_map_id="niiri:resels_per_voxel_map_id"
        ),
        "DerivedMap-RPVMap": dict(
            derived_from_map_id="niiri:resels_per_voxel_map_id_der",
            derived_map_type="nidm:NIDM_0000144",
            filename="RPV.nii",
            format="image/nifti",
            sha="963283cdde607c40e4640c27453867bd0d70133b6d61482933862487c0f4a\
5acdb2e338a12a2605ee044b1aa47b5717f0c520b90ed3c49b5227f0483bd48512d",
            map_id="niiri:resels_per_voxel_map_id"
            ),
        "ClusterLabelsMap": dict(
            cluster_label_map_id="niiri:cluster_label_map_id",
            location="ClusterLabels.nii.gz",
            filename="ClusterLabels.nii.gz",
            format="image/nifti"
            ),
        "SPM_Software": dict(
            software_id="niiri:software_id",
            software_type="nlx:nif-0000-00343",
            label="SPM",
            version="12.12.1"
            ),
        "Image": dict(
            image_id="niiri:maximum_intensity_projection_id",
            location="MaximumIntensityProjection.png",
            filename="MaximumIntensityProjection.png",
            format="image/png"
            ),
        "GrandMeanMap": dict(
            grand_mean_map_id="niiri:grand_mean_map_id",
            label="Grand Mean Map",
            location="GrandMean.nii.gz",
            filename="GrandMean.nii.gz",
            format="image/nifti",
            masked_median="132.008995056152",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="4d3528031bce4a9c1b994b8124e6e0eddb9df90b49c84787652ed94df8c14\
c04ec92100a2d8ea86a8df24ba44617aca7457ddcb2f42253fc17e33296a1aea1cb",
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
            )
        }

    NIDM_SPM_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'spm', "example001")
    ttl_file = os.path.join(NIDM_SPM_DIR, 'example001_spm_results.ttl')
    example = ExampleFromTemplate(nidm_classes, ttl_file, False)
    example.create_example()

if __name__ == '__main__':
    main()
