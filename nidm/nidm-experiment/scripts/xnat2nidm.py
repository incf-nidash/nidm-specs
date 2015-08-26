#!/usr/bin/env python
"""
Prototypical XNAT Converstion to NIDM
"""
__author__ = "Nolan Nichols <http://orcid.org/0000-0003-1099-3328>"

import os
import glob
import json
import hashlib
import tempfile
import argparse

import rdflib
import dateutil
import requests
import pandas as pd
from lxml import etree

# Verbose setting for cli
verbose = None

# Define global namespace for parsing XNAT XML files
ns = {'xnat': 'http://nrg.wustl.edu/xnat'}

# Define global format to be used in XNAT requests
return_format = '?format=csv'


def get_config(config_file):
    """
    Get a json configuration in pyXNAT format
    :param config_file: str
    :return: dict
    """
    path = os.path.abspath(config_file)
    with open(path, 'rb') as fi:
        config = json.load(fi)
    # Include an API key in conf
    config.update(api=config['server'] + '/data')
    if verbose:
        print("Getting configurtion file: {0}".format(path))
    return config


def get_collections(config):
    """
    Get a dictionary of lambda functions that create collection URLs
    :param config: dict
    :return: dict
    """
    server = config['api']
    collections = dict(projects=lambda: server + '/projects',
                       subjects=lambda x: server + '/{0}/subjects'.format(x),
                       experiments=lambda: server + '/experiments')
    if verbose:
        print("Getting collections configuration...")
    return collections


def get_entities(config):
    """
    Get a dictionary of lambda functions that create entity URLs
    :param config: dict
    :return: dict
    """
    server = config['api']
    entities = dict(project=lambda project: server + '/projects/{0}'.format(project),
                    subject=lambda project, subject: server + '/{0}/subjects/{1}'.format(project, subject),
                    experiment=lambda experiment: server + '/experiments/{0}'.format(experiment),
                    scan=lambda experiment, scan: server + '/experiments/{0}/scans/{1}'.format(experiment, scan))
    if verbose:
        print("Getting entities configuration...")
    return entities


def get_xnat_session(config):
    """
    Get a requests.session instance from the config

    :return: requests.session
    """
    jsessionid = ''.join([config['api'], '/JSESSIONID'])
    session = requests.session()
    session.auth = (config['user'], config['password'])
    session.get(jsessionid)
    if verbose:
        print("Getting an XNAT session using: {0}".format(jsessionid))
    return session


def write_experiments(config, session):
    """
    Write out a csv file representing all the experiments in the given XNAT
    session.

    :param config: dict
    :param session: requests.session
    :return: str
    """
    experiments_filename = tempfile.mktemp()
    collections = get_collections(config)
    experiments = session.get(collections.get('experiments')() + return_format)
    with open(experiments_filename, 'w') as fi:
        fi.flush()
        fi.write(experiments.text)
        fi.close()
    if verbose:
        print("Writing list of experiment ids to temp: {0}".format(experiments_filename))
    return experiments_filename


def extract_experiment_xml(config, session, experiment_dir, session_id=None, extract=None):
    """
    Open an experiments csv file, then extract the XML representation,
    and write it to disk.

    :param config: dict
    :param session: requests.session
    :param experiment_dir: str
    :param session_id: str
    :param extract: int
    :return: str
    """
    entities = get_entities(config)
    experiments_file = write_experiments(config, session)
    # make sure the output directory exists and is empty
    outdir = os.path.abspath(experiment_dir)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    else:
        [os.remove(f) for f in glob.glob(os.path.join(outdir, '*'))]
    df_experiments = pd.read_csv(experiments_file)
    if not extract:
        if verbose:
            print("Running XML extraction for all sessions: {0} Total".format(df_experiments.shape[0]))
        extract = df_experiments.shape[0]
    if session_id:
        df_experiments = df_experiments[df_experiments.ID == session_id]
    experiment_ids = df_experiments.ID[:extract]
    experiment_files = list()
    for idx, experiment_id in experiment_ids.iteritems():
        experiment = session.get(entities.get('experiment')(experiment_id) + return_format)
        experiment_file = os.path.join(outdir, '{0}.xml'.format(experiment_id))
        experiment_files.append(experiment_file)
        with open(experiment_file, 'w') as fi:
            fi.flush()
            fi.write(experiment.text)
            fi.close()
        if verbose:
            num = idx + 1
            print("Writing XML file {0} of {1} to: {2}".format(num, extract, experiment_file))
    return experiment_files


