[![alt text](https://www.incf.org/themes/incf/images/logo.svg "INCF")](http://incf.org) [![Build Status](https://travis-ci.org/incf-nidash/nidm-specs.png?branch=master)](https://travis-ci.org/incf-nidash/nidm-specs) 

# NeuroImaging Data Model (NIDM)

A model to represent neuroimaging data with their metadata in support of data sharing and reuse! 

NIDM is currently made up of:
 - 1 released model
   - [**NIDM-Results**](#nidm-results): harmonised representation of mass univariate neuroimaging results (such as fMRI)
 - 2 models under development
   - [**NIDM-Workflows**](#nidm-workflows): representation of neuroimaging workflows
   - [**NIDM-Experiment**](#nidm-experiment): representation of neuroimaging raw data


![alt text](doc/content/specs/img/nidm-upper-layer.png)

NIDM is defined as an extension the [W3C PROV](http://www.w3.org/TR/prov-primer/) standard for provenance.

## NIDM-Results

### Documentation
The NIDM-Results specification is available at: http://nidm.nidash.org/specs/nidm-results.html

### Citation
Camille Maumet, Tibor Auer, Alexander Bowring, Gang Chen, Samir Das, Guillaume Flandin, Satrajit Ghosh, Tristan Glatard, Krzysztof J. Gorgolewski, Karl G. Helmer, Mark Jenkinson, David B. Keator, B. Nolan Nichols, Jean-Baptiste Poline, Richard Reynolds, Vanessa Sochat, Jessica Turner & Thomas E. Nichols. **Sharing brain mapping statistical results with the neuroimaging data model**. *Scientific Data*, Nature Publishing Group, 2016, 3. doi: [10.1038/sdata.2016.102](doi.org/10.1038/sdata.2016.102)

### Tools
 * NIDM-Results I/O (reference implementations): [Python library](https://github.com/incf-nidash/nidmresults), [Matlab library](https://www.artefact.tk/software/matlab/provenance/)
 * Export to NIDM-Results from neuroimaging tools: [FSL to NIDM-Results](https://github.com/incf-nidash/nidmresults-fsl), [SPM to NIDM-Results](https://github.com/incf-nidash/nidmresults-spm)
 * NIDM-Results viewers: [SPM viewer](https://github.com/incf-nidash/nidmresults-spmhtml), [FSL viewer](https://github.com/incf-nidash/nidmresults-fslhtml), [NeuroVault viewer](https://github.com/vsoch/nidmviewer), [Javascript viewer](https://github.com/incf-nidash/nidmviewer).

### Getting Started
Interested in using NIDM-Results? See the [get started with NIDM](http://nidm.nidash.org/getting-started/) page where you will find how to publish your fMRI results from SPM and FSL & upload to NeuroVault.

### Contributing
Thanks for you interest in contributing to NIDM-Results! If you would like to submit an update or outline an issue with the NIDM-Results specification, please [submit an issue](https://github.com/incf-nidash/nidm-specs/issues/new) or [email us](mailto:incf-nidash-nidm<AT>googlegroups<DOT>com). You can also join our [weekly calls](#nidm-weekly-calls)!

## NIDM-Workflows

### Contributing
Contributions to NIDM-Workflows are gathered on the work-in-progress [NIDM-Worklows specification](https://docs.google.com/document/d/1OjdvKyjSuLXoPrmH18SPj2Fe1bvkomQjowY7TG-F8MQ/edit). Please feel free to commment directly on this document or [submit an issue](https://github.com/incf-nidash/nidm-specs/issues/new). . You can also join our [weekly calls](#nidm-weekly-calls)!

## NIDM-Experiment

### Preview 

## Contributing
We use the [incf-nidash GitHub](https://github.com/incf-nidash/) organisation and  to foster collaboration among the developers working on NIDM:
 * All components: the [current repository](https://github.com/cmaumet/nidm) is used to foster discussions on all NIDM components. See our issues on [NIDM-Results](https://github.com/incf-nidash/nidm/labels/nidm-results), [NIDM-Workflows](https://github.com/incf-nidash/nidm/labels/nidm-workflows), [NIDM-Experiment](https://github.com/incf-nidash/nidm/labels/nidm-experiment) or the [full list](https://github.com/incf-nidash/nidm/issues) of open questions/comments. 
 * NIDM-Workflows: 

 * NIDM-Experiment: [NIDM-Experiment python library](https://github.com/incf-nidash/pyNIDM)


## NIDM weekly calls
We meet every week by videoconference on Mondays at 8-9am PDT / 11am-12pm EDT / 4-5pm BST. The group is always open to new contributors interested in neuroimaging data sharing. To join the call or to ask any question, please email us at incf-nidash-nidm@googlegroups.com. [Meeting minutes](https://drive.google.com/drive/folders/0B3KAfE6L3piOMWsyc0FyU1JWY3c?usp=sharing).

## Other resources
 * [NIDM website](http://nidm.nidash.org)
 * [NIDASH shared Google folder](https://drive.google.com/drive/folders/0B-BLof5_SOh8bWR3UDE4WTdELXM?usp=sharing)
 * [Abstracts](https://drive.google.com/drive/folders/0B3KAfE6L3piOTExkaWdlaVZGaHc)

## Acknoledgments
The NIDM working group is a collaboration supported by the [INCF](http://www.incf.org).
