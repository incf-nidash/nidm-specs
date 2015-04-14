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
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='AFNI's Legendre Polinomial Drift Model'"> [find issues/PR] </a></td>
    <td><b>afni:'AFNI's Legendre Polinomial Drift Model': </b>A drift model in which the drifts are modeled by a Legendre orthogonal polynomial basis added to the regression model</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='FSL's Gaussian Running Line Drift Model'"> [find issues/PR] </a></td>
    <td><b>fsl:'FSL's Gaussian Running Line Drift Model': </b>A drift model in which the drifts are modeled with a Gaussian-weighted running line smoother, fit to and subtracted from the data and each column of the design matrix</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/285">#285</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Data'"> [more] </a></td>
    <td><b>nidm:'Data': </b>"A collection or single item of factual information, derived from measurement or research, from which conclusions may be drawn." (This definition is from NCIT)(same as: <a href=http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C25474>http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C25474</a>)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/274">#274</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Design Matrix'"> [more] </a></td>
    <td><b>nidm:'Design Matrix': </b>A matrix of values defining the explanatory variables used in a regression model.  Each column corresponds to one explanatory variable, each row corresponds to one observation (editor: TN)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='Drift Model'"> [find issues/PR] </a></td>
    <td><b>nidm:'Drift Model': </b>A model used to compensate for low frequency baseline drifts when analyzing functional MRI data at the subject level</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/280">#280</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Height Threshold'"> [more] </a></td>
    <td><b>nidm:'Height Threshold': </b>A numerical value that establishes a bound on a range of voxelwise or vertex-wise defined statistic.
</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='SPM's DCT Drift Model'"> [find issues/PR] </a></td>
    <td><b>spm:'SPM's DCT Drift Model': </b>A drift model in which the drifts are modeled by a Discrete Cosine Transform basis added to regression model</td>
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
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/282">#282</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Cluster Labels Map'"> [more] </a></td>
    <td><b>nidm:'Cluster Labels Map': </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/137">#137</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='FSL Results'"> [more] </a></td>
    <td><b>nidm:'FSL Results': </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Finite Impulse Response HRB'"> [more] </a></td>
    <td><b>nidm:'Finite Impulse Response HRB': </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Gamma Difference HRF'"> [more] </a></td>
    <td><b>nidm:'Gamma Difference HRF': </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Gamma HRB'"> [more] </a></td>
    <td><b>nidm:'Gamma HRB': </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Gamma HRF'"> [more] </a></td>
    <td><b>nidm:'Gamma HRF': </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/288">#288</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Grand Mean Map'"> [more] </a></td>
    <td><b>nidm:'Grand Mean Map': </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Hemodynamic Response Function Basis'"> [more] </a></td>
    <td><b>nidm:'Hemodynamic Response Function Basis': </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Hemodynamic Response Function Derivative'"> [more] </a></td>
    <td><b>nidm:'Hemodynamic Response Function Derivative': </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Hemodynamic Response Function'"> [more] </a></td>
    <td><b>nidm:'Hemodynamic Response Function': </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/137">#137</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='NIDM Object Model'"> [more] </a></td>
    <td><b>nidm:'NIDM Object Model': </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/137">#137</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='SPM Results'"> [more] </a></td>
    <td><b>nidm:'SPM Results': </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/194">#194</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Spatial Model'"> [more] </a></td>
    <td><b>nidm:'Spatial Model': </b>FIXME</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/194">#194</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Spatially Global Model'"> [more] </a></td>
    <td><b>nidm:'Spatially Global Model': </b>FIXME</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/194">#194</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Spatially Local Model'"> [more] </a></td>
    <td><b>nidm:'Spatially Local Model': </b>FIXME</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/194">#194</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Spatially Regularized Model'"> [more] </a></td>
    <td><b>nidm:'Spatially Regularized Model': </b>FIXME</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='World Coordinate System'"> [more] </a></td>
    <td><b>nidm:'World Coordinate System': </b>&lt;undefined&gt;</td>
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
    <td>Under discussion at <a href="https://github.com/ISA-tools/stato/pull/28">ISA-tools/stato#28</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Arbitrarily Correlated Error'"> [more] </a></td>
    <td><b>nidm:'Arbitrarily Correlated Error': </b>&lt;undefined&gt; (editor: TN)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/ISA-tools/stato/pull/28">ISA-tools/stato#28</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Compound Symmetric Error'"> [more] </a></td>
    <td><b>nidm:'Compound Symmetric Error': </b>&lt;undefined&gt; (editor: TN)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/276">#276</a>, discussed in <a href="https://github.com/ISA-tools/stato/pull/23">ISA-tools/stato#23</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Contrast Estimation'"> [more] </a></td>
    <td><b>nidm:'Contrast Estimation': </b>The process of estimating a contrast from the estimated parameters of statistical model</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at: <a href="https://github.com/ISA-tools/stato/pull/23">ISA-tools/stato#23</a>
