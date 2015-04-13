<h1>NIDM-Results Terms curation status</h1>You will find below a listing of the NIDM-Results terms that need to be curated. If you would like **to help with the curation of a term, please follow those steps**:
 1. Check if the terms is already under discussion in an issue.
 2. If not, create a new issue including the current definition (available in  the table below) and your proposed update.

If possible, priority should be given to uncurated terms (in red).

Thank you in advance for taking part in NIDM-Results term curation!

<b>Curation status</b>: 
<img src="../../../doc/content/specs/img/green.png?raw=true"/>&nbsp;Pending final vetting;
<img src="../../../doc/content/specs/img/orange.png?raw=true"/>&nbsp;Metadata incomplete; Metadata complete; Requires discussion;
<img src="../../../doc/content/specs/img/red.png?raw=true"/>&nbsp;Uncurated;
<img src="../../../doc/content/specs/img/yellow.png?raw=true"/>&nbsp;To be replaced with external ontology term;
<h2>Classes</h2>
<table>
<tr><th>Curation Status</th><th>Issue/PR</th><th>Term</th></tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=LegendrePolynomialDriftModel"> [find issues/PR] </a></td>
    <td><b>afni:LegendrePolynomialDriftModel: </b>A drift model in which the drifts are modeled by a Legendre orthogonal polynomial basis added to the regression model</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=GaussianRunningLineDriftModel"> [find issues/PR] </a></td>
    <td><b>fsl:GaussianRunningLineDriftModel: </b>A drift model in which the drifts are modeled with a Gaussian-weighted running line smoother, fit to and subtracted from the data and each column of the design matrix</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/285">#285</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=Data"> [more] </a></td>
    <td><b>nidm:Data: </b>"A collection or single item of factual information, derived from measurement or research, from which conclusions may be drawn." (This definition is from NCIT)(same as: <a href=http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C25474>http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C25474</a>)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/274">#274</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=DesignMatrix"> [more] </a></td>
    <td><b>nidm:DesignMatrix: </b>A matrix of values defining the explanatory variables used in a regression model.  Each column corresponds to one explanatory variable, each row corresponds to one observation (editor: TN)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=DriftModel"> [find issues/PR] </a></td>
    <td><b>nidm:DriftModel: </b>A model used to compensate for low frequency baseline drifts when analyzing functional MRI data at the subject level</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/280">#280</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=HeightThreshold"> [more] </a></td>
    <td><b>nidm:HeightThreshold: </b>A numerical value that establishes a bound on a range of voxelwise or vertex-wise defined statistic.
</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=DCTDriftModel"> [find issues/PR] </a></td>
    <td><b>spm:DCTDriftModel: </b>A drift model in which the drifts are modeled by a Discrete Cosine Transform basis added to regression model</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=BLOCK"> [more] </a></td>
    <td><b>afni:BLOCK: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=FiniteImpulseResponseHRB"> [more] </a></td>
    <td><b>afni:FiniteImpulseResponseHRB: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a>
