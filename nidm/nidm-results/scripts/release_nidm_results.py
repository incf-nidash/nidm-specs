#!/usr/bin/env python
''' Create a NIDM-Results release including:
 - copy the owl file to the release directory
 - merge all the import owl import files
 - update the examples address
 - create a git tag

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2015
'''

import logging
import os
from rdflib.compare import *
import sys
import shutil

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)
NIDMPATH = os.path.join(NIDMRESULTSPATH, os.pardir)

# Append parent script directory to path
sys.path.append(os.path.join(NIDMRESULTSPATH, os.pardir, os.pardir, "scripts"))
from Constants import *

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TERMS_FOLDER = os.path.join(NIDMRESULTSPATH, 'terms')
RELEASED_TERMS_FOLDER = os.path.join(TERMS_FOLDER, "releases")


def main(nidm_original_version):
    nidm_version = nidm_original_version.replace(".", "")

    owl_file = os.path.join(TERMS_FOLDER, 'nidm-results.owl')
    assert os.path.exists(owl_file)

    # Copy the owl file to the release folder
    release_owl_file = os.path.join(RELEASED_TERMS_FOLDER,
                                    "nidm_results_%s.owl" % (nidm_version))
    shutil.copyfile(owl_file, release_owl_file)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        nidm_version = sys.argv[1]
    else:
        raise Exception("Error: missing version number for NIDM release")

    main(nidm_version)
