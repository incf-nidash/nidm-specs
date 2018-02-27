[![alt text](https://www.incf.org/themes/incf/images/logo.svg "INCF")](http://incf.org) [![Build Status](https://travis-ci.org/incf-nidash/nidm-specs.png?branch=master)](https://travis-ci.org/incf-nidash/nidm-specs) 

# NeuroImaging Data Model (NIDM)

A model to represent all neuroimaging data and metadata! 

NIDM provides structured representations of neuroimaging data with the goal of supporting data sharing in the neuroimaging community. 

![alt text](https://raw.githubusercontent.com/cmaumet/nidm/contributing/doc/content/specs/img/nidm-layer-cake.png "NIDM components")

NIDM is currently made up of 3 components:
 - **NIDM-Results**: software-agnostic representation of GLM results
 - **NIDM-Workflows**: representation of neuroimaging workflows
 - **NIDM-Experiment**: representation of neuroimaging raw data

and is defined as an extension the [W3C PROV](http://www.w3.org/TR/prov-primer/) standard for provenance.

## Getting Started

Interested in using NIDM? See the [get started with NIDM](http://nidm.nidash.org/getting-started/) page where you will find how to publish your fMRI results from SPM and FSL & upload to NeuroVault.

We use the [incf-nidash GitHub](https://github.com/incf-nidash/) organisation and [NIDASH shared Google folder](https://drive.google.com/drive/folders/0B-BLof5_SOh8bWR3UDE4WTdELXM?usp=sharing) to foster collaboration among the developers working on NIDM:
 * All components: the [current repository](https://github.com/cmaumet/nidm) is used to foster discussions on all NIDM components. See our issues on [NIDM-Results](https://github.com/incf-nidash/nidm/labels/nidm-results), [NIDM-Workflows](https://github.com/incf-nidash/nidm/labels/nidm-workflows), [NIDM-Experiment](https://github.com/incf-nidash/nidm/labels/nidm-experiment) or the [full list](https://github.com/incf-nidash/nidm/issues) of open questions/comments. 
 * NIDM-Workflows: Comment on work-in-progress [NIDM-Worklows specification](https://docs.google.com/document/d/1OjdvKyjSuLXoPrmH18SPj2Fe1bvkomQjowY7TG-F8MQ/edit).

You can also contribute to our ecosystem of tools to read/write/interact with NIDM, including:
 * NIDM-Results: [NIDM-Results python library](https://github.com/incf-nidash/nidmresults), [FSL to NIDM-Results](https://github.com/incf-nidash/nidmresults-fsl), [SPM to NIDM-Results](https://github.com/incf-nidash/nidmresults-spm), [View NIDM-Results in SPM](https://github.com/incf-nidash/nidmresults-spmhtml), [View NIDM-Results in FSL](https://github.com/incf-nidash/nidmresults-fslhtml)
 * NIDM-Experiment: [NIDM-Experiment python library](https://github.com/incf-nidash/pyNIDM)


## Contributing

Thanks for your interest in contributing to NIDM! 

The NIDM working group is a collaboration supported by the [INCF](http://www.incf.org). We meet every week by videoconference on Mondays at 8:30-9:30am PDT / 11:30am-12:30pm EDT / 4:30-5:30pm BST. The group is always open to new contributors who are interested in neuroimaging data sharing. To join the call or to ask any question, please email us at incf-nidash-nidm@googlegroups.com. There are many ways to contribute. To get started, take a look at our [issue tracker](https://github.com/incf-nidash/nidm/issues).

## Other resources
 * [NIDM specifications](http://nidm.nidash.org)
 * [NIDM call meeting minutes](https://drive.google.com/drive/folders/0B3KAfE6L3piOMWsyc0FyU1JWY3c?usp=sharing)
 * [NIDM abstracts in conferences](https://drive.google.com/drive/folders/0B3KAfE6L3piOTExkaWdlaVZGaHc)

