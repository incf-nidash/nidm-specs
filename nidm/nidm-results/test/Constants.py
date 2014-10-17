#!/usr/bin/env python
''' Definition of constants

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2014
'''

from rdflib import Namespace

PROV = Namespace('http://www.w3.org/ns/prov#')
NIDM = Namespace('http://www.incf.org/ns/nidash/nidm#')
SPM = Namespace('http://www.incf.org/ns/nidash/spm#')
FSL = Namespace('http://www.incf.org/ns/nidash/fsl#')
RDFS = Namespace('http://www.w3.org/2000/01/rdf-schema#')
CRYPTO = Namespace('http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions#')
DCT = Namespace('http://purl.org/dc/terms/')
# This is a workaround to avoid issue with "#" in base prefix as 
# described in https://github.com/RDFLib/rdflib/issues/379,
# When the fix is introduced in rdflib this line will be replaced by:
# OWL = Namespace('http://www.w3.org/2002/07/owl#')
OWL = Namespace('http://www.w3.org/2002/07/owl')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')

OBO = Namespace("http://purl.obolibrary.org/obo/")
IAO = Namespace("http://purl.obolibrary.org/obo/iao.owl#")

IAO_EXAMPLE = IAO['IAO_0000112']

OBO_PENDING_FINAL = OBO['IAO_0000125']
OBO_METADATA_COMPLETE = OBO['IAO_0000120']
OBO_METADATA_INCOMPLETE = OBO['IAO_0000123']
OBO_REQUIRES_DISCUSSION = OBO['IAO_0000428']
OBO_UNCURATED = OBO['IAO_0000124']
OBO_TO_BE_REPLACED = OBO['IAO_0000423']
OBO_READY = OBO['IAO_0000122']

HAS_CURATION_STATUS = OBO['IAO_0000114']