Discussed with @afni-rickr in <a href="https://github.com/incf-nidash/nidm/pull/248">#248</a>: supported via GAM<br/><a href="https://github.com/incf-nidash/nidm//issues?&q=GammaHRF"> [more] </a></td>
    <td><b>afni:GammaHRF: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/286">#286</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=ClusterMaximumStatistic"> [more] </a></td>
    <td><b>fsl:ClusterMaximumStatistic: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/287">#287</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=ContrastVarianceMap"> [more] </a></td>
    <td><b>fsl:ContrastVarianceMap: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=CustomHRB"> [more] </a></td>
    <td><b>fsl:CustomHRB: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=FiniteImpulseResponseHRB"> [more] </a></td>
    <td><b>fsl:FiniteImpulseResponseHRB: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=GammaDifferenceHRF"> [more] </a></td>
    <td><b>fsl:GammaDifferenceHRF: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=GammaHRB"> [more] </a></td>
    <td><b>fsl:GammaHRB: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=GammaHRF"> [more] </a></td>
    <td><b>fsl:GammaHRF: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=GaussianHRF"> [more] </a></td>
    <td><b>fsl:GaussianHRF: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=NoHRF"> [more] </a></td>
    <td><b>fsl:NoHRF: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=SineHRB"> [more] </a></td>
    <td><b>fsl:SineHRB: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=TemporalDerivative"> [more] </a></td>
    <td><b>fsl:TemporalDerivative: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/282">#282</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=ClusterLabelsMap"> [more] </a></td>
    <td><b>nidm:ClusterLabelsMap: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/137">#137</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=FSLResults"> [more] </a></td>
    <td><b>nidm:FSLResults: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=FiniteImpulseResponseHRB"> [more] </a></td>
    <td><b>nidm:FiniteImpulseResponseHRB: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=GammaDifferenceHRF"> [more] </a></td>
    <td><b>nidm:GammaDifferenceHRF: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=GammaHRB"> [more] </a></td>
    <td><b>nidm:GammaHRB: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=GammaHRF"> [more] </a></td>
    <td><b>nidm:GammaHRF: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/288">#288</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=GrandMeanMap"> [more] </a></td>
    <td><b>nidm:GrandMeanMap: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=HemodynamicResponseFunction"> [more] </a></td>
    <td><b>nidm:HemodynamicResponseFunction: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=HemodynamicResponseFunctionBasis"> [more] </a></td>
    <td><b>nidm:HemodynamicResponseFunctionBasis: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=HemodynamicResponseFunctionDerivative"> [more] </a></td>
    <td><b>nidm:HemodynamicResponseFunctionDerivative: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/137">#137</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=NIDMObjectModel"> [more] </a></td>
    <td><b>nidm:NIDMObjectModel: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/137">#137</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=SPMResults"> [more] </a></td>
    <td><b>nidm:SPMResults: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/194">#194</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=SpatialModel"> [more] </a></td>
    <td><b>nidm:SpatialModel: </b>FIXME</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/194">#194</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=SpatiallyGlobalModel"> [more] </a></td>
    <td><b>nidm:SpatiallyGlobalModel: </b>FIXME</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/194">#194</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=SpatiallyLocalModel"> [more] </a></td>
    <td><b>nidm:SpatiallyLocalModel: </b>FIXME</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/194">#194</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=SpatiallyRegularizedModel"> [more] </a></td>
    <td><b>nidm:SpatiallyRegularizedModel: </b>FIXME</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=WorldCoordinateSystem"> [more] </a></td>
    <td><b>nidm:WorldCoordinateSystem: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=DispersionDerivative"> [more] </a></td>
    <td><b>spm:DispersionDerivative: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=FiniteImpulseResponseHRB"> [more] </a></td>
    <td><b>spm:FiniteImpulseResponseHRB: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=FourierHRB"> [more] </a></td>
    <td><b>spm:FourierHRB: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=GammaDifferenceHRF"> [more] </a></td>
    <td><b>spm:GammaDifferenceHRF: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=GammaHRB"> [more] </a></td>
    <td><b>spm:GammaHRB: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=TemporalDerivative"> [more] </a></td>
    <td><b>spm:TemporalDerivative: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/ISA-tools/stato/pull/28">ISA-tools/stato#28</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=ArbitrarilyCorrelatedError"> [more] </a></td>
    <td><b>nidm:ArbitrarilyCorrelatedError: </b>&lt;undefined&gt; (editor: TN)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/ISA-tools/stato/pull/28">ISA-tools/stato#28</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=CompoundSymmetricError"> [more] </a></td>
    <td><b>nidm:CompoundSymmetricError: </b>&lt;undefined&gt; (editor: TN)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/276">#276</a>, discussed in <a href="https://github.com/ISA-tools/stato/pull/23">ISA-tools/stato#23</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=ContrastEstimation"> [more] </a></td>
    <td><b>nidm:ContrastEstimation: </b>The process of estimating a contrast from the estimated parameters of statistical model</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at: <a href="https://github.com/ISA-tools/stato/pull/23">ISA-tools/stato#23</a>
