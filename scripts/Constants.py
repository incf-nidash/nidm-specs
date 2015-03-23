#!/usr/bin/env python
''' Definition of constants

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2014
'''

from rdflib import Namespace

PROV = Namespace('http://www.w3.org/ns/prov#')
NIDM = Namespace('http://www.incf.org/ns/nidash/nidm#')

NIDM_EXPERIMENT = Namespace('http://purl.org/nidash/nidm/experiment#')

NIIRI = Namespace('http://iri.nidash.org/')
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

OBO_URL = "http://purl.obolibrary.org/obo/"
OBO = Namespace(OBO_URL)

OBO_EXAMPLE = OBO['IAO_0000112']
OBO_TERM_EDITOR = OBO['IAO_0000117']
OBO_EDITOR_NOTE = OBO['IAO_0000116']

OBO_PENDING_FINAL = OBO['IAO_0000125']
OBO_METADATA_COMPLETE = OBO['IAO_0000120']
OBO_METADATA_INCOMPLETE = OBO['IAO_0000123']
OBO_REQUIRES_DISCUSSION = OBO['IAO_0000428']
OBO_UNCURATED = OBO['IAO_0000124']
OBO_TO_BE_REPLACED = OBO['IAO_0000423']
OBO_READY = OBO['IAO_0000122']
OBO_DEFINITION = OBO['IAO_0000115']

HAS_CURATION_STATUS = OBO['IAO_0000114']

STATO_OLS = OBO['STATO_0000370']
STATO_OLS_STR = str(STATO_OLS).replace(OBO_URL, "obo:")
# TODO: labels should be grabbed automatically from the corresponding owl file
STATO_OLS_LABEL = "obo:'ordinary least squares estimation'"
STATO_GLS = OBO['STATO_0000372']
STATO_GLS_STR = str(STATO_GLS).replace(OBO_URL, "obo:")
STATO_GLS_LABEL = "obo:'generalized least squares estimation'"