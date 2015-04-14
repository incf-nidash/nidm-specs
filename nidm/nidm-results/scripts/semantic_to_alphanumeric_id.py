"""
Convert from semantic identifier (e.g. nidm:ContrastMap) to alphanumeric
identifier (e.g. nidm:NIDM_0000012) for a given term

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2015
"""

import os
import re
import glob
import sys

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)

TERMS_PATH = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), 'terms')

# Append parent script directory to path
sys.path.append(
    os.path.join(RELPATH, os.pardir, os.pardir, os.pardir, "scripts"))
from OwlReader import OwlReader
from Constants import NIDM, SPM, FSL


def main(sid, aid, owl_file, template_files, script_files,
         constants_file):
    owl_txt = get_file_text(owl_file)

    templates_txt = dict()
    for template_file in template_files:
        templates_txt[template_file] = get_file_text(template_file)

    scripts_txt = dict()
    for script_file in script_files:
        scripts_txt[script_file] = get_file_text(script_file)

    cst_txt = get_file_text(constants_file)

    # If alphanumeric identifier was not defined, find the next available
    if aid is None:
        before_alnum = "nidm:NIDM_"

        # Find all alphanumeric identifiers in the owl file
        alphanum_ids = set(re.findall("("+before_alnum+'\d+)\s+', owl_txt))

        # Get identifier number for next alphanumeric identifier
        last_id = sorted(list(alphanum_ids))[-1]
        new_id_num = int(last_id.replace(before_alnum, ""))+1

        aid = before_alnum+"{0:0>7}".format(new_id_num)

    owl = OwlReader
    sid_name = sid.split(":")[1]
    sid_namespace = sid.split(":")[0]

    if sid_namespace == "nidm":
        uri = NIDM[sid_name]
    elif sid_namespace == "fsl":
        uri = FSL[sid_name]
    elif sid_namespace == "spm":
        uri = SPM[sid_name]

    owl = OwlReader(owl_file)
    label = owl.get_label(uri).split(":")[1].replace("'", "")

    # Replace all occurences of semantic id
    owl_txt = owl_txt.replace(sid+" ", aid+" ")
    # Replace ids in templates
    for tpl, tpl_txt in templates_txt.items():
        templates_txt[tpl] = tpl_txt.replace(sid+" ", aid+" ")
    for scr, scr_txt in scripts_txt.items():
        scripts_txt[scr] = scr_txt.replace('"'+sid+'"', '"'+aid+'"')

    new_constant = "NIDM_" + label.upper().replace(" ", "_") + \
                   " = NIDM['"+aid.replace("nidm:", "")+"']"
    cst_txt = cst_txt.replace("# NIDM constants",
                              "# NIDM constants\n"+new_constant)

    replace_file_txt(owl_file, owl_txt)
    replace_file_txt(constants_file, cst_txt)
    for tpl, tpl_txt in templates_txt.items():
        replace_file_txt(tpl, tpl_txt)
    for scr, scr_txt in scripts_txt.items():
        replace_file_txt(scr, scr_txt)


def get_file_text(file_name):
    fid = open(file_name)
    txt = fid.read()
    fid.close()
    return txt


def replace_file_txt(file_name, txt):
    fid = open(file_name, 'w')
    fid.write(txt)
    fid.close()

if __name__ == '__main__':
    if len(sys.argv) > 1 and len(sys.argv) <= 3:
        semantic_id = sys.argv[1]
        if len(sys.argv) == 3:
            aphanum_id = sys.argv[2]
        else:
            aphanum_id = None
    else:
        raise Exception("1 or 2 arguments are needed.")

    owl_file = os.path.join(TERMS_PATH, 'nidm-results.owl')

    template_files = glob.glob(os.path.join(TERMS_PATH, "templates", '*.txt'))
    script_files = glob.glob(
        os.path.join(TERMS_PATH, os.pardir, "scripts", '*.py'))

    constants_file = os.path.join(TERMS_PATH, os.pardir, os.pardir,
                                  os.pardir, "scripts", 'Constants.py')

    main(semantic_id, aphanum_id, owl_file,
         template_files, script_files, constants_file)