Range: Vector of integers not found.<br/><a href="https://github.com/incf-nidash/nidm//issues?&q=ContrastWeights"> [more] </a></td>
    <td><b>nidm:ContrastWeights: </b>Vector defining the linear combination associated with a particular contrast. </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/ISA-tools/stato/pull/28">ISA-tools/stato#28</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=ExchangeableError"> [more] </a></td>
    <td><b>nidm:ExchangeableError: </b>&lt;undefined&gt; (editor: TN)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/ISA-tools/stato/pull/28">ISA-tools/stato#28</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=IndependentError"> [more] </a></td>
    <td><b>nidm:IndependentError: </b>&lt;undefined&gt; (editor: TN)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/ISA-tools/stato/pull/28">ISA-tools/stato#28</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=SeriallyCorrelatedError"> [more] </a></td>
    <td><b>nidm:SeriallyCorrelatedError: </b>&lt;undefined&gt; (editor: TN)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/290">#290</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=CoordinateSpace"> [more] </a></td>
    <td><b>nidm:CoordinateSpace: </b>An entity with spatial attributes (e.g., dimensions, units, and voxel-to-world mapping) that provides context to a SpatialImage (e.g., a StatisticMap)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=CustomCoordinateSystem"> [more] </a></td>
    <td><b>nidm:CustomCoordinateSystem: </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=MNICoordinateSystem"> [more] </a></td>
    <td><b>nidm:MNICoordinateSystem: </b>Coordinate system defined with reference to the MNI atlas</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/283">#283</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=Peak"> [more] </a></td>
    <td><b>nidm:Peak: </b>Statistic defined at the peak-level in an excursion set. FIXME (now Peak instead of PeakStatistic)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=StandardizedCoordinateSystem"> [more] </a></td>
    <td><b>nidm:StandardizedCoordinateSystem: </b>Parent of all reference spaces except "Subject"</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=SubjectCoordinateSystem"> [more] </a></td>
    <td><b>nidm:SubjectCoordinateSystem: </b>Coordinate system defined by the subject brain (no spatial normalisation applied)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=TalairachCoordinateSystem"> [more] </a></td>
    <td><b>nidm:TalairachCoordinateSystem: </b>Reference space defined by the dissected brain used for the Talairach and Tournoux atlas</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/294">#294</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=KConjunctionInference"> [more] </a></td>
    <td><b>spm:KConjunctionInference: </b>Inference testing for the joint significance of a subset of the effects</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=ReselsPerVoxelMap"> [find issues/PR] </a></td>
    <td><b>spm:ReselsPerVoxelMap: </b>A map whose value at each location is the number of resels per voxel. </td>
