#!/usr/bin/env python
"""
REDCap Data Dictionary to OWL Converter
=======================================
This script provides a conversion utility for modeling REDCap Data
Dictionaries as an OWL Ontology, where instances are specific implementations
of a given REDCap Form.
"""
__author__ = 'Nolan Nichols <https://orcid.org/0000-0003-1099-3328>'
import os
import csv
import sys
import hashlib

import rdflib

verbose = None

ns = dict(nidm=rdflib.Namespace('http://purl.org/nidash/nidm/'),
          owl=rdflib.OWL)


def datatype_property(term):
    triple = [term,
              rdflib.RDF.term('type'),
              rdflib.OWL.term('DatatypeProperty')]
    return triple


def rdfs_label(term, label):
    triple = [term,
              rdflib.RDFS.term('label'),
              rdflib.Literal(label)]
    return triple


def header_to_owl(header):
    nidm = ns.get('nidm')
    g = rdflib.Graph()
    [g.bind(k, v) for k, v in ns.iteritems()]
    for idx, prop in enumerate(header):
        term = nidm.term('nidm_{}'.format(hashlib.sha1(prop).hexdigest()))
        g.add(datatype_property(term))
        g.add(rdfs_label(term, prop))
    return g


def main(args=None):
    with open(args.input, mode='rb') as fi:
        csvreader = csv.reader(fi)
        rows = list(csvreader)
        hdr = rows.pop(0)
        fi.close()
    g = header_to_owl(hdr)
    print g.serialize(args.output, format='turtle')


if __name__ == "__main__":
    import argparse

    formatter = argparse.RawDescriptionHelpFormatter
    default = 'default: %(default)s'
    parser = argparse.ArgumentParser(prog="file_name.py",
                                     description=__doc__,
                                     formatter_class=formatter)
    parser.add_argument('-i', '--input',
                        required=True,
                        help="Input REDCap data dictionary as a csv file")
    parser.add_argument('-o', '--output',
                        default='redcap.owl',
                        help="Output file in turtle OWL format. {}".format(default))
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='Enable verbose {}'.format(default))
    args = parser.parse_args()
    verbose = args.verbose
    sys.exit(main(args=args))