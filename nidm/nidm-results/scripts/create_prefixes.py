"""
Create csv file listing preferred prefixes for NIDM terms
@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2015
"""

import os
import sys

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)
NIDMPATH = os.path.join(NIDMRESULTSPATH, os.pardir)

# Append parent script directory to path
sys.path.append(os.path.join(NIDMRESULTSPATH, os.pardir, os.pardir, "scripts"))
from OwlReader import *
from Constants import *

logging.basicConfig(filename='debug.log', level=logging.DEBUG, filemode='w')
logger = logging.getLogger(__name__)


def main():
    owl_reader = OwlReader(os.path.join(NIDMRESULTSPATH, "terms",
                           "nidm-results.owl"))
    owl_reader.prefixes_as_csv(os.path.join(NIDMRESULTSPATH, "terms",
                               "prefixes.csv"))

if __name__ == '__main__':
    main()