</tr>
</table><h2>Properties</h2>
<table>
<tr><th>Curation Status</th><th>Issue/PR</th><th>Term</th><th>Domain</th><th>Range</th></tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=driftBasisOrder"> [find issues/PR] </a></td>
    <td><b>afni:driftBasisOrder: </b>The number of basis in the drift model</td>
    <td>afni:LegendrePolynomialDriftModel </td>
    <td>xsd:int </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=driftCutoffPeriod"> [find issues/PR] </a></td>
    <td><b>fsl:driftCutoffPeriod: </b>Full Width at Half Maximum in seconds of the Gaussian weight function used in the running line smoother</td>
    <td>fsl:GaussianRunningLineDriftModel </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=clusterSizeInVoxels"> [find issues/PR] </a></td>
    <td><b>nidm:clusterSizeInVoxels: </b>Number of voxels that make up the cluster</td>
    <td>nidm:ExtentThreshold nidm:SignificantCluster </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/285">#285</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=grandMeanScaling"> [more] </a></td>
    <td><b>nidm:grandMeanScaling: </b>Binary flag defining whether the data was scaled. Specifically, "grand mean scaling" refers to multipliciation of every voxel in every scan by a common value.  Grand mean scaling is essential for first-level fMRI, to transform the arbitrary MRI units, but is generally not used with second level analyses</td>
    <td>nidm:Data </td>
    <td>xsd:boolean </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=hasDriftModel"> [find issues/PR] </a></td>
    <td><b>nidm:hasDriftModel: </b>A property that associates a drift model to a design matrix (only used for first-level fMRI experiments)</td>
    <td>nidm:DesignMatrix </td>
    <td>nidm:DriftModel </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/288">#288</a>, naming previously discussed at: <a href="https://github.com/incf-nidash/nidm/pull/70">#70</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=maskedMedian"> [more] </a></td>
    <td><b>nidm:maskedMedian: </b>Median value considering only in-mask voxels. Useful diagnostic when computed on grand mean image when grandMeanScaling is TRUE, as the median should be close to targetIntensity</td>
    <td>nidm:GrandMeanMap </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/291">#291</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=softwareVersion"> [more] </a></td>
    <td><b>nidm:softwareVersion: </b>Name and number that specifies the software version</td>
    <td>prov:SoftwareAgent </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/285">#285</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=targetIntensity"> [more] </a></td>
    <td><b>nidm:targetIntensity: </b>Value to which the grand mean of the Data was scaled (applies only if grandMeanScaling is true)</td>
    <td>nidm:Data </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=driftCutoffPeriod"> [find issues/PR] </a></td>
    <td><b>spm:driftCutoffPeriod: </b>Discrete Cosine Transform basis cut-off, specified as period length in seconds and ensures that all basis elements will have period of this duration or longer</td>
    <td>spm:DCTDriftModel </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=expectedNumberOfClusters"> [find issues/PR] </a></td>
    <td><b>spm:expectedNumberOfClusters: </b>Expected number of clusters in an excursion set</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=searchVolumeReselsGeometry"> [find issues/PR] </a></td>
    <td><b>spm:searchVolumeReselsGeometry: </b>Description of geometry of search volume.  As per Worsley et al. [ http://www.ncbi.nlm.nih.gov/pubmed/20408186 ], the first element is the Euler Characteristic of the search volume, the second element is twice the average caliper diameter, the third element is half the surface area, and the fourth element is the volume.  With the exception of the first element (which is a unitless integer) all quantities are in units of Resels</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=smallestSignifClusterSizeInVerticesFDR05"> [find issues/PR] </a></td>
    <td><b>spm:smallestSignifClusterSizeInVerticesFDR05: </b>Smallest cluster size in vertices that are significant at a false discovery rate corrected alpha value of 0.05.  </td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=smallestSignifClusterSizeInVerticesFWE05"> [find issues/PR] </a></td>
    <td><b>spm:smallestSignifClusterSizeInVerticesFWE05: </b>Smallest cluster size in vertices significant at family-wise error rate corrected alpha value of 0.05</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=smallestSignifClusterSizeInVoxelsFDR05"> [find issues/PR] </a></td>
    <td><b>spm:smallestSignifClusterSizeInVoxelsFDR05: </b>Smallest cluster size in voxels significant at false discovery rate corrected alpha value of 0.05.  </td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=smallestSignifClusterSizeInVoxelsFWE05"> [find issues/PR] </a></td>
    <td><b>spm:smallestSignifClusterSizeInVoxelsFWE05: </b>Smallest cluster size in voxels significant at family-wise error corrected alpha value of 0.05. 
</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=userSpecifiedThresholdType"> [find issues/PR] </a></td>
    <td><b>nidm:userSpecifiedThresholdType: </b>Type of method used to define a threshold (e.g. statistic value, uncorrected P-value or corrected P-value) (editor: Discussed in https://github.com/incf-nidash/nidm/pull/150)</td>
    <td>nidm:ExtentThreshold nidm:HeightThreshold </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at: <a href="https://github.com/incf-nidash/nidm/pull/270">#270</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=coordinateInVoxels"> [more] </a></td>
    <td><b>fsl:coordinateInVoxels: </b>Coordinate along the first dimension in voxels. (This definition needs to be re-worked as this term was renamed from coordinate1 to coordinate in https://github.com/incf-nidash/nidm/issues/270)</td>
    <td>nidm:Coordinate </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/214">#214</a> and <a href="https://github.com/incf-nidash/nidm/pull/275">#275</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=dlh"> [more] </a></td>
    <td><b>fsl:dlh: </b>&lt;undefined&gt;</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/291">#291</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=featVersion"> [more] </a></td>
    <td><b>fsl:featVersion: </b>&lt;undefined&gt;</td>
    <td>nlx:birnlex_2067 </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/275">#275</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=reselSizeInVoxels"> [more] </a></td>
    <td><b>fsl:reselSizeInVoxels: </b>&lt;undefined&gt;</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at: <a href="https://github.com/incf-nidash/nidm/pull/270">#270</a> and <a href="https://github.com/incf-nidash/nidm/pull/145">#145</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=coordinate"> [more] </a></td>
    <td><b>nidm:coordinate: </b>Coordinate along the first dimension in voxel units. (This definition needs to be re-worked as this term was renamed from coordinate1 to coordinate in https://github.com/incf-nidash/nidm/issues/270)</td>
    <td>nidm:Coordinate </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/194">#194</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=dependenceSpatialModel"> [more] </a></td>
    <td><b>nidm:dependenceSpatialModel: </b>FIXME</td>
    <td>nidm:ErrorModel </td>
    <td>nidm:SpatialModel </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/294">#294</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=globalNullDegree"> [more] </a></td>
    <td><b>nidm:globalNullDegree: </b>&lt;undefined&gt;</td>
    <td>spm:KConjunctionInference </td>
    <td>xsd:int </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=hasHRFBasis"> [more] </a></td>
    <td><b>nidm:hasHRFBasis: </b>&lt;undefined&gt;</td>
    <td>nidm:DesignMatrix </td>
    <td>nidm:HemodynamicResponseFunctionBasis </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/292">#292</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=numberOfClusters"> [more] </a></td>
    <td><b>nidm:numberOfClusters: </b>&lt;undefined&gt;</td>
    <td>nidm:ExcursionSetMap </td>
    <td>xsd:int </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/137">#137</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=objectModel"> [more] </a></td>
    <td><b>nidm:objectModel: </b>&lt;undefined&gt;</td>
    <td>prov:Bundle </td>
    <td>nidm:NIDMObjectModel </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=searchVolumeInVoxels"> [find issues/PR] </a></td>
    <td><b>nidm:searchVolumeInVoxels: </b>Total number of voxels within the search volume</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/293">#293</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=statisticType"> [more] </a></td>
    <td><b>nidm:statisticType: </b>&lt;undefined&gt;</td>
    <td>nidm:ContrastWeights nidm:StatisticMap </td>
    <td>obo:STATO_0000039 </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/194">#194</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=varianceSpatialModel"> [more] </a></td>
    <td><b>nidm:varianceSpatialModel: </b>FIXME</td>
    <td>nidm:ErrorModel </td>
    <td>nidm:SpatialModel </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/137">#137</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=version"> [more] </a></td>
    <td><b>nidm:version: </b>&lt;undefined&gt;</td>
    <td>prov:Bundle </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/293">#293</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=withEstimationMethod"> [more] </a></td>
    <td><b>nidm:withEstimationMethod: </b>FIXME</td>
    <td>nidm:ModelParametersEstimation </td>
    <td>obo:STATO_0000119 </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/275">#275</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=searchVolumeInResels"> [more] </a></td>
    <td><b>spm:searchVolumeInResels: </b>Total number of resels within the search volume</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/ISA-tools/stato/pull/38">ISA-tools/stato#38</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=pValueFWER"> [more] </a></td>
    <td><b>nidm:pValueFWER: </b>"A quantitative confidence value resulting from a multiple testing error correction method which adjusts the p-value used as input to control for Type I error in the context of multiple pairwise tests"(same as: <a href=This definition is from OBI. Please update this note if the definition is modified.>This definition is from OBI. Please update this note if the definition is modified.</a>)</td>
    <td>nidm:ExtentThreshold nidm:HeightThreshold nidm:Peak nidm:SignificantCluster </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/ISA-tools/stato/pull/38">ISA-tools/stato#38</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=pValueUncorrected"> [more] </a></td>
    <td><b>nidm:pValueUncorrected: </b>A p-value reported without correction for multiple testing.        </td>
    <td>nidm:ExtentThreshold nidm:HeightThreshold nidm:Peak nidm:SignificantCluster </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=clusterSizeInVertices"> [find issues/PR] </a></td>
    <td><b>nidm:clusterSizeInVertices: </b>Number of vertices that make up the cluster</td>
    <td>nidm:ExtentThreshold nidm:SignificantCluster </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=contrastName"> [find issues/PR] </a></td>
    <td><b>nidm:contrastName: </b>Name of the contrast</td>
    <td>nidm:ContrastMap nidm:ContrastWeights nidm:StatisticMap </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at: <a href="https://github.com/incf-nidash/nidm/pull/146">#146</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=dimensionsInVoxels"> [more] </a></td>
    <td><b>nidm:dimensionsInVoxels: </b>Dimensions of some N-dimensional data</td>
    <td>nidm:CoordinateSpace </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/277">#277</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=effectDegreesOfFreedom"> [more] </a></td>
    <td><b>nidm:effectDegreesOfFreedom: </b>Degrees of freedom of the effect</td>
    <td>nidm:StatisticMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=equivalentZStatistic"> [find issues/PR] </a></td>
    <td><b>nidm:equivalentZStatistic: </b>Statistic value transformed into Z units; the output of a process which takes a non-normal statistic and transforms it to an equivalent z score</td>
    <td>nidm:Peak </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/277">#277</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=errorDegreesOfFreedom"> [more] </a></td>
    <td><b>nidm:errorDegreesOfFreedom: </b>Degrees of freedom of the error</td>
    <td>nidm:StatisticMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/282">#282</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=hasClusterLabelsMap"> [more] </a></td>
    <td><b>nidm:hasClusterLabelsMap: </b>A map whose value at each location denotes cluster membership. Each cluster is denoted by a different integer</td>
    <td>nidm:ExcursionSetMap </td>
    <td>nidm:ClusterLabelsMap </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=inWorldCoordinateSystem"> [more] </a></td>
    <td><b>nidm:inWorldCoordinateSystem: </b>Type of coordinate system</td>
    <td>nidm:CoordinateSpace </td>
    <td>nidm:WorldCoordinateSystem </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/173">#173</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=noiseFWHM"> [more] </a></td>
    <td><b>nidm:noiseFWHM: </b>Estimated Full Width at Half Maximum of the noise distribution</td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/130">#130</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=randomFieldStationarity"> [more] </a></td>
    <td><b>nidm:randomFieldStationarity: </b>Is the random field assumed to be stationary across the entire search volume?</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td>xsd:boolean </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=expectedNumberOfVerticesPerCluster"> [find issues/PR] </a></td>
    <td><b>spm:expectedNumberOfVerticesPerCluster: </b>Expected number of vertices in a cluster</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=expectedNumberOfVoxelsPerCluster"> [find issues/PR] </a></td>
    <td><b>spm:expectedNumberOfVoxelsPerCluster: </b>Expected number of voxels in a cluster</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/293">#293</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=hasMaximumIntensityProjection"> [more] </a></td>
    <td><b>spm:hasMaximumIntensityProjection: </b>Maximum intensity projection of a map</td>
    <td>nidm:ExcursionSetMap </td>
    <td>dctype:Image </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at: <a href="https://github.com/incf-nidash/nidm/pull/214">#214</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=noiseFWHMInUnits"> [more] </a></td>
    <td><b>spm:noiseFWHMInUnits: </b>Estimated Full Width at Half Maximum of the noise distribution in world units</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at: <a href="https://github.com/incf-nidash/nidm/pull/214">#214</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=noiseFWHMInVertices"> [more] </a></td>
    <td><b>spm:noiseFWHMInVertices: </b>Estimated Full Width at Half Maximum of the noise distribution in world vertices</td>
    <td>nidm:MaskMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at: <a href="https://github.com/incf-nidash/nidm/pull/214">#214</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=noiseFWHMInVoxels"> [more] </a></td>
    <td><b>spm:noiseFWHMInVoxels: </b>Estimated Full Width at Half Maximum of the noise distribution in voxels</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/275">#275</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=reselSize"> [more] </a></td>
    <td><b>spm:reselSize: </b>Size of one resel in voxels or vertices</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=searchVolumeInVertices"> [find issues/PR] </a></td>
    <td><b>spm:searchVolumeInVertices: </b>Total number of vertices within the search volume</td>
    <td>nidm:SearchSpaceMaskMap </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/291">#291</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=softwareRevision"> [more] </a></td>
    <td><b>spm:softwareRevision: </b>revision number of a piece of software</td>
    <td>prov:SoftwareAgent </td>
    <td>xsd:string </td>
</tr>
</table><h2>Individuals</h2>
<table>
<tr><th>Curation Status</th><th>Issue/PR</th><th>Term</th><th>Type</th></tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=Colin27CoordinateSystem"> [more] </a></td>
    <td><b>nidm:Colin27CoordinateSystem: </b>Coordinate system defined by the "stereotaxic average of 27 T1-weighted MRI scans of the same individual"</td>
    <td>nidm:StandardizedCoordinateSystem</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=Icbm452AirCoordinateSystem"> [more] </a></td>
    <td><b>nidm:Icbm452AirCoordinateSystem: </b>Coordinate system defined by the "average of 452 T1-weighted MRIs of normal young adult brains" with "linear transforms of the subjects into the atlas space using a 12-parameter affine transformation"</td>
    <td>nidm:MNICoordinateSystem</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=Icbm452Warp5CoordinateSystem"> [more] </a></td>
    <td><b>nidm:Icbm452Warp5CoordinateSystem: </b>Coordinate system defined by the "average of 452 T1-weighted MRIs of normal young adult brains" "based on a 5th order polynomial transformation into the atlas space"</td>
    <td>nidm:MNICoordinateSystem</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=IcbmMni152LinearCoordinateSystem"> [more] </a></td>
    <td><b>nidm:IcbmMni152LinearCoordinateSystem: </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, linearly transformed to Talairach space"</td>
    <td>nidm:MNICoordinateSystem</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=IcbmMni152NonLinear2009aAsymmetricCoordinateSystem"> [more] </a></td>
    <td><b>nidm:IcbmMni152NonLinear2009aAsymmetricCoordinateSystem: </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, non-linearly transformed to MNI152 linear space"</td>
    <td>nidm:MNICoordinateSystem</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=IcbmMni152NonLinear2009aSymmetricCoordinateSystem"> [more] </a></td>
    <td><b>nidm:IcbmMni152NonLinear2009aSymmetricCoordinateSystem: </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, non-linearly transformed to MNI152 linear space"</td>
    <td>nidm:MNICoordinateSystem</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=IcbmMni152NonLinear2009bAsymmetricCoordinateSystem"> [more] </a></td>
    <td><b>nidm:IcbmMni152NonLinear2009bAsymmetricCoordinateSystem: </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, non-linearly transformed to MNI152 linear space"</td>
    <td>nidm:MNICoordinateSystem</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=IcbmMni152NonLinear2009bSymmetricCoordinateSystem"> [more] </a></td>
    <td><b>nidm:IcbmMni152NonLinear2009bSymmetricCoordinateSystem: </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, non-linearly transformed to MNI152 linear space"</td>
    <td>nidm:MNICoordinateSystem</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=IcbmMni152NonLinear2009cAsymmetricCoordinateSystem"> [more] </a></td>
    <td><b>nidm:IcbmMni152NonLinear2009cAsymmetricCoordinateSystem: </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, non-linearly transformed to MNI152 linear space"</td>
    <td>nidm:MNICoordinateSystem</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=IcbmMni152NonLinear2009cSymmetricCoordinateSystem"> [more] </a></td>
    <td><b>nidm:IcbmMni152NonLinear2009cSymmetricCoordinateSystem: </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, non-linearly transformed to MNI152 linear space"</td>
    <td>nidm:MNICoordinateSystem</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=IcbmMni152NonLinear6thGenerationCoordinateSystem"> [more] </a></td>
    <td><b>nidm:IcbmMni152NonLinear6thGenerationCoordinateSystem: </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, linearly and non-linearly (6 iterations) transformed to form a symmetric model in Talairach space"</td>
    <td>nidm:MNICoordinateSystem</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=Ixi549CoordinateSystem"> [more] </a></td>
    <td><b>nidm:Ixi549CoordinateSystem: </b>Coordinate system defined by the average of the "549 [...] subjects from the IXI dataset" linearly transformed to ICBM MNI 452</td>
    <td>nidm:MNICoordinateSystem</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=Mni305CoordinateSystem"> [more] </a></td>
    <td><b>nidm:Mni305CoordinateSystem: </b>Coordinate system defined by the "average of 305 T1-weighted MRI scans, linearly transformed to Talairach space"</td>
    <td>nidm:MNICoordinateSystem</td>
</tr>
</table>