Range: Vector of integers not found.<br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Contrast Weights'"> [more] </a></td>
    <td><b>nidm:'Contrast Weights': </b>Vector defining the linear combination associated with a particular contrast. </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/ISA-tools/stato/pull/28">ISA-tools/stato#28</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Exchangeable Error'"> [more] </a></td>
    <td><b>nidm:'Exchangeable Error': </b>&lt;undefined&gt; (editor: TN)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/ISA-tools/stato/pull/28">ISA-tools/stato#28</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Independent Error'"> [more] </a></td>
    <td><b>nidm:'Independent Error': </b>&lt;undefined&gt; (editor: TN)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/ISA-tools/stato/pull/28">ISA-tools/stato#28</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Serially Correlated Error'"> [more] </a></td>
    <td><b>nidm:'Serially Correlated Error': </b>&lt;undefined&gt; (editor: TN)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/290">#290</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Coordinate Space'"> [more] </a></td>
    <td><b>nidm:'Coordinate Space': </b>An entity with spatial attributes (e.g., dimensions, units, and voxel-to-world mapping) that provides context to a SpatialImage (e.g., a StatisticMap)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Custom Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Custom Coordinate System': </b>&lt;undefined&gt;</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='MNI Coordinate System'"> [more] </a></td>
    <td><b>nidm:'MNI Coordinate System': </b>Coordinate system defined with reference to the MNI atlas</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/283">#283</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Peak'"> [more] </a></td>
    <td><b>nidm:'Peak': </b>Statistic defined at the peak-level in an excursion set. FIXME (now Peak instead of PeakStatistic)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Standardized Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Standardized Coordinate System': </b>Parent of all reference spaces except "Subject"</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Subject Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Subject Coordinate System': </b>Coordinate system defined by the subject brain (no spatial normalisation applied)</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Talairach Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Talairach Coordinate System': </b>Reference space defined by the dissected brain used for the Talairach and Tournoux atlas</td>
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
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='AFNI's drift Basis Order'"> [find issues/PR] </a></td>
    <td><b>afni:'AFNI's drift Basis Order': </b>The number of basis in the drift model</td>
    <td>afni:LegendrePolynomialDriftModel </td>
    <td>xsd:int </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='FSL's Drift Cut-off Period'"> [find issues/PR] </a></td>
    <td><b>fsl:'FSL's Drift Cut-off Period': </b>Full Width at Half Maximum in seconds of the Gaussian weight function used in the running line smoother</td>
    <td>fsl:GaussianRunningLineDriftModel </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='cluster Size In Voxels'"> [find issues/PR] </a></td>
    <td><b>nidm:'cluster Size In Voxels': </b>Number of voxels that make up the cluster</td>
    <td>nidm:NIDM_0000026 nidm:NIDM_0000070 </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/285">#285</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='grand Mean Scaling'"> [more] </a></td>
    <td><b>nidm:'grand Mean Scaling': </b>Binary flag defining whether the data was scaled. Specifically, "grand mean scaling" refers to multipliciation of every voxel in every scan by a common value.  Grand mean scaling is essential for first-level fMRI, to transform the arbitrary MRI units, but is generally not used with second level analyses</td>
    <td>nidm:NIDM_0000018 </td>
    <td>xsd:boolean </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='has Drift Model'"> [find issues/PR] </a></td>
    <td><b>nidm:'has Drift Model': </b>A property that associates a drift model to a design matrix (only used for first-level fMRI experiments)</td>
    <td>nidm:NIDM_0000019 </td>
    <td>nidm:NIDM_0000087 </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/288">#288</a>, naming previously discussed at: <a href="https://github.com/incf-nidash/nidm/pull/70">#70</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='masked Median'"> [more] </a></td>
    <td><b>nidm:'masked Median': </b>Median value considering only in-mask voxels. Useful diagnostic when computed on grand mean image when grandMeanScaling is TRUE, as the median should be close to targetIntensity</td>
    <td>nidm:NIDM_0000033 </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/291">#291</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='software Version'"> [more] </a></td>
    <td><b>nidm:'software Version': </b>Name and number that specifies the software version</td>
    <td>prov:SoftwareAgent </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/285">#285</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='target Intensity'"> [more] </a></td>
    <td><b>nidm:'target Intensity': </b>Value to which the grand mean of the Data was scaled (applies only if grandMeanScaling is true)</td>
    <td>nidm:NIDM_0000018 </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='SPM's Drift Cut-off Period'"> [find issues/PR] </a></td>
    <td><b>spm:'SPM's Drift Cut-off Period': </b>Discrete Cosine Transform basis cut-off, specified as period length in seconds and ensures that all basis elements will have period of this duration or longer</td>
    <td>spm:DCTDriftModel </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=expectedNumberOfClusters"> [find issues/PR] </a></td>
    <td><b>spm:expectedNumberOfClusters: </b>Expected number of clusters in an excursion set</td>
    <td>nidm:NIDM_0000068 </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=searchVolumeReselsGeometry"> [find issues/PR] </a></td>
    <td><b>spm:searchVolumeReselsGeometry: </b>Description of geometry of search volume.  As per Worsley et al. [ http://www.ncbi.nlm.nih.gov/pubmed/20408186 ], the first element is the Euler Characteristic of the search volume, the second element is twice the average caliper diameter, the third element is half the surface area, and the fourth element is the volume.  With the exception of the first element (which is a unitless integer) all quantities are in units of Resels</td>
    <td>nidm:NIDM_0000068 </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=smallestSignifClusterSizeInVerticesFDR05"> [find issues/PR] </a></td>
    <td><b>spm:smallestSignifClusterSizeInVerticesFDR05: </b>Smallest cluster size in vertices that are significant at a false discovery rate corrected alpha value of 0.05.  </td>
    <td>nidm:NIDM_0000068 </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=smallestSignifClusterSizeInVerticesFWE05"> [find issues/PR] </a></td>
    <td><b>spm:smallestSignifClusterSizeInVerticesFWE05: </b>Smallest cluster size in vertices significant at family-wise error rate corrected alpha value of 0.05</td>
    <td>nidm:NIDM_0000068 </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=smallestSignifClusterSizeInVoxelsFDR05"> [find issues/PR] </a></td>
    <td><b>spm:smallestSignifClusterSizeInVoxelsFDR05: </b>Smallest cluster size in voxels significant at false discovery rate corrected alpha value of 0.05.  </td>
    <td>nidm:NIDM_0000068 </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/green.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=smallestSignifClusterSizeInVoxelsFWE05"> [find issues/PR] </a></td>
    <td><b>spm:smallestSignifClusterSizeInVoxelsFWE05: </b>Smallest cluster size in voxels significant at family-wise error corrected alpha value of 0.05. 
</td>
    <td>nidm:NIDM_0000068 </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='user Specified Threshold Type'"> [find issues/PR] </a></td>
    <td><b>nidm:'user Specified Threshold Type': </b>Type of method used to define a threshold (e.g. statistic value, uncorrected P-value or corrected P-value) (editor: Discussed in https://github.com/incf-nidash/nidm/pull/150)</td>
    <td>nidm:NIDM_0000026 nidm:NIDM_0000034 </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/214">#214</a> and <a href="https://github.com/incf-nidash/nidm/pull/275">#275</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=dlh"> [more] </a></td>
    <td><b>fsl:dlh: </b>&lt;undefined&gt;</td>
    <td>nidm:NIDM_0000068 </td>
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
    <td>nidm:NIDM_0000068 </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/194">#194</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='dependence Spatial Model'"> [more] </a></td>
    <td><b>nidm:'dependence Spatial Model': </b>FIXME</td>
    <td>nidm:NIDM_0000023 </td>
    <td>nidm:NIDM_0000071 </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/294">#294</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='global Null Degree'"> [more] </a></td>
    <td><b>nidm:'global Null Degree': </b>&lt;undefined&gt;</td>
    <td>spm:KConjunctionInference </td>
    <td>xsd:int </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/281">#281</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='has HRF Basis'"> [more] </a></td>
    <td><b>nidm:'has HRF Basis': </b>&lt;undefined&gt;</td>
    <td>nidm:NIDM_0000019 </td>
    <td>nidm:NIDM_0000036 </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/292">#292</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='number Of Clusters'"> [more] </a></td>
    <td><b>nidm:'number Of Clusters': </b>&lt;undefined&gt;</td>
    <td>nidm:NIDM_0000025 </td>
    <td>xsd:int </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/137">#137</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='object Model'"> [more] </a></td>
    <td><b>nidm:'object Model': </b>&lt;undefined&gt;</td>
    <td>prov:Bundle </td>
    <td>nidm:NIDM_0000057 </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='search Volume In Voxels'"> [find issues/PR] </a></td>
    <td><b>nidm:'search Volume In Voxels': </b>Total number of voxels within the search volume</td>
    <td>nidm:NIDM_0000068 </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/293">#293</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='statistic Type'"> [more] </a></td>
    <td><b>nidm:'statistic Type': </b>&lt;undefined&gt;</td>
    <td>nidm:NIDM_0000014 nidm:NIDM_0000076 </td>
    <td>obo:STATO_0000039 </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/194">#194</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='variance Spatial Model'"> [more] </a></td>
    <td><b>nidm:'variance Spatial Model': </b>FIXME</td>
    <td>nidm:NIDM_0000023 </td>
    <td>nidm:NIDM_0000071 </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/137">#137</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='version'"> [more] </a></td>
    <td><b>nidm:'version': </b>&lt;undefined&gt;</td>
    <td>prov:Bundle </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/293">#293</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='with Estimation Method'"> [more] </a></td>
    <td><b>nidm:'with Estimation Method': </b>FIXME</td>
    <td>nidm:NIDM_0000056 </td>
    <td>obo:STATO_0000119 </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/red.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/275">#275</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=searchVolumeInResels"> [more] </a></td>
    <td><b>spm:searchVolumeInResels: </b>Total number of resels within the search volume</td>
    <td>nidm:NIDM_0000068 </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/ISA-tools/stato/pull/38">ISA-tools/stato#38</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='p Value FWER'"> [more] </a></td>
    <td><b>nidm:'p Value FWER': </b>"A quantitative confidence value resulting from a multiple testing error correction method which adjusts the p-value used as input to control for Type I error in the context of multiple pairwise tests"(same as: <a href=This definition is from OBI. Please update this note if the definition is modified.>This definition is from OBI. Please update this note if the definition is modified.</a>)</td>
    <td>nidm:NIDM_0000026 nidm:NIDM_0000034 nidm:NIDM_0000062 nidm:NIDM_0000070 </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/yellow.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/ISA-tools/stato/pull/38">ISA-tools/stato#38</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='p Value Uncorrected'"> [more] </a></td>
    <td><b>nidm:'p Value Uncorrected': </b>A p-value reported without correction for multiple testing.        </td>
    <td>nidm:NIDM_0000026 nidm:NIDM_0000034 nidm:NIDM_0000062 nidm:NIDM_0000070 </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at: <a href="https://github.com/incf-nidash/nidm/pull/270">#270</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=coordinateInVoxels"> [more] </a></td>
    <td><b>fsl:coordinateInVoxels: </b>Coordinate along the first dimension in voxels. (This definition needs to be re-worked as this term was renamed from coordinate1 to coordinate in https://github.com/incf-nidash/nidm/issues/270)</td>
    <td>nidm:NIDM_0000015 </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='cluster Size In Vertices'"> [find issues/PR] </a></td>
    <td><b>nidm:'cluster Size In Vertices': </b>Number of vertices that make up the cluster</td>
    <td>nidm:NIDM_0000026 nidm:NIDM_0000070 </td>
    <td>xsd:positiveInteger </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='contrast Name'"> [find issues/PR] </a></td>
    <td><b>nidm:'contrast Name': </b>Name of the contrast</td>
    <td>nidm:NIDM_0000002 nidm:NIDM_0000014 nidm:NIDM_0000076 </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at: <a href="https://github.com/incf-nidash/nidm/pull/270">#270</a> and <a href="https://github.com/incf-nidash/nidm/pull/145">#145</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='coordinate'"> [more] </a></td>
    <td><b>nidm:'coordinate': </b>Coordinate along the first dimension in voxel units. (This definition needs to be re-worked as this term was renamed from coordinate1 to coordinate in https://github.com/incf-nidash/nidm/issues/270)</td>
    <td>nidm:NIDM_0000015 </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at: <a href="https://github.com/incf-nidash/nidm/pull/146">#146</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='dimensions In Voxels'"> [more] </a></td>
    <td><b>nidm:'dimensions In Voxels': </b>Dimensions of some N-dimensional data</td>
    <td>nidm:NIDM_0000016 </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/277">#277</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='effect Degrees Of Freedom'"> [more] </a></td>
    <td><b>nidm:'effect Degrees Of Freedom': </b>Degrees of freedom of the effect</td>
    <td>nidm:NIDM_0000076 </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='equivalent ZStatistic'"> [find issues/PR] </a></td>
    <td><b>nidm:'equivalent ZStatistic': </b>Statistic value transformed into Z units; the output of a process which takes a non-normal statistic and transforms it to an equivalent z score</td>
    <td>nidm:NIDM_0000062 </td>
    <td>xsd:float </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/277">#277</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='error Degrees Of Freedom'"> [more] </a></td>
    <td><b>nidm:'error Degrees Of Freedom': </b>Degrees of freedom of the error</td>
    <td>nidm:NIDM_0000076 </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/282">#282</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='has Cluster Labels Map'"> [more] </a></td>
    <td><b>nidm:'has Cluster Labels Map': </b>A map whose value at each location denotes cluster membership. Each cluster is denoted by a different integer</td>
    <td>nidm:NIDM_0000025 </td>
    <td>nidm:NIDM_0000008 </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='in World Coordinate System'"> [more] </a></td>
    <td><b>nidm:'in World Coordinate System': </b>Type of coordinate system</td>
    <td>nidm:NIDM_0000016 </td>
    <td>nidm:NIDM_0000081 </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/173">#173</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='noise FWHM'"> [more] </a></td>
    <td><b>nidm:'noise FWHM': </b>Estimated Full Width at Half Maximum of the noise distribution</td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/130">#130</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='random Field Stationarity'"> [more] </a></td>
    <td><b>nidm:'random Field Stationarity': </b>Is the random field assumed to be stationary across the entire search volume?</td>
    <td>nidm:NIDM_0000068 </td>
    <td>xsd:boolean </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q='search Volume In Vertices'"> [find issues/PR] </a></td>
    <td><b>nidm:'search Volume In Vertices': </b>Total number of vertices within the search volume</td>
    <td>nidm:NIDM_0000068 </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=expectedNumberOfVerticesPerCluster"> [find issues/PR] </a></td>
    <td><b>spm:expectedNumberOfVerticesPerCluster: </b>Expected number of vertices in a cluster</td>
    <td>nidm:NIDM_0000068 </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td><a href="https://github.com/incf-nidash/nidm//issues?&q=expectedNumberOfVoxelsPerCluster"> [find issues/PR] </a></td>
    <td><b>spm:expectedNumberOfVoxelsPerCluster: </b>Expected number of voxels in a cluster</td>
    <td>nidm:NIDM_0000068 </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/293">#293</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=hasMaximumIntensityProjection"> [more] </a></td>
    <td><b>spm:hasMaximumIntensityProjection: </b>Maximum intensity projection of a map</td>
    <td>nidm:NIDM_0000025 </td>
    <td>dctype:Image </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at: <a href="https://github.com/incf-nidash/nidm/pull/214">#214</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=noiseFWHMInUnits"> [more] </a></td>
    <td><b>spm:noiseFWHMInUnits: </b>Estimated Full Width at Half Maximum of the noise distribution in world units</td>
    <td>nidm:NIDM_0000068 </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at: <a href="https://github.com/incf-nidash/nidm/pull/214">#214</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=noiseFWHMInVertices"> [more] </a></td>
    <td><b>spm:noiseFWHMInVertices: </b>Estimated Full Width at Half Maximum of the noise distribution in world vertices</td>
    <td>nidm:NIDM_0000054 </td>
    <td></td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at: <a href="https://github.com/incf-nidash/nidm/pull/214">#214</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=noiseFWHMInVoxels"> [more] </a></td>
    <td><b>spm:noiseFWHMInVoxels: </b>Estimated Full Width at Half Maximum of the noise distribution in voxels</td>
    <td>nidm:NIDM_0000068 </td>
    <td>xsd:string </td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/275">#275</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q=reselSize"> [more] </a></td>
    <td><b>spm:reselSize: </b>Size of one resel in voxels or vertices</td>
    <td>nidm:NIDM_0000068 </td>
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
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Colin27 Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Colin27 Coordinate System': </b>Coordinate system defined by the "stereotaxic average of 27 T1-weighted MRI scans of the same individual"</td>
    <td>nidm:NIDM_0000075</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Icbm Mni152 Linear Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Icbm Mni152 Linear Coordinate System': </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, linearly transformed to Talairach space"</td>
    <td>nidm:NIDM_0000051</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Icbm Mni152 Non Linear2009a Asymmetric Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Icbm Mni152 Non Linear2009a Asymmetric Coordinate System': </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, non-linearly transformed to MNI152 linear space"</td>
    <td>nidm:NIDM_0000051</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Icbm Mni152 Non Linear2009a Symmetric Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Icbm Mni152 Non Linear2009a Symmetric Coordinate System': </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, non-linearly transformed to MNI152 linear space"</td>
    <td>nidm:NIDM_0000051</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Icbm Mni152 Non Linear2009b Asymmetric Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Icbm Mni152 Non Linear2009b Asymmetric Coordinate System': </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, non-linearly transformed to MNI152 linear space"</td>
    <td>nidm:NIDM_0000051</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Icbm Mni152 Non Linear2009b Symmetric Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Icbm Mni152 Non Linear2009b Symmetric Coordinate System': </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, non-linearly transformed to MNI152 linear space"</td>
    <td>nidm:NIDM_0000051</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Icbm Mni152 Non Linear2009c Asymmetric Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Icbm Mni152 Non Linear2009c Asymmetric Coordinate System': </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, non-linearly transformed to MNI152 linear space"</td>
    <td>nidm:NIDM_0000051</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Icbm Mni152 Non Linear2009c Symmetric Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Icbm Mni152 Non Linear2009c Symmetric Coordinate System': </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, non-linearly transformed to MNI152 linear space"</td>
    <td>nidm:NIDM_0000051</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Icbm Mni152 Non Linear6th Generation Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Icbm Mni152 Non Linear6th Generation Coordinate System': </b>Coordinate system defined by the "average of 152 T1-weighted MRI scans, linearly and non-linearly (6 iterations) transformed to form a symmetric model in Talairach space"</td>
    <td>nidm:NIDM_0000051</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Icbm452 Air Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Icbm452 Air Coordinate System': </b>Coordinate system defined by the "average of 452 T1-weighted MRIs of normal young adult brains" with "linear transforms of the subjects into the atlas space using a 12-parameter affine transformation"</td>
    <td>nidm:NIDM_0000051</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Icbm452 Warp5 Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Icbm452 Warp5 Coordinate System': </b>Coordinate system defined by the "average of 452 T1-weighted MRIs of normal young adult brains" "based on a 5th order polynomial transformation into the atlas space"</td>
    <td>nidm:NIDM_0000051</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Ixi549 Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Ixi549 Coordinate System': </b>Coordinate system defined by the average of the "549 [...] subjects from the IXI dataset" linearly transformed to ICBM MNI 452</td>
    <td>nidm:NIDM_0000051</td>
</tr>
<tr>
    <td><img src="../../../doc/content/specs/img/orange.png?raw=true"/>  </td>
    <td>Under discussion at <a href="https://github.com/incf-nidash/nidm/pull/284">#284</a><br/><a href="https://github.com/incf-nidash/nidm//issues?&q='Mni305 Coordinate System'"> [more] </a></td>
    <td><b>nidm:'Mni305 Coordinate System': </b>Coordinate system defined by the "average of 305 T1-weighted MRI scans, linearly transformed to Talairach space"</td>
    <td>nidm:NIDM_0000051</td>
</tr>
</table>