def get_experiment_info(config, experiment_xml_file):
    """
    Extract basic information from the experiment xml file and return a
    dictionary

    :param experiment_xml_file: str
    :return: dict
    """
    # Parse the XML file.
    xml = etree.parse(experiment_xml_file)
    root = xml.getroot()

    # Gather info from Experiment XML file.
    project_id = root.attrib.get('project')
    experiment_id = root.attrib.get('ID')
    visit_id = root.attrib.get('visit_id')
    session_type = root.attrib.get('session_type')
    uid = root.attrib.get('UID')
    experiment_label = root.attrib.get('label')
    # For datetime convert to proper type
    experiment_date = root.find('./xnat:date', namespaces=ns).text
    experiment_time = root.find('./xnat:time', namespaces=ns).text
    experiment_datetime = dateutil.parser.parse(' '.join([experiment_date, experiment_time]))
    acquisition_site = root.find('./xnat:acquisition_site', namespaces=ns).text
    subject_id = root.find('./xnat:subject_ID', namespaces=ns).text
    manufactuer = root.find('./xnat:scanner', namespaces=ns).attrib.get('manufacturer')
    model = root.find('./xnat:scanner', namespaces=ns).attrib.get('model')

    # Create URIRef objects for primary objects.
    entities = get_entities(config)
    project_uri = rdflib.URIRef(entities['project'](project_id))
    subject_uri = rdflib.URIRef(entities['subject'](project_id, subject_id))
    experiment_uri = rdflib.URIRef(entities['experiment'](experiment_id))

    result = dict(project_id=project_id,
                  experiment_id=experiment_id,
                  visit_id=visit_id,
                  session_type=session_type,
                  uid=uid,
                  experiment_label=experiment_label,
                  experiment_datetime=experiment_datetime,
                  acquisition_site=acquisition_site,
                  subject_id=subject_id,
                  manufactuer=manufactuer,
                  model=model,
                  project_uri=project_uri,
                  subject_uri=subject_uri,
                  experiment_uri=experiment_uri)
    if verbose:
        print("Parsed experiment info for: {0}".format(result))
    return result


def get_experiments_dir_info(config, experiments_dir):
    """
    Get a list of experiment dicts from all the experiment xml files in the
    experiments directory

    :param experiments_dir: str
    :return: list
    """
    results = list()
    if os.path.exists(os.path.abspath(experiments_dir)):
        glob_path = ''.join([os.path.abspath(experiments_dir), '/*'])
        experiment_files = glob.glob(glob_path)
    else:
        experiment_files = list()
    for path in experiment_files:
        results.append(get_experiment_info(config, path))
    return results


def get_scans_info(config, experiment_xml_file):
    """
    Get a dict of dicts for each scan from an XNAT experiment XML document

    :param experiment_xml_file: lxml.etree.Element
    :return: list
    """
    xml = etree.parse(experiment_xml_file)
    root = xml.getroot()
    experiment_id = root.attrib.get('ID')
    result = list()
    scans = root.findall('./xnat:scans/xnat:scan', namespaces=ns)
    for scan in scans:
        values = dict()
        scan_id = scan.attrib.get('ID')
        scan_type = scan.attrib.get('type')
        # handle null finds
        values.update(quality=scan.find('./xnat:quality', namespaces=ns))
        values.update(series_description=scan.find(
            './xnat:series_description', namespaces=ns))
        values.update(coil=scan.find('./xnat:coil', namespaces=ns))
        values.update(scanner=scan.find('./xnat:scanner', namespaces=ns))
        values.update(field_strength=scan.find('./xnat:fieldStrength',
                                               namespaces=ns))
        for k, v in values.iteritems():
            try:
                values[k] = v.text
            except AttributeError, e:
                values[k] = None
                if verbose:
                    print(e, "for attribute {0} in scan {1} of experiment {2}".format(k, scan_id, experiment_id))
        # Create URIRef objects for primary objects.
        entities = get_entities(config)
        scan_uri = rdflib.URIRef(entities['scan'](experiment_id, scan_id))
        scan_dict = dict(experiment_id=experiment_id,
                         scan_id=scan_id,
                         scan_type=scan_type,
                         scanner=values.get('scanner'),
                         quality=values.get('quality'),
                         series_description=values.get('series_description'),
                         coil=values.get('coil'),
                         field_strength=values.get('field_strength'),
                         scan_uri=scan_uri)
        result.append(scan_dict)
    return result


def get_experiments_dir_scan_info(config, experiments_dir):
    """
    Get a list of scan dicts from all the experiment xml files in the
    experiments directory

    :param experiments_dir: str
    :return: list
    """
    results = list()
    if os.path.exists(os.path.abspath(experiments_dir)):
        glob_path = ''.join([os.path.abspath(experiments_dir), '/*'])
        experiment_files = glob.glob(glob_path)
    else:
        experiment_files = list()
    for path in experiment_files:
        results.append(get_scans_info(config, path))
    return results

