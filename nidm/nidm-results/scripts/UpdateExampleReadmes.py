# For each document in the NIDM repository, this script checks if there is a public document with the same content (from title)
# in the Prov Store (https://provenance.ecs.soton.ac.uk/store). If there is none, the document is uploaded and its README file is updated
# to link to the json, turtle, svg, PDF and png serialisations. 

# To use this script you need to have an account on the Prov Store (cf. https://provenance.ecs.soton.ac.uk/store/account/signup/) and to
# create a file named store_login_key.txt in the same directory including the following text: "mylogin:mykey" where mylogin 
# must be replaced by your Prov Store login and mykey by your ApiKey (cf. https://provenance.ecs.soton.ac.uk/store/account/developer/)

import urllib2
import json
import logging
import os
import rdflib
from rdflib.graph import Graph
from rdflib.compare import *
import sys

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)

# Append test directory to path
sys.path.append(os.path.join(RELPATH, "..", "test"))
from TestCommons import *

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Define title for all examples
doc_titles = dict()
doc_titles[os.path.join('spm', 'example001', 'example001_spm_results.provn')] = "SPM example 001"
doc_titles[os.path.join('fsl', 'example001', 'fsl_nidm.provn')] = "FSL example 001"
doc_titles[os.path.join('spm', 'spm_results.provn')] = "SPM"
doc_titles[os.path.join('spm', 'example002', 'spm_results_2contrasts.provn')] = "SPM example 002"
doc_titles[os.path.join('spm', 'example003', 'spm_results_conjunction.provn')] = "SPM example 003: Conjunction"
doc_titles[os.path.join('spm', 'example004', 'spm_inference_activities.provn')] = "SPM example 004: Inference"
doc_titles[os.path.join('fsl', 'fsl_results.provn')] = "FSL"

# Find document with same title in the prov store and return URL to json serialisation
def get_doc_from_title(doc_title):
	doc_url = None

	# Retreive most recent document with same title
	url = "https://provenance.ecs.soton.ac.uk/store/api/v0/documents/?document_name__startswith="+\
			doc_title+"&document_name__endswith="+doc_title+\
			"&format=json&order_by=-created_at&limit=1"
	req = urllib2.Request(url)

	response = urllib2.urlopen(req)
	data = json.load(response)
	if data['meta']['total_count'] == 0:
		logger.debug('No document entitled: "'+doc_title+'"')
	else:
		doc_url = "https://provenance.ecs.soton.ac.uk"+data['objects'][0]['resource_uri']
		logger.info('\tLast version of this document in the ProvStore: '+'"'+doc_url+'"')
	return doc_url

# Update Readme
def write_readme(readme_file, doc_url):
	readme_file_open = open(readme_file, 'w')

	doc_url = doc_url.replace("api/v0/", "")

	readme_file_open.write("""
Prov store: """+doc_url+"""
	
Alternative serialisations: [json]("""+doc_url[:-1]+""".json), [turtle]("""+doc_url[:-1]+""".ttl), 
Graph: [svg]("""+doc_url[:-1]+""".svg), [PDF]("""+doc_url[:-1]+""".pdf), [png]("""+doc_url[:-1]+""".png)

![Prov Graph]("""+doc_url[:-1]+""".png)

		""")
	readme_file_open.close()

# Create a new document on the ProvStore
def create_document(doc_json_url, doc_title):
	# Read json version of current document
	response = urllib2.urlopen(doc_json_url)
	# doc_json_url = response.geturl()
	doc_json = response.read()

	# Retreive ApiKey
	api_key_file = os.path.join(RELPATH, "store_login_key.txt")
	if not os.path.isfile(api_key_file):
		raise Exception("No Api Key. Please specify your ApiKey in store_login_key.txt.")
	api_key_file = open(api_key_file, 'r')
	api_key = api_key_file.read()

	# Create new document on the prov store
	url = "https://provenance.ecs.soton.ac.uk/store/api/v0/documents/"
	headers = { 'Content-type' : "application/json",
				'Authorization' : 'ApiKey '+api_key,
				'Accept' : "application/json" }
	# This is a trick to avoid issue with xsd namespace
	doc_json = doc_json.replace("http://www.w3.org/2001/XMLSchema", "http://www.w3.org/2001/XMLSchema#")
	data = ' {"content":'+doc_json+',"public":true,"rec_id":"'+doc_title+'"} '

	req = urllib2.Request(url, data, headers)

	response = urllib2.urlopen(req)
	data = json.load(response)

	doc_url = "https://provenance.ecs.soton.ac.uk"+data['resource_uri']
	logger.info('\tCreated document "'+doc_title+'" at: '+doc_url)

	return doc_url

if __name__ == '__main__':
	for example_file in example_filenames:

		# Get title for current document
		if example_file not in doc_titles:
			doc_title = "<Title not found>"
			logger.debug('No title for document: '+example_file)
		else:
			doc_title = doc_titles[example_file]

		doc_title="NIDM-Results: "+doc_title
		logger.info('Document entitled: '+'"'+doc_title+'"')

		# Get provn of current document
		doc_provn_file = os.path.join(NIDMRESULTSPATH, example_file)
		doc_ttl_file = doc_provn_file.replace(".provn", ".ttl")
		doc_provn_file_open = open(doc_provn_file, 'r')
		doc_provn = doc_provn_file_open.read()
		doc_provn_file_open.close()

		# Convert provn to json using Prov Translator APIs
		url = "https://provenance.ecs.soton.ac.uk/validator/provapi/documents/"
		headers = { 'Content-type' : "text/provenance-notation",
					'Accept' : "application/json" }
		req = urllib2.Request(url, doc_provn, headers)
		response = urllib2.urlopen(req)
		doc_json_url = response.geturl()
		logger.info('\tDocument in json: '+'"'+doc_json_url+'"')

		# Find most recent document with same title on the ProvStore
		# same_doc_url = get_doc_from_title(doc_title)

		# Find corresponding document on the ProvStore by looking at the README
		# Read README
		readme_file = os.path.join(NIDMRESULTSPATH, os.path.dirname(example_file), 'README.md')
		readme_fid = open(readme_file)
		readme_txt = readme_fid.read()
		readme_fid.close()

		provstore_url_index = re.search("https://provenance.ecs.soton.ac.uk/store/documents/[^/]*/", readme_txt)
		# Get corresponding turtle on Prov Store            
		if provstore_url_index:
			same_doc_url = readme_txt[provstore_url_index.start():provstore_url_index.end()]
		else:
			same_doc_url = None

		if same_doc_url:
			same_doc_ttl_url = same_doc_url[:-1]+".ttl"
			found_difference = compare_ttl_documents(doc_json_url.replace(".json", ".ttl"), same_doc_ttl_url) 
			
			if found_difference:
				logger.info('\tDifferent from last version.')
			else:
				logger.info('\tSame as last version.')
		else:
			logger.info('\tNo previous version.')
			found_difference = True

		if found_difference:
			doc_url = create_document(doc_json_url, doc_title)

			ttl_fid = open(doc_ttl_file, 'w')
			response = urllib2.urlopen(same_doc_ttl_url)
			doc_ttl = response.read()
			ttl_fid.write(doc_ttl)
			ttl_fid.close()
		else:
			doc_url = same_doc_url

		readme_file = os.path.join(os.path.dirname(os.path.join(NIDMRESULTSPATH, example_file)), 'README.md')
		if not os.path.isfile(readme_file):
			raise Exception("Missing README file. Please create a README file for "+example_file+".")
		write_readme(readme_file, doc_url)
