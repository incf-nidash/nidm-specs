"""
Convert from semantic identifiers (e.g. nidm:ContrastMap) to alphanumeric 
identifiers (e.g. nidm:NIDM_0000012)

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2015
"""

import os, re, glob

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)

TERMS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'terms')

def main(owl_file, template_files, script_files, constants_file):
	owl_txt = get_file_text(owl_file)

	templates_txt = dict()
	for template_file in template_files:
		templates_txt[template_file] = get_file_text(template_file)

	scripts_txt = dict()
	for script_file in script_files:
		scripts_txt[script_file] = get_file_text(script_file)		

	cst_txt = get_file_text(constants_file)

	before_alnum = "nidm:NIDM_"
	before_seman = "nidm:"

	# Find all alphanumeric identifiers in the owl file
	alphanum_ids = set(re.findall("("+before_alnum+'\d+)\s+', owl_txt))

	# Find all semantic identifiers in the owl file
	semantic_ids = sorted(set(re.findall("("+before_seman+'\w+)\s+', owl_txt)) - alphanum_ids)

	# Get identifier number for next alphanumeric identifier
	last_id = sorted(list(alphanum_ids))[-1]	
	new_id_num = int(last_id.replace(before_alnum, ""))+1

	for sid in semantic_ids:
		aid = before_alnum+"{0:0>7}".format(new_id_num)

		# Replace ids in owl_file (and for class definition add label)
		words = re.findall('[A-Z][^A-Z]*', sid)

		# Group acronyms
		for idx, word in reversed(list(enumerate(words))):
			# As word might have been updated at a previous iteration
			word = words[idx]
			previous_word = words[idx-1]
			if len(previous_word) == 1:
				if sum(1 for c in word if c.islower()) == 0 or not len(words[idx-2]) == 1:
					words[idx-1] = previous_word+word
					words.pop(idx)

		beginning = sid.replace(''.join(words), '')
		if beginning == sid:
			# Just a single word
			label = sid.replace("nidm:", "")
		else:
			beginning = beginning.replace("nidm:", "")
			if beginning:
				beginning = beginning+" "
			# Several words
			label = beginning+" ".join(words)

		class_def = re.compile(sid+r'(\s+rdf:type\s+owl:\w+\s+;)')
		owl_txt = class_def.sub(aid+r'\1'+"""

                            rdfs:label \""""+label+"""\" ;""", owl_txt)
		indiv_def = re.compile(sid+r'(\s+rdf:type[^\.]+owl:NamedIndividual\s+;)')
		owl_txt = indiv_def.sub(aid+r'\1'+"""

                    rdfs:label \""""+label+"""\" ;""", owl_txt)

		# Replace remaining occurences of semantic id
		owl_txt = owl_txt.replace(sid+" ", aid+" ")
		# Replace ids in templates
		for tpl, tpl_txt in templates_txt.items():
			templates_txt[tpl] = tpl_txt.replace(sid+" ", aid+" ")
		for scr, scr_txt in scripts_txt.items():
			scripts_txt[scr] = scr_txt.replace('"'+sid+'"', '"'+aid+'"')

		new_constant = "NIDM_"+label.upper().replace(" ", "_")+" = NIDM['"+aid.replace("nidm:", "")+"']"
		cst_txt = cst_txt.replace("# NIDM constants", "# NIDM constants\n"+new_constant)

		new_id_num = new_id_num + 1

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
	owl_file = os.path.join(TERMS_PATH, 'nidm-results.owl')

	template_files = glob.glob(os.path.join(TERMS_PATH, "templates", '*.txt'))
	script_files = glob.glob(os.path.join(TERMS_PATH, os.pardir, "scripts", '*.py'))

	constants_file = os.path.join(TERMS_PATH, os.pardir, os.pardir, \
		os.pardir, "scripts", 'Constants.py')

	main(owl_file, template_files, script_files, constants_file)