"""
Create csv file listing preferred prefixes for NIDM terms
@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2015
"""

import os
import sys
import glob

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)
NIDMPATH = os.path.join(NIDMRESULTSPATH, os.pardir)

# Append parent script directory to path
sys.path.append(os.path.join(NIDMRESULTSPATH, os.pardir, os.pardir, "scripts"))
from nidmresults.owl.owl_reader import *
from nidmresults.objects.constants_rdflib import *

logging.basicConfig(filename='debug.log', level=logging.DEBUG, filemode='w')
logger = logging.getLogger(__name__)


def main(owl=None):
    if owl is None:
        owl = os.path.join(NIDMRESULTSPATH, "terms",
                           "nidm-results.owl")

    owl_imports = glob.glob(
        os.path.join(os.path.dirname(owl),
                     os.pardir, os.pardir, "imports", '*.ttl'))

    owl_reader = OwlReader(owl, import_owl_files=owl_imports)

    owl_file = os.path.basename(owl)
    if "_" in owl_file:
        version = "_" + owl_file.split("_")[1].replace(".owl", "")
    else:
        version = ""

    owl_reader.prefixes_as_csv(os.path.join(os.path.dirname(owl),
                               "prefixes" + version + ".csv"))
    owl_reader.prefixes_in_owl_file()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        owl = sys.argv[1]
    else:
        owl = None

    main(owl)
