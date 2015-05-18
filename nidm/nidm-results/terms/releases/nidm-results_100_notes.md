#### Updated namespaces
- nidm namespace (http://www.incf.org/ns/nidash/nidm#) replaced by http://purl.org/nidash/nidm# [PR 237](https://github.com/incf-nidash/nidm/pull/237)
- spm namespace (http://www.incf.org/ns/nidash/spm#) replaced by http://purl.org/nidash/spm# [PR 237](https://github.com/incf-nidash/nidm/pull/237)
- fsl namespace (http://www.incf.org/ns/nidash/fsl#) replaced by http://purl.org/nidash/fsl# [PR 237](https://github.com/incf-nidash/nidm/pull/237)


#### Updated terms

### Alphanumeric identifiers:
- Semantic identifiers replaced by alphanumeric identifiers. For example, nidm:ContrastMap replaced by [nidm:'Contrast Map'](http://www.incf.org/ns/nidash/nidm#NIDM_0000002) (cf. https://github.com/incf-nidash/nidm/blob/master/scripts/Constants.py for a complete list).

### Re-use of Dublin Core and NFO terms ([PR 247](https://github.com/incf-nidash/nidm/pull/247))
- nidm:Image replaced by [dctype:Image](http://purl.org/dc/dcmitype/Image)
- nidm:visualisation replaced by [dct:description](http://purl.org/dc/dcmitype/description)
- nidm:filename replaced by [nfo:filename](http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#)

### Re-use STATO estimation methods ([PR 252](https://github.com/incf-nidash/nidm/pull/252)):
- nidm:EstimationMethod replaced by [obo:'model parameter estimation'](http://purl.obolibrary.org/obo/STATO_0000119)
- nidm:GeneralizedLeastSquares replaced by [obo:'generalized least squares estimation'](http://purl.obolibrary.org/obo/STATO_0000372)
- nidm:OrdinaryLeastSquares replaced by [obo:'ordinary least squares estimation'](http://purl.obolibrary.org/obo/STATO_0000370)
- nidm:RobustIterativelyReweighedLeastSquares replaced by [obo:'iteratively reweighted least squares estimation'](http://purl.obolibrary.org/obo/STATO_0000373)
- nidm:WeightedLeastSquares replaced by [obo:'weighted least squares estimation'](http://purl.obolibrary.org/obo/STATO_0000371)

### Re-use Neurolex/RRID SPM and FSL terms ([PR 263](https://github.com/incf-nidash/nidm/pull/263)):
- nidm:SPM replaced by [nlx:SPM](http://neurolex.org/wiki/Category:Resource:SPM)
- nidm:FSL replaced by [nlx:FSL](http://neurolex.org/wiki/Category:Resource:FSL)

### Re-use STATO statistic ([PR 262](https://github.com/incf-nidash/nidm/pull/262)):
- nidm:Statistic replaced by [obo:'statistic'](http://purl.obolibrary.org/obo/STATO_0000039)
- nidm:FStatistic replaced by [obo:'F-statistic'](http://purl.obolibrary.org/obo/STATO_0000282)
- nidm:TStatistic replaced by [obo:'t-statistic'](http://purl.obolibrary.org/obo/STATO_0000176)
- nidm:ZStatistic replaced by [obo:'Z-statistic'](http://purl.obolibrary.org/obo/STATO_0000376)

### Re-use error covariance structures from STATO ([PR 306](https://github.com/incf-nidash/nidm/pull/306)):
- nidm:ErrorDependence replaced by [obo:'covariance structure'](http://purl.obolibrary.org/obo/STATO_0000346)
- nidm:CompoundSymmetricNoise replaced by [obo:'compound symmetry covariance structure'](http://www.incf.org/ns/nidash/nidm#NIDM_0000022)
- nidm:SeriallyCorrelatedError replaced by [obo:'Toeplitz covariance structure'](http://purl.obolibrary.org/obo/STATO_0000357)

### Re-use "contrast weight matrix" from STATO ([PR 305](https://github.com/incf-nidash/nidm/pull/305)):
- nidm:ContrastWeights replaced by [obo:'contrast weight matrix'](http://purl.obolibrary.org/obo/STATO_0000323)

### Noise spatial model terms ([PR 194](https://github.com/incf-nidash/nidm/pull/194)):
- nidm:ErrorParameterSpatialDependence replaced by [nidm:'Error Parameter Map-Wise Dependence'](http://www.incf.org/ns/nidash/nidm#NIDM_0000071)
- nidm:varianceSpatialModel: replaced by [nidm:'variance Map-Wise Dependence'](http://www.incf.org/ns/nidash/nidm#NIDM_0000126)
- nidm:dependenceSpatialModel replaced by [nidm:'dependence Map-Wise Dependence'](http://www.incf.org/ns/nidash/nidm#NIDM_0000089)
- nidm:SpatiallyGlobalModel replaced by [nidm:'Constant Parameter'](http://www.incf.org/ns/nidash/nidm#NIDM_0000072)
- nidm:SpatiallyLocalModel replaced by [nidm:'Independent Parameter'](http://www.incf.org/ns/nidash/nidm#NIDM_0000073)
- nidm:SpatiallyRegularizedModel replaced by [nidm:'Regularized Parameter'](http://www.incf.org/ns/nidash/nidm#NIDM_0000074)

### Mask terms ([PR 258](https://github.com/incf-nidash/nidm/pull/258)):
- nidm:CustomMask replaced by nidm:MaskMap with attribute nidm:isUserDefined = true.
- nidm:SearchSpaceMask replaced by nidm:SearchSpaceMaskMap
- nidm:DisplayMask replaced by nidm:DisplayMaskMap

### Change in namespace:
- spm:searchVolumeInVoxels and fsl:searchVolumeInVoxels replaced by nidm:searchVolumeInVoxels ([PR 269](https://github.com/incf-nidash/nidm/pull/269)).
- spm:searchVolumeInUnits replaced by [nidm:'search Volume In Units'](http://www.incf.org/ns/nidash/nidm#NIDM_0000136) ([PR 300](https://github.com/incf-nidash/nidm/pull/300)).
- spm:searchVolumeInVertices replaced by [nidm:'search Volume In Vertices'](http://www.incf.org/ns/nidash/nidm#NIDM_0000137) ([PR 300](https://github.com/incf-nidash/nidm/pull/300)).
- spm:hasMaximumIntensityProjection replaced by [nidm:'has Maximum Intensity Projection'](http://www.incf.org/ns/nidash/nidm#NIDM_0000138) ([PR 293](https://github.com/incf-nidash/nidm/pull/293)).
- fsl:coordinateInVoxels replaced by [nidm:'coordinate In Voxels'](http://www.incf.org/ns/nidash/nidm#NIDM_0000139)  ([PR 301](https://github.com/incf-nidash/nidm/pull/301)).
- fsl:ClusterCenterOfGravity replaced by [nidm:'Cluster Center Of Gravity'](http://www.incf.org/ns/nidash/nidm#NIDM_0000140)  ([PR 301](https://github.com/incf-nidash/nidm/pull/301)).
- spm:expectedNumberOfClusters replaced by [nidm:'expected Number Of Clusters'](http://www.incf.org/ns/nidash/nidm#NIDM_0000141)  ([PR 301](https://github.com/incf-nidash/nidm/pull/301)).
- spm:expectedNumberOfVerticesPerCluster replaced by [nidm:'expected Number Of Vertices Per Cluster'](http://www.incf.org/ns/nidash/nidm#NIDM_0000142)  ([PR 301](https://github.com/incf-nidash/nidm/pull/301)).
- spm:expectedNumberOfVoxelsPerCluster replaced by [nidm:'expected Number Of Voxels Per Cluster'](http://www.incf.org/ns/nidash/nidm#NIDM_0000143) ([PR 301](https://github.com/incf-nidash/nidm/pull/301)).
- spm:ReselsPerVoxelMap replaced by [nidm:'Resels Per Voxel Map'](http://www.incf.org/ns/nidash/nidm#NIDM_0000144) ([PR 301](https://github.com/incf-nidash/nidm/pull/301)).
- fsl:dlh replaced by [nidm:'noise Roughness In Voxels'](http://www.incf.org/ns/nidash/nidm#NIDM_0000145) ([PR 275](https://github.com/incf-nidash/nidm/pull/275) and [PR 301](https://github.com/incf-nidash/nidm/pull/301)).
- spm:heightCriticalThresholdFDR05 replaced by [nidm:'height Critical Threshold FDR 05'](http://www.incf.org/ns/nidash/nidm#NIDM_0000146) ([PR 301](https://github.com/incf-nidash/nidm/pull/301)).
- spm:heightCriticalThresholdFWE05 replaced by [nidm:'height Critical Threshold FWE 05'](http://www.incf.org/ns/nidash/nidm#NIDM_0000147) ([PR 301](https://github.com/incf-nidash/nidm/pull/301)).
- fsl:reselSizeInVoxels and spm:reselSize replaced by [nidm:'resel Size In Voxels'](http://www.incf.org/ns/nidash/nidm#NIDM_0000148)  ([PR 275](https://github.com/incf-nidash/nidm/pull/275)).
- spm:searchVolumeInResels replaced by [nidm:'search Volume In Resels'](http://www.incf.org/ns/nidash/nidm#NIDM_0000149)  ([PR 275](https://github.com/incf-nidash/nidm/pull/275)).

### coordinate1, coordinate2, coordinate3 -> coordinate Vector ([PR 270](https://github.com/incf-nidash/nidm/pull/270)):
- nidm:coordinate1, nidm:coordinate2, nidm:coordinate3 replaced by [nidm:'coordinate Vector'](http://www.incf.org/ns/nidash/nidm#NIDM_0000086)

#### New terms
Hemodynamic Response Function (HRF)([PR 248](https://github.com/incf-nidash/nidm/pull/248)):
- New attribute nidm:hasHRFBasis in nidm:DesignMatrix (only for first-level analyses) to represent which hemodynamic response function that was used.

Drift models ([PR 261](https://github.com/incf-nidash/nidm/pull/261)):
- New attribute nidm:hasDriftModel in nidm:DesignMatrix (only for first-level analyses) to represent which drift model was used.

Type of fMRI design and regressor names ([PR 299](https://github.com/incf-nidash/nidm/pull/299)):
- New attribute [nidm:'has fMRI Design'](http://www.incf.org/ns/nidash/nidm#NIDM_0000010) in nidm:DesignMatrix (only for first-level analyses) specifying the type of fMRI design (block-based, event-related, mixed).
- New attribute [nidm:'regressor Names'](http://www.incf.org/ns/nidash/nidm#NIDM_0000021) in nidm:DesignMatrix (only for first-level analyses) providing list of abstract names for the design matrix regressors.


#### Updated labels
- "ExcursionSet" replaced by "Excursion Set Map" ([PR 256](https://github.com/incf-nidash/nidm/pull/256))
- "Cluster" replaced by "Significant Cluster" ([PR 71](https://github.com/incf-nidash/nidm/pull/71))
- "numberOfClusters" replaced by "number of Significant Clusters" ([PR 292](https://github.com/incf-nidash/nidm/pull/292))
- nidm:Data replaced by [nidm:'Data Scaling'](http://www.incf.org/ns/nidash/nidm#NIDM_0000018) ([PR 285](https://github.com/incf-nidash/nidm/pull/285))
- spm:KConjunctionInference replaced by [spm:'Partial Conjunction Inference'](http://www.incf.org/ns/nidash/spm#SPM_0000005)([PR 294](https://github.com/incf-nidash/nidm/pull/294) and [PR 316](https://github.com/incf-nidash/nidm/pull/316)).
- nidm:globalNullDegree replaced by [nidm:'Partial Conjunction Degree'](http://www.incf.org/ns/nidash/nidm#NIDM_0000095) ([PR 294](https://github.com/incf-nidash/nidm/pull/294) and [PR 316](https://github.com/incf-nidash/nidm/pull/316)).


#### Deprecated terms:
- spm:softwareVersion deprecated [PR 291](https://github.com/incf-nidash/nidm/pull/291)
- fsl:ClusterMaximumStatistic deprecated [PR 286](https://github.com/incf-nidash/nidm/pull/286)
- nidm:objectModel deprecated [PR 137](https://github.com/incf-nidash/nidm/pull/137)