# Start conversion to NIDM

def initialize_graph():
    # Create a graph and add namespaces
    g = rdflib.Graph()
    nidm = rdflib.Namespace('http://purl.org/nidash/nidm/')
    prov = rdflib.Namespace('http://www.w3.org/ns/prov#')
    iri = rdflib.Namespace('http://purl.org/nidash/iri/')
    xnat = rdflib.Namespace('http://nrg.wustl.edu/xnat/')
    nrg = rdflib.Namespace('http://nrg.wustl.edu/')
    g.bind('nidm', nidm)
    g.bind('prov', prov)
    g.bind('iri', iri)
    g.bind('xnat', xnat)
    g.bind('nrg', nrg)
    return g


def get_namespaces(graph):
    """
    Extract namespaces from a graph and store as attrs of returned object.
    """
    namespace_dict = {k: rdflib.Namespace(v) for k, v in graph.namespaces()}
    return argparse.Namespace(**namespace_dict)


def get_sha_uri(text, graph):
    """
    Create a URI from a string
    """
    namespaces = get_namespaces(graph)
    return namespaces.iri[hashlib.sha1(text).hexdigest()]


def create_investigation_level(experiment, graph):
    # Now create the Investigation collection
    namespace = get_namespaces(graph)
    # Get info from the input dict
    project_uri = experiment.get('project_uri')
    experiment_uri = experiment.get('experiment_uri')
    activity_uri = get_sha_uri(experiment['project_id'], graph)
    agent_uri = namespace.iri[experiment.get('acquisition_site')]
    # Create an Investigation Clollection
    # Add type information and add to the graph.
    graph.add([project_uri,
               rdflib.RDF['type'],
               namespace.prov['Collection']])
    graph.add([project_uri,
               rdflib.RDF['type'],
               namespace.nidm['Investigation']])
    # Add the project id as an attribute in the XNAT namespace.
    graph.add([project_uri,
               namespace.xnat['project_id'],
               rdflib.Literal(experiment['project_id'])])
    # Add the site as the Agent of the Investigation.
    graph.add([project_uri,
               namespace.prov['wasAttributedTo'],
               agent_uri])
    # Add the (placeholder) activity that generated the Investigation
    graph.add([project_uri,
               namespace.prov['wasGeneratedBy'],
               activity_uri])
    # Add the type information for the acuisition site.
    graph.add([agent_uri,
               rdflib.RDF['type'],
               namespace.prov['Agent']])
    graph.add([agent_uri,
               rdflib.RDF['type'],
               namespace.prov['Organization']])
    # Add the acquisition site label for the acuisition site.
    graph.add([agent_uri,
               rdflib.RDFS['label'],
               rdflib.Literal(experiment['acquisition_site'])])
    # Add an activity for this investigation.
    graph.add([activity_uri,
               rdflib.RDF['type'],
               namespace.prov['Activity']])
    # Add a link to the investigation agent
    graph.add([activity_uri,
               namespace.prov['wasAssociatedWith'],
               agent_uri])
    # Add experiment as a member of the Investigation Collection.
    graph.add([project_uri,
               namespace.prov['hadMember'],
               experiment_uri])
    return graph


def create_session_level(experiment, scans, graph):
    # Now create the session collection
    namespace = get_namespaces(graph)
    # Get info from the input dict
    experiment_uri = experiment.get('experiment_uri')
    subject_uri = experiment.get('subject_uri')
    activity_uri = get_sha_uri(experiment['experiment_id'], graph)
    usage_bnode = rdflib.BNode()
    # Create an Investigation Clollection
    # Add type information and add to the graph.
    graph.add([experiment_uri,
               rdflib.RDF['type'],
               namespace.prov['Collection']])
    graph.add([experiment_uri,
               rdflib.RDF['type'],
               namespace.nidm['Session']])
    # Add the experiment id as an attribute in the XNAT namespace.
    graph.add([experiment_uri,
               namespace.xnat['experiment_id'],
               rdflib.Literal(experiment['experiment_id'])])
    # Add the subject as the Agent of the Session.
    graph.add([experiment_uri,
               namespace.prov['wasAttributedTo'],
               subject_uri])
    # Add the (placeholder) activity for Session.
    graph.add([experiment_uri,
               namespace.prov['wasGeneratedBy'],
               activity_uri])
    # Add the type information for the subject.
    graph.add([subject_uri,
               rdflib.RDF['type'],
               namespace.prov['Agent']])
    graph.add([subject_uri,
               rdflib.RDF['type'],
               namespace.prov['Person']])
    # Add the subject id label for the subject.
    graph.add([subject_uri,
               rdflib.RDFS['label'],
               rdflib.Literal(experiment['subject_id'])])
    # Add an activity for this session.
    graph.add([activity_uri,
               rdflib.RDF['type'],
               namespace.prov['Activity']])
    # Add a link to the subject agent
    graph.add([activity_uri,
               namespace.prov['wasAssociatedWith'],
               subject_uri])
    graph.add([activity_uri,
               namespace.prov['startedAtTime'],
               rdflib.Literal(experiment.get('experiment_datetime'))])
    graph.add([activity_uri,
               namespace.prov['endedAtTime'],
               rdflib.Literal(experiment.get('experiment_datetime'))])
    # Include the subject with a role in expanded "qualified" form
    graph.add([activity_uri,
               namespace.prov['qualifiedAssociation'],
               usage_bnode])
    graph.add([usage_bnode,
               rdflib.RDF['type'],
               namespace.prov['Association']])
    graph.add([usage_bnode,
               namespace.prov['agent'],
               subject_uri])
    graph.add([usage_bnode,
               namespace.prov['role'],
               namespace.nidm['Participant']])
    # Add scans as members of the Session Collection.
    for scan in scans:
        graph.add([experiment_uri,
                   namespace.prov['hadMember'],
                   scan.get('scan_uri')])
    return graph


