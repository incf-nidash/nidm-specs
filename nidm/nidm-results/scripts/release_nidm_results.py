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
import re
from rdflib.compare import *
import sys
import shutil
import urllib2
from create_results_specification import main as create_spec
import glob
import recompute_all_ex
import UpdateExampleReadmes
import UpdateTermReadme
from create_prefixes import main as create_pref

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)
NIDMPATH = os.path.join(NIDMRESULTSPATH, os.pardir)
SPECSPATH = os.path.join(NIDMPATH, os.pardir, "doc", "content", "specs")
SCRIPTPATH = os.path.join(NIDMPATH, os.pardir, "scripts")

# Append parent script directory to path
sys.path.append(SCRIPTPATH)
from Constants import *

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TERMS_FOLDER = os.path.join(NIDMRESULTSPATH, 'terms')
IMPORT_FOLDER = os.path.join(os.path.dirname(NIDMRESULTSPATH), "imports")
RELEASED_TERMS_FOLDER = os.path.join(TERMS_FOLDER, "releases")


class NIDMRelease(object):

    def get_import_name(self, import_url):
        return import_url.split("/")[-1].replace(".owl", "")

    def __init__(self, nidm_original_version):
        self.nidm_original_version = nidm_original_version
        self.nidm_version = \
            nidm_original_version.replace(".", "")

    def create_release(self):
        owl_file = os.path.join(TERMS_FOLDER, 'nidm-results.owl')
        assert os.path.exists(owl_file)

        # Copy the owl file to the release folder
        release_owl_file = os.path.join(
            RELEASED_TERMS_FOLDER,
            "nidm-results_%s.owl" % (self.nidm_version))
        shutil.copyfile(owl_file, release_owl_file)

        with open(release_owl_file, 'r') as fp:
            owl_txt = fp.read()

        # Remove imports and copy the import directly in the release file
        match = re.search(
            r'\[[\w:;\n\s]' +
            r'*(?P<imports>(\s*<.*>\s*,?\s*\n)*)\s*\] \.', owl_txt)
        if match:
            owl_txt = owl_txt.replace(match.group(), "")

            owl_imports = re.findall(r"<.*>", match.group("imports"))

            for im in owl_imports:
                im = im.replace("<", "").replace(">", "")
                im_name = self.get_import_name(im)
                name = im_name.split("-")[0].replace("_import", "")

                im_file = os.path.join(IMPORT_FOLDER, im_name+".ttl")

                if os.path.exists(im_file):
                    with open(im_file, 'r') as fp:
                        im_txt = fp.read()
                else:
                    response = urllib2.urlopen(im+'.ttl')
                    im_txt = response.read()

                # Replace prefix ":" by named namespace in import
                default_match = re.search(r'@prefix : <.*>', im_txt)
                if default_match:
                    im_txt = im_txt.replace(" :", " "+name+":")
                    im_txt = im_txt.replace("\n:", "\n"+name+":")

                # Remove base prefix
                base_match = re.search(r'@base <.*>', im_txt)
                if base_match:
                    im_txt = im_txt.replace(base_match.group(), "")

                # Copy missing prefixes in nidm-results owl file
                prefixes = re.findall(r'@prefix \w+: <.*> \.\n', im_txt)
                for prefix in prefixes:
                    if not prefix in owl_txt:
                        owl_txt = prefix+owl_txt
                    im_txt = im_txt.replace(prefix, "")

                owl_txt = owl_txt + "\n\n##### Imports from %s #####" % (name)
                owl_txt = owl_txt + im_txt

        # Remove AFNI-related terms (not ready for release yet)
        if int(self.nidm_version.split("-rc")[0]) <= 130:
            owl_txt = owl_txt.replace(
                "@prefix afni: <http://purl.org/nidash/afni#> .\n", "")
            # Remove terms: nidm:'Legendre Polynomial Order', afni:'BLOCK',
            # afni:'GammaHRF' and afni:'LegendrePolynomialDriftModel'
            terms_under_development = [
                NIDM['NIDM_0000014'], AFNI['BLOCK'], AFNI['GammaHRF'],
                AFNI['LegendrePolynomialDriftModel']]
            for term in terms_under_development:
                m = re.search(
                    re.escape("###  "+str(term))+r"[^\#]*\.", owl_txt)
                owl_txt = owl_txt.replace(m.group(), "")

        with open(release_owl_file, 'w') as fp:
            fp.write(owl_txt)

        # Create specification (before the address of examples are updated to
        # avoid issue with examples pointing to tag not pushed yet)
        create_spec(self.nidm_original_version)
        image_dir_prev = os.path.join(SPECSPATH, "img", "nidm-results_dev")
        image_dir = os.path.join(
            SPECSPATH, "img", "nidm-results_"+self.nidm_version)
        if not os.path.isdir(image_dir):
            shutil.copytree(image_dir_prev, image_dir)

        # Update version number in examples and in script files
        script_files = glob.glob(
            os.path.join(NIDMRESULTSPATH, "scripts", "*.py"))
        for script in script_files:
            if not script.endswith("release_nidm_results.py"):
                with open(script, 'r') as fp:
                    script_txt = fp.read()
                with open(script, 'w') as fp:
                        fp.write(
                            script_txt.replace(
                                'version="dev"',
                                'version="' + self.nidm_original_version +
                                '"'))
        # Re-create turtle examples from template
        recompute_all_ex.main()
        # Upload to Prov Store
        UpdateExampleReadmes.main()
        # Update terms README
        UpdateTermReadme.main()
        # Update specifications

        # Replace address of examples
        owl_txt = owl_txt.replace(
            "https://raw.githubusercontent.com/incf-nidash/nidm/\
master/",
            "https://raw.githubusercontent.com/incf-nidash/nidm/\
NIDM-Results_"+self.nidm_original_version+"/")

        with open(release_owl_file, 'w') as fp:
            fp.write(owl_txt)

        create_pref(release_owl_file)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        nidm_version = sys.argv[1]
    else:
        raise Exception("Error: missing version number for NIDM release")

    nidm_release = NIDMRelease(nidm_version)
    nidm_release.create_release()
