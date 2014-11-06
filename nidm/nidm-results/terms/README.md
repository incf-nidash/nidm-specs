<h1>NIDM-Results Terms curation status</h1><b>Curation status</b>: 
<img src="../../../doc/content/specs/img/green.png?raw=true"/>&nbsp;Pending final vetting;
<img src="../../../doc/content/specs/img/orange.png?raw=true"/>&nbsp;Metadata incomplete; Metadata complete; Requires discussion;
<img src="../../../doc/content/specs/img/red.png?raw=true"/>&nbsp;Uncurated;
<img src="../../../doc/content/specs/img/yellow.png?raw=true"/>&nbsp;To be replaced with external ontology term;
<h2>Classes</h2>
<table>
<tr><th>Curation Status</th><th>Term</th></tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>fsl:NonParametricSymmetricDistribution: </b>Probability distribution estimated empirically on the data assuming a symmetric probability distribution. Non-parametric distribution are usually estimated using permutation of the class labels or sign-flipping.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:ContrastMap: </b>A map whose value at each location is statistical contrast estimate.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:ContrastStandardErrorMap: </b>A map whose value at each location is the standard error of a given contrast.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:Data: </b>"A collection or single item of factual information, derived from measurement or research, from which conclusions may be drawn."</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:DesignMatrix: </b>A matrix of values defining the explanatory variables used in a regression model.  Each column corresponds to one explanatory variable, each row corresponds to one observation. (editor: TN)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:ExcursionSet: </b>Set of map elements surviving a thresholding procedure.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:FSL: </b>FMRIB Software Library software package for the analysis of neuroimaging data from the FMRIB.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:HeightThreshold: </b>A numerical value that establishes a bound on a range of voxelwise or vertex-wise defined statistic.
</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:NonParametricDistribution: </b>Probability distribution estimated empirically on the data without assumption on the shape of the probability distribution. Non-parametric distribution are usually estimated using permutation of the class labels or sign-flipping.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:ResidualMeanSquaresMap: </b>A map whose value at each location is the residual of the mean squares fit to the data. (editor: KH)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:SPM: </b>Statistical Parametric Mapping software package for the analysis of neuroimaging data from the FIL Methods Group.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td><b>nidm:ContrastEstimation: </b>The process of estimating a contrast from the estimated parameters of statistical model.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td><b>nidm:ContrastWeights: </b>Vector defining the linear combination associated with a particular contrast. </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td><b>nidm:ModelParametersEstimation: </b>The process of estimating the parameters of a general linear model from the available data.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>fsl:CenterOfGravity: </b>Centre Of Gravity for the cluster, equivalent to the concept of Centre Of Gravity for a object with distributed mass, where intensity substitutes for mass in this case (definition from http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Cluster)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:Cluster: </b>Statistic defined at the cluster-level in an excusion set. In SPM it is defined as the cluster size. FIXME (now Cluster instead of ClusterStatistic)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:CoordinateSpace: </b>An entity with spatial attributes (e.g., dimensions, units, and voxel-to-world mapping) that provides context to a SpatialImage (e.g., a StatisticMap).</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:CustomMaskMap: </b>mask defined by the user to restrain the space in which model fitting is performed.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:ExtentThreshold: </b>A numerical value that establishes a bound on a range of cluster-sizes. / [from extentThresh:]        Minimum cluster size used when thresholding a statistic image        5voxels
</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:MNICoordinateSystem: </b>Coordinate system defined with reference to the MNI atlas.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:MaskMap: </b>map or surface on which the associated results are displayed. </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:ParameterEstimateMap: </b>A map whose value at each location is the estimate of a model parameter.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:Peak: </b>Statistic defined at the peak-level in an excursion set. FIXME (now Peak instead of PeakStatistic)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:SearchSpaceMap: </b>mask in which the inference was performed.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:StandardizedCoordinateSystem: </b>Parent of all reference spaces except "Subject".</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:StatisticMap: </b>A map whose value at each location is a statistic. </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:SubjectCoordinateSystem: </b>Coordinate system defined by the subject brain (no spatial normalisation applied).</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:TalairachCoordinateSystem: </b>Reference space defined by the dissected brain used for the Talairach and Tournoux atlas.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>spm:KConjunctionInference: </b>Inference testing for the joint significance of a subset of the effects.</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>spm:ReselsPerVoxelMap: </b>A map whose value at each location is the number of resels per voxel. </td>
</tr>
</table><h2>Properties</h2>
<table>
<tr><th>Curation Status</th><th>Term</th><th>Domain</th><th>Range</th></tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:clusterLabelId: </b>Integer associated with a particular cluster as specified in the clusterLabelsMap.</td>
    <td>nidm:Cluster </td>
    <td>xsd:int </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:clusterSizeInVoxels: </b>Number of voxels that make up the cluster.</td>
    <td>nidm:Cluster nidm:ExtentThreshold </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:grandMeanScaling: </b>Binary flag defining whether the data was scaled. Specifically, "grand mean scaling" refers to multipliciation of every voxel in every scan by a common value.  Grand mean scaling is essential for first-level fMRI, to transform the arbitrary MRI units, but is generally not used with second level analyses.</td>
    <td>nidm:Data </td>
    <td>xsd:boolean </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:hasErrorDistribution: </b>Property that associates an ErrorDistribution with an ErrorModel.</td>
    <td>nidm:ErrorModel </td>
    <td>nidm:ErrorDistribution </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:maskedMedian: </b>Median value considering only in-mask voxels. Useful diagnostic when computed on grand mean image when grandMeanScaling is TRUE, as the median should be close to targetIntensity. (editor: TN, Naming discussed at: https://github.com/incf-nidash/nidm/issues/70)</td>
    <td>nidm:GrandMeanMap </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:softwareVersion: </b>Name and number that specifies the software version.</td>
    <td>prov:SoftwareAgent </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>nidm:targetIntensity: </b>Value to which the grand mean of the Data was scaled (applies only if grandMeanScaling is true).</td>
    <td>nidm:Data </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>spm:expectedNumberOfClusters: </b>Expected number of clusters in an excursion set.</td>
    <td>nidm:SearchSpaceMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>spm:searchVolumeReselsGeometry: </b>Description of geometry of search volume.  As per Worsley et al. [ http://www.ncbi.nlm.nih.gov/pubmed/20408186 ], the first element is the Euler Characteristic of the search volume, the second element is twice the average caliper diameter, the third element is half the surface area, and the fourth element is the volume.  With the exception of the first element (which is a unitless integer) all quantities are in units of Resels.</td>
    <td>nidm:SearchSpaceMap </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>spm:smallestSignifClusterSizeInVerticesFDR05: </b>Smallest cluster size in vertices that are significant at a false discovery rate corrected alpha value of 0.05.  </td>
    <td>nidm:SearchSpaceMap </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>spm:smallestSignifClusterSizeInVerticesFWE05: </b>Smallest cluster size in vertices significant at family-wise error rate corrected alpha value of 0.05. 
</td>
    <td>nidm:SearchSpaceMap </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>spm:smallestSignifClusterSizeInVoxelsFDR05: </b>Smallest cluster size in voxels significant at false discovery rate corrected alpha value of 0.05.  </td>
    <td>nidm:SearchSpaceMap </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><b>spm:smallestSignifClusterSizeInVoxelsFWE05: </b>Smallest cluster size in voxels significant at family-wise error corrected alpha value of 0.05. 
</td>
    <td>nidm:SearchSpaceMap </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:userSpecifiedThresholdType: </b>Type of method used to define a threshold (e.g. statistic value, uncorrected P-value or corrected P-value). (editor: Discussed in https://github.com/incf-nidash/nidm/pull/150)</td>
    <td>nidm:ExtentThreshold nidm:HeightThreshold </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td><b>spm:searchVolumeInVoxels: </b>Total number of voxels within the search volume.</td>
    <td>nidm:SearchSpaceMap </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td><b>nidm:pValueFWER: </b>"A quantitative confidence value resulting from a multiple testing error correction method which adjusts the p-value used as input to control for Type I error in the context of multiple pairwise tests"</td>
    <td>nidm:Cluster nidm:ExtentThreshold nidm:HeightThreshold nidm:Peak </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td><b>nidm:pValueUncorrected: </b>A p-value reported without correction for multiple testing.        </td>
    <td>nidm:Cluster nidm:ExtentThreshold nidm:HeightThreshold nidm:Peak </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>fsl:coordinate1InVoxels: </b>Coordinate along the first dimension in voxels.</td>
    <td>nidm:Coordinate </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>fsl:coordinate2InVoxels: </b>Coordinate along the second dimension in voxels.</td>
    <td>nidm:Coordinate </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>fsl:coordinate3InVoxels: </b>Coordinate along the third dimension in voxels</td>
    <td>nidm:Coordinate </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:clusterSizeInVertices: </b>Number of vertices that make up the cluster.</td>
    <td>nidm:Cluster nidm:ExtentThreshold </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:contrastName: </b>Name of the contrast.</td>
    <td>nidm:ContrastMap nidm:ContrastWeights nidm:StatisticMap </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:coordinate1: </b>Coordinate along the first dimension in voxel units.</td>
    <td>nidm:Coordinate </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:coordinate2: </b>Coordinate along the second dimension in voxel units.</td>
    <td>nidm:Coordinate </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:coordinate3: </b>Coordinate along the third dimension in voxel units.</td>
    <td>nidm:Coordinate </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:dimensionsInVoxels: </b>Dimensions of some N-dimensional data.</td>
    <td>nidm:CoordinateSpace </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:effectDegreesOfFreedom: </b>Degrees of freedom of the effect.</td>
    <td>nidm:StatisticMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:equivalentZStatistic: </b>Statistic value transformed into Z units; the output of a process which takes a non-normal statistic and transforms it to an equivalent z score.</td>
    <td>nidm:Peak </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:errorDegreesOfFreedom: </b>Degrees of freedom of the error.</td>
    <td>nidm:StatisticMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:hasClusterLabelsMap: </b>A map whose value at each location denotes cluster membership. Each cluster is denoted by a different integer.</td>
    <td>nidm:ExcursionSet </td>
    <td>nidm:ClusterLabelsMap </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:inWorldCoordinateSystem: </b>Type of coordinate system.</td>
    <td>nidm:CoordinateSpace </td>
    <td>nidm:WorldCoordinateSystem </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:noiseFWHM: </b>Estimated Full Width at Half Maximum of the noise distribution. (editor: Under discussion at https://github.com/incf-nidash/nidm/issues/173)</td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:numberOfDimensions: </b>Number of dimensions of a data matrix.</td>
    <td>nidm:CoordinateSpace </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:randomFieldStationarity: </b>Is the random field assumed to be stationary across the entire search volume? (editor: Under discussion at https://github.com/incf-nidash/nidm/issues/130)</td>
    <td>nidm:SearchSpaceMap </td>
    <td>xsd:boolean </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:visualisation: </b>Graphical representation of an entity.</td>
    <td>nidm:DesignMatrix nidm:ExcursionSet </td>
    <td>nidm:Image </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:voxelSize: </b>3D size of a voxel measured in voxelUnits.</td>
    <td>nidm:CoordinateSpace </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>nidm:voxelUnits: </b>Units associated with each dimensions of some N-dimensional data. (editor: Under discussion at https://github.com/incf-nidash/nidm/issues/147)</td>
    <td>nidm:CoordinateSpace </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>spm:expectedNumberOfVerticesPerCluster: </b>Expected number of vertices in a cluster.</td>
    <td>nidm:SearchSpaceMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>spm:expectedNumberOfVoxelsPerCluster: </b>Expected number of voxels in a cluster.</td>
    <td>nidm:SearchSpaceMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>spm:hasMaximumIntensityProjection: </b>Maximum intensity projection of a map.</td>
    <td>nidm:ExcursionSet </td>
    <td>nidm:Image </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>spm:noiseFWHMInUnits: </b>Estimated Full Width at Half Maximum of the noise distribution in world units.</td>
    <td>nidm:SearchSpaceMap </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>spm:noiseFWHMInVertices: </b>Estimated Full Width at Half Maximum of the noise distribution in world vertices.</td>
    <td>nidm:MaskMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>spm:noiseFWHMInVoxels: </b>Estimated Full Width at Half Maximum of the noise distribution in voxels.</td>
    <td>nidm:SearchSpaceMap </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>spm:reselSize: </b>Size of one resel in voxels or vertices.</td>
    <td>nidm:SearchSpaceMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>spm:searchVolumeInVertices: </b>Total number of vertices within the search volume.</td>
    <td>nidm:SearchSpaceMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><b>spm:softwareRevision: </b>revision number of a piece of software.</td>
    <td>prov:SoftwareAgent </td>
    <td>xsd:string </td>
</tr>
</table>