def create_run_level(scan, graph):
    # Now create the run collection/entity
    namespace = get_namespaces(graph)
    # Get info from the input dict
    scan_uri = scan.get('scan_uri')
    scanner_uri = namespace.iri[scan.get('scanner')]
    activity_uri = get_sha_uri(scan['scan_id'], graph)
    # Create an Investigation Clollection
    # Add type information and add to the graph.
    graph.add([scan_uri,
               rdflib.RDF['type'],
               namespace.prov['Entity']])
    graph.add([scan_uri,
               rdflib.RDF['type'],
               namespace.nidm['Run']])
    # Add attributes in the XNAT namespace.
    graph.add([scan_uri,
               namespace.xnat['scan_id'],
               rdflib.Literal(scan['scan_id'])])
    graph.add([scan_uri,
               namespace.xnat['scan_type'],
               rdflib.Literal(scan['scan_type'])])
    graph.add([scan_uri,
               namespace.xnat['quality'],
               rdflib.Literal(scan['quality'])])
    graph.add([scan_uri,
               namespace.xnat['series_description'],
               rdflib.Literal(scan['series_description'])])
    graph.add([scan_uri,
               namespace.xnat['coil'],
               rdflib.Literal(scan['coil'])])
    graph.add([scan_uri,
               namespace.xnat['field_strength'],
               rdflib.Literal(scan['field_strength'])])
    # Add the scanner as the Agent of the Run.
    graph.add([scan_uri,
               namespace.prov['wasAttributedTo'],
               scanner_uri])
    # Add the (placeholder) activity for Session.
    graph.add([scan_uri,
               namespace.prov['wasGeneratedBy'],
               activity_uri])
    # Add the type information for the scanner.
    graph.add([scanner_uri,
               rdflib.RDF['type'],
               namespace.prov['Agent']])
    graph.add([scanner_uri,
               rdflib.RDF['type'],
               namespace.prov['Software']])
    # Add the scanner label for the scanner.
    graph.add([scanner_uri,
               rdflib.RDFS['label'],
               rdflib.Literal(scan['scanner'])])
    # Add an activity for this session.
    graph.add([activity_uri,
               rdflib.RDF['type'],
               namespace.prov['Activity']])
    # Add a link to the subject agent
    graph.add([activity_uri,
               namespace.prov['wasAssociatedWith'],
               scanner_uri])
    return graph

def main(args=None):
    if args.update:
        config = get_config(args.config)
        session = get_xnat_session(config)
        extract_experiment_xml(config, session,
                               args.experimentsdir, args.num_extract)

    # extract info from the experiment XML files
    experiment = get_experiments_dir_info(args.experimentsdir)
    scan = get_experiments_dir_scan_info(args.experimentsdir)


if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(prog='check_valid_sessions.py',
                                     description=__doc__)
    parser.add_argument('-c', '--config',
                        type=str)
    parser.add_argument('-b', '--baseline',
                        action='store_true',
                        help='Create report for baseline visit.')
    parser.add_argument('-e', '--experimentsdir',
                        type=str,
                        default='/tmp/experiments',
                        help='Name of experiments xml directory')
    parser.add_argument('-o', '--outfile',
                        type=str,
                        help='Name of csv file to write.')
    parser.add_argument('-n', '--num_extract',
                        type=int,
                        help='Number of sessions to extract')
    parser.add_argument('-u', '--update',
                        action='store_true',
                        help='Update the cache of xml files')
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='Print verbose output.')
    argv = parser.parse_args()
    verbose = argv.verbose

    sys.exit(main(args=argv))
