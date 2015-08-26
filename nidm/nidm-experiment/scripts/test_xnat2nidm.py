#!/usr/bin/env python
import os
import argparse

import rdflib
from xnat2nidm import *

args = argparse.Namespace()
args.config = os.path.abspath('xnat-central.cfg')
#args.experimentsdir = '/tmp/experiments'
args.experimentsdir = '/tmp/experiments'
args.session_id = 'CENTRAL_E03925'
args.num_extract = 1

config = get_config(args.config)
session = get_xnat_session(config)
extract_experiment_xml(config, session, args.experimentsdir, args.session_id, args.num_extract)

# extract info from the experiment XML files
experiments = get_experiments_dir_info(config, args.experimentsdir)
all_scans = get_experiments_dir_scan_info(config, args.experimentsdir)

# Get out configured graph
g = initialize_graph()

# Experiment
experiment = experiments[0]

# Create out investigation level
g = create_investigation_level(experiment, g)

# Create session level
single_experiment_scans = all_scans[0]
g = create_session_level(experiment, single_experiment_scans, g)

# Create run level
for scan in single_experiment_scans:
    g = create_run_level(scan, g)

print g.serialize(format='turtle')

query = 'SELECT DISTINCT ?series_description WHERE {?scan xnat:series_description ?series_description .}'
print
print "Example Query for Series Descriptions"
print query
print
result = g.query(query)
print result.serialize(format='csv')

g.serialize('{}.ttl'.format(args.session_id), format='turtle')
