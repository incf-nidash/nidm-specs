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
    STATO_TSTATISTIC_LABEL, OBO_P_VALUE_FWER_QNAME, OBO_Q_VALUE_FDR_QNAME, \
    NIDM_P_VALUE_UNCORRECTED_QNAME, OBO_STATISTIC_QNAME, \
    NIDM_FINITE_IMPULSE_RESPONSE_HRB, SPM_CANONICAL_HRF, \
    SPM_TEMPORAL_DERIVATIVE, SPM_DISPERSION_DERIVATIVE, \
    NIDM_SPATIALLY_LOCAL_MODEL, NIDM_SPATIALLY_GLOBAL_MODEL, \
    STATO_UNSTRUCTURED_COVARIANCE


def main():
    nidm_classes = {
        "NIDMBundle": dict(
            comment="NIDM-Results Bundle",
            bundle_id="niiri:nidm_results_id",
            label="NIDM-Results",
            object_model="nidm:NIDM_0000027",
            version="1.1.0",
            time="2014-05-19T10:30:00.000+01:00",
            export_id="niiri:export_id"
            ),
        "SPM_Software": dict(
            software_id="niiri:spm_software_id",
            software_type="nlx:nif-0000-00343",
            label="SPM",
            version="8.6225"
            ),
        "FSL_Software": dict(
            software_id="niiri:software_id",
            software_type="nlx:birnlex_2067",
            label="FSL",
            version="5.0.1",
            feat_version="6.00"
            ),
        "ExporterSoftware-FSL": dict(
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
        "ExporterSoftware-SPM": dict(
            software_id="niiri:exporter_id",
            software_type="nidm:NIDM_0000168",
            label="spm_results_nidm",
            version="12b.5858"
            ),
        "DesignMatrix": dict(
            comment="Design Matrix: Group Level",
            design_matrix_id='niiri:design_matrix_id',
            label="Design Matrix",
            location="DesignMatrix.csv",
            format="text/csv",
            filename="DesignMatrix.csv",
            design_matrix_png_id="niiri:design_matrix_png_id"),
        "DesignMatrix_1stLevel": dict(
            comment="Design Matrix: Subject Level",
            design_matrix_id='niiri:first_level_design_matrix_id',
            label="First-Level Design Matrix",
            location="DesignMatrix.csv",
            format="text/csv",
            filename="DesignMatrix.csv",
            design_matrix_png_id="niiri:design_matrix_png_id",
            hrf_basis="niiri:hrf_basis_id",
            drift_model="niiri:drift_model_id",
            regressors="[\\\"Sn(1) active*bf(1)\\\",\\\"Sn(1) constant\\\"]"),
        "DesignMatrix_1stLevel-FIR": dict(
            comment="HRF: FIR Basis Set",
            design_matrix_id='niiri:first_level_design_matrix_id',
            label="First-Level Design Matrix",
            location="DesignMatrix.csv",
            format="text/csv",
            filename="DesignMatrix.csv",
            design_matrix_png_id="niiri:design_matrix_png_id",
            hrf_basis=NIDM_FINITE_IMPULSE_RESPONSE_HRB,
            drift_model="niiri:drift_model_id",
            regressors="[\\\"Sn(1) active*bf(1)\\\",\\\"Sn(1) constant\\\"]"),
        "DesignMatrix_1stLevel_HRFBasis2_HRFBasis3-InformedBasisSet": dict(
            comment="HRF: SPM's Informed Basis Set",
            design_matrix_id='niiri:first_level_design_matrix_id',
            label="First-Level Design Matrix",
            location="DesignMatrix.csv",
            format="text/csv",
            filename="DesignMatrix.csv",
            design_matrix_png_id="niiri:design_matrix_png_id",
            hrf_basis=SPM_CANONICAL_HRF,
            hrf_basis_2=SPM_TEMPORAL_DERIVATIVE,
            hrf_basis_3=SPM_DISPERSION_DERIVATIVE,
            drift_model="niiri:drift_model_id",
            regressors="[\\\"Sn(1) active*bf(1)\\\",\\\"Sn(1) constant\\\"]"),
        "Map_atLocation-nii": dict(
            comment="Map: One-file Nifti (.nii)",
            map_type="nidm:NIDM_0000052",
            map_id="niiri:map_id",
            filename='image.nii',
            coordinate_space_id="niiri:coordinate_space_id",
            sha="e43b6e01b0463fe7d40782137867ae43b6e01b0463fe7d40782137867a",
            location="image.nii"),
        "Map_atLocation_hasMapHeader-img": dict(
            comment="Map: Nifti (.img)",
            map_type="nidm:NIDM_0000052",
            map_id="niiri:map_id",
            filename='image.img',
            coordinate_space_id="niiri:coordinate_space_id",
            sha="e43b6e01b0463fe7d40782137867ae43b6e01b0463fe7d40782137867a",
            map_header="niiri:map_header_id",
            location="image.img"),
        "MapHeader": dict(
            comment="Map Header: Nifti header (.hdr)",
            map_header_id="niiri:map_header_id",
            filename='image.hdr',
            sha="e43b6e01b0463fe7d40782137867ae43b6e01b0463fe7d40782137867a",
            location="image.hdr"),
        "Image-DesignMatrix": dict(
            comment="Image: Design Matrix",
            image_id="niiri:design_matrix_png_id",
            location="DesignMatrix.png",
            filename="DesignMatrix.png",
            format="image/png"
            ),
        "Data": dict(
            comment="Data",
            data_id='niiri:data_id',
            label="Data",
            scaling="true",
            target=100
            ),
        "ErrorModel": dict(
            comment="Error Model",
            error_model_id="niiri:error_model_id",
            noise_distribution="obo:STATO_0000227",
            variance_homo="true",
            variance_spatial="nidm:NIDM_0000073",
            dependence="nidm:NIDM_0000048",
            dependence_spatial="nidm:NIDM_0000073"
            ),
        "ErrorModel-SPMnonSphericity": dict(
            comment="Error Model: SPM non sphericity",
            error_model_id="niiri:error_model_id",
            noise_distribution="obo:STATO_0000227",
            variance_homo="false",
            variance_spatial=NIDM_SPATIALLY_LOCAL_MODEL,
            dependence=STATO_UNSTRUCTURED_COVARIANCE,
            dependence_spatial=NIDM_SPATIALLY_GLOBAL_MODEL
            ),
        "ModelParametersEstimation": dict(
            comment="Model Parameters Estimation",
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
            comment="Parameter Estimate Map",
            beta_map_id="niiri:beta_map_id_1",
            label="Beta Map 1",
            location="ParameterEstimate_0001.nii.gz",
            filename="ParameterEstimate_0001.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            param_est_id="niiri:model_pe_id"),
        "ResidualMeanSquaresMap": dict(
            comment="Residual Mean Squares Map",
            residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
            label="Residual Mean Squares Map",
            location="ResidualMeanSquares.nii.gz",
            filename="ResidualMeanSquares.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            param_est_id="niiri:model_pe_id"),
        "MaskMap": dict(
            comment="Mask Map",
            mask_id="niiri:mask_id_2",
            user_defined="false",
            label="Mask",
            location="Mask.nii.gz",
            filename="Mask.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            used_by_act_id="niiri:model_pe_id"),
        "ContrastWeights": dict(
            comment="Contrast Weights",
            contrast_id="niiri:contrast_id",
            label="Contrast: Listening > Rest",
            value="[ 1, 0, 0 ]",
            statistic_type=STATO_TSTATISTIC_STR,
            stat_type_comment=STATO_TSTATISTIC_LABEL,
            contrast_name="listening > rest"),
        "ContrastEstimation": dict(
            comment="Contrast Estimation",
            contrast_estimation_id="niiri:contrast_estimation_id",
            label="Contrast estimation",
            software_id="niiri:software_id",
            mask_id="niiri:mask_id_2",
            residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
            design_matrix_id="niiri:design_matrix_id",
            contrast_id="niiri:contrast_id",
            param_est_map="niiri:beta_map_id_1"),
        "ContrastMap": dict(
            comment="Contrast Map",
            contrast_map_id="niiri:contrast_map_id",
            label="Contrast Map: listening > rest",
            location="Contrast.nii.gz",
            format="image/nifti",
            filename="Contrast.nii.gz",
            contrast_name="listening > rest",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            contrast_est_id="niiri:contrast_estimation_id"),
        "ContrastStandardErrorMap": dict(
            comment="Contrast Standard Error Map",
            contrast_standard_error_map_id="niiri:contrast_standard_error_map_\
id",
            label="Contrast Standard Error Map",
            location="ContrastStandardError.nii.gz",
            format="image/nifti",
            filename="ContrastStandardError.nii.gz",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            contrast_est_id="niiri:contrast_estimation_id"),
        "StatisticMap_T": dict(
            comment="Statistic Map: T",
            statistic_map_id="niiri:statistic_map_id",
            label="Statistic Map: listening > rest",
            location="TStatistic.nii.gz",
            format="image/nifti",
            filename="TStatistic.nii.gz",
            statistic_type=STATO_TSTATISTIC_STR,
            stat_type_comment=STATO_TSTATISTIC_LABEL,
            contrast_name="listening > rest",
            error_dof="72.9999999990787",
            effect_dof="1",
            sha="e43b6e01b0463fe7d40782137867a",
            coordinate_space_id="niiri:coordinate_space_id_1",
            contrast_est_id="niiri:contrast_estimation_id"),
        "HeightThreshold_equivThresh-FWER": dict(
            comment="Height Threshold: p<0.05 FWER",
            height_threshold_id="niiri:height_threshold_fwer_id",
            label="Height Threshold: p<0.05 (FWER-corrected)",
            value="0.05",
            thresh_type=OBO_P_VALUE_FWER_QNAME,
            equiv_thresh="niiri:height_threshold_stat_id"
            ),
        "HeightThreshold-Stat": dict(
            comment="Height Threshold: Z<0.0000000672357409",
            height_threshold_id="niiri:height_threshold_stat_id",
            label="Height Threshold: Z<0.0000000672357409",
            value="0.0000000672357409",
            thresh_type=OBO_STATISTIC_QNAME,
            ),
        "HeightThreshold-FDR": dict(
            comment="Height Threshold: p<0.05 FDR",
            height_threshold_id="niiri:height_threshold_fdr_id",
            label="Height Threshold: p<0.05 (FDR-corrected)",
            value="0.05",
            thresh_type=OBO_Q_VALUE_FDR_QNAME
            ),
        "HeightThreshold-Unc": dict(
            comment="Height Threshold: p<0.001 uncorrected",
            height_threshold_id="niiri:height_threshold_unc_id",
            label="Height Threshold: p<0.001 (uncorrected)",
            value="0.001",
            thresh_type=NIDM_P_VALUE_UNCORRECTED_QNAME
            ),
        "ExtentThresholdStat_clusterSizeResels": dict(
            comment="Extent Threshold: k>=0",
            extent_threshold_id="niiri:extent_threshold_stat_id",
            label="Extent Threshold: k>=0",
            cluster_size_vox="0",
            cluster_size_resels="0",
            ),
        "ExtentThreshold_equivThresh-FWER": dict(
            comment="Extent Threshold: p<0.05 FWER",
            extent_threshold_id="niiri:extent_threshold_fwer_id",
            thresh_type=OBO_P_VALUE_FWER_QNAME,
            label="Extent Threshold: p<0.05 (FWER-corrected)",
            value="0.05",
            equiv_thresh="niiri:extent_threshold_stat_id"
            ),
        "ExtentThreshold-FDR": dict(
            comment="Extent Threshold: p<0.05 FDR",
            extent_threshold_id="niiri:extent_threshold_fdr_id",
            thresh_type=OBO_Q_VALUE_FDR_QNAME,
            label="Extent Threshold: p<0.05 (FDR-corrected)",
            value="0.05"
            ),
        "ExtentThreshold-Unc": dict(
            comment="Extent Threshold: p<0.001 uncorrected",
            extent_threshold_id="niiri:extent_threshold_unc_id",
            thresh_type=NIDM_P_VALUE_UNCORRECTED_QNAME,
            label="Extent Threshold: p<0.001 (uncorrected)",
            value="0.001"
            ),
        "SPM_ReselsPerVoxelMap": dict(
            comment="Resels per Voxel Map",
            resels_per_voxel_map_id="niiri:resels_per_voxel_map_id",
            label="Resels per Voxel Map",
            location="ReselsPerVoxel.nii.gz",
            filename="ReselsPerVoxel.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            model_pe_id="niiri:model_pe_id"
            ),
        "ClusterLabelsMap": dict(
            comment="Cluster Labels Map",
            cluster_label_map_id="niiri:cluster_label_map_id",
            location="ClusterLabels.nii.gz",
            filename="ClusterLabels.nii.gz",
            format="image/nifti"
            ),
        "DisplayMaskMap": dict(
            comment="Display Mask Map",
            display_map_id="niiri:display_map_id",
            label="Display Mask Map",
            location="DisplayMask.nii.gz",
            filename="DisplayMask.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_2",
            sha="e43b6e01b0463fe7d40782137867a"
            ),
        "PeakDefinitionCriteria_MaxPeaks": dict(
            comment="Peak Definition Criteria",
            peak_definition_criteria_id="niiri:peak_definition_criteria_id",
            label="Peak Definition Criteria",
            max_num_peaks="3",
            min_dist_peaks="8.0"
            ),
        "ClusterDefinitionCriteria": dict(
            comment="Cluster Definition Criteria",
            cluster_definition_criteria_id="niiri:cluster_definition_criteria_\
id",
            label="Cluster Connectivity Criterion: 18",
            connectivity="nidm:NIDM_0000128"
            ),
        "Inference": dict(
            comment="Inference",
            inference_id="niiri:inference_id",
            label="Inference",
            alternative_hyp="nidm:NIDM_0000060",
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
        "ConjunctionInference": dict(
            comment="Conjunction Inference",
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
        "SPM_KConjunctionInference": dict(
            comment="SPM's Partial Conjunction Inference",
            conj_inference_id="niiri:conjunction_id_2",
            label="SPM's Partial Conjunction Inference",
            alternative_hyp="nidm:NIDM_0000060",
            stat_map_id_1="niiri:statistic_map_id_1",
            stat_map_id_2="niiri:statistic_map_id_2",
            global_null_degree="1",
            height_thresh_id="niiri:height_threshold_id",
            extent_thresh_id="niiri:extent_threshold_id",
            display_mask_id="niiri:display_map_id",
            peak_def_id="niiri:peak_definition_criteria_id",
            cluster_def_id="niiri:cluster_definition_criteria_id",
            mask_id="niiri:mask_id_1",
            software_id="niiri:software_id"
            ),
        "ExcursionSetMap": dict(
            comment="Excursion Set Map",
            id="niiri:excursion_set_map_id",
            label="Excursion Set Map",
            location="ExcursionSet.nii.gz",
            format="image/nifti",
            filename="ExcursionSet.nii.gz",
            cluster_label_map_id="niiri:cluster_label_map_id",
            max_intensity_projection_id="niiri:maximum_intensity_projection_\
id",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a",
            num_of_clusters="8",
            p_value="8.95949980872501e-14",
            inference_id="niiri:inference_id"
            ),
        "SupraThresholdCluster": dict(
            comment="Supra-Threshold Cluster",
            cluster_id="niiri:supra_threshold_cluster_0001",
            label="Supra-Threshold Cluster 0001",
            cluster_size_in_voxels="530",
            cluster_label_id="1",
            cluster_size_in_resels="23.1209189500945",
            p_value_unc="9.56276736481136e-52",
            p_value_fwe="0",
            p_value_fdr="7.65021389184909e-51",
            excursion_set_id="niiri:excursion_set_map_id"
            ),
        "Peak_ValueP": dict(
            comment="Peak",
            peak_id="niiri:peak_0001",
            label="Peak 0001",
            location="niiri:coordinate_0001",
            value="13.9346199035645",
            equiv_z="INF",
            p_uncorr="4.44089209850063e-16",
            p_value_fwe="0",
            p_value_fdr="6.3705194444993e-11",
            cluster_id="niiri:supra_threshold_cluster_0001"
            ),
        "Coordinate": dict(
            comment="Coordinate",
            coordinate_id="niiri:coordinate_0001",
            label="Coordinate: 0001",
            coord="[ -60, -28, 13 ]"
            ),
        "SearchSpaceMaskMap": dict(
            comment="Search Space Mask Map",
            search_space_id="niiri:search_space_mask_id",
            location="SearchSpaceMask.nii.gz",
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
            search_vol_resels_geom="[3, 72.3216126440484, 850.716735116472, \
2552.68032521656]",
            noise_fwhm_in_voxels="[ 2.95881189165801, 2.96628446669584, \
2.61180425626264 ]",
            noise_fwhm_in_units="[ 8.87643567497404, 8.89885340008753, \
7.83541276878791 ]",
            random_field_station="false",
            sha="e43b6e01b0463fe7d40782137867a",
            inference_id="niiri:inference_id"
            ),
        "FSL_ClusterCenterOfGravity": dict(
            comment="Cluster Center Of Gravity",
            center_of_gravity_id="niiri:center_of_gravity_1",
            location="niiri:coordinate_0001",
            label="Center of gravity",
            cluster_id="niiri:supra_threshold_cluster_0001",
            ),
        "CoordinateSpace": dict(
            comment="Coordinate Space",
            coordinate_space_id="niiri:coordinate_space_id_1",
            label="Coordinate space 1",
            voxel_to_world_mapping="[[-3, 0, 0, 78],[0, 3, 0, -112],\
[0, 0, 3, -50],[0, 0, 0, 1]]",
            voxel_units="[ \\\"mm\\\", \\\"mm\\\", \\\"mm\\\" ]",
            voxel_size="[ 3, 3, 3 ]",
            coord_system="nidm:NIDM_0000051",
            number_of_dim="3",
            dimensions="[ 53, 63, 46 ]"),
        "Image": dict(
            comment="Image",
            image_id="niiri:maximum_intensity_projection_id",
            location="MaximumIntensityProjection.png",
            filename="MaximumIntensityProjection.png",
            format="image/png"
            ),
        "GrandMeanMap": dict(
            comment="Grand Mean Map",
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
        "SPM_DriftModel": dict(
            comment="SPM's DCT Drift Model",
            id="niiri:drift_model_id",
            label="SPM's DCT Drift Model",
            cut_off="128"
            ),
        "FSL_DriftModel": dict(
            comment="FSL's Gaussian Running Line Drift Model",
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
