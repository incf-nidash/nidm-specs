#!/usr/bin/env python
'''Read an owl file and extract interesting information

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2014
'''

from rdflib import RDF, term
from rdflib.graph import Graph
from rdflib.term import Literal
from Constants import *
import urllib2
import warnings
import vcr
import os
import logging
import csv
import collections
import re

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDM_PATH = os.path.dirname(RELPATH)

logging.basicConfig(filename='debug.log', level=logging.DEBUG, filemode='w')
logger = logging.getLogger(__name__)


class OwlReader():

    def __init__(self, owl_file, import_owl_files=None):
        self.file = owl_file
        self.import_files = import_owl_files
        self.graph = self.get_graph()

        # Retreive all classes defined in the owl file
        self.classes = self.get_class_names()
        self.properties = self.get_property_names()
        self.individuals = self.get_individuals()
        # For each class find out attribute list as defined by domain in
        # attributes
        self.attributes, self.ranges, \
            self.type_restrictions, self.parent_ranges = self.get_attributes()

        labels = dict(self.graph.subject_objects(RDFS['label']))
        self.labels = collections.OrderedDict(
            zip(labels.values(), labels.keys()))

    def get_class_names(self):
        # Add PROV sub-types
        sub_types = set([PROV['Bundle'], PROV['Location'],
                         PROV['Collection']])

        for class_name in self.graph.subjects(RDF['type'], OWL['Class']):
            if not isinstance(class_name, term.BNode):
                sub_types.add(class_name)

        return sub_types

    def get_direct_children(self, term):
        # Find all direct children of 'term'
        children = set()

        for class_name in self.graph.subjects(RDFS['subClassOf'], term):
            children.add(class_name)

        return children

    def get_direct_parents(self, term):
        # Find all direct parents of 'term'
        parents = set()

        for parent_name in self.graph.objects(term, RDFS['subClassOf']):
            parents.add(parent_name)

        return parents

    def get_nidm_parent(self, term):
        # Find direct nidm parent of 'term'
        parents = self.get_direct_parents(term)

        for parent in parents:
            if not self.is_external_namespace(parent):
                return parent

        return None

    def is_class(self, uri):
        return (uri, RDF['type'], OWL['Class']) in self.graph

    def get_class_names_by_prov_type(self, classes=None, prefix=None,
                                     but=None):
        class_names = dict()
        # We at least want to have an output for Entity, Activity and Agent
        class_names[PROV['Entity']] = list()
        class_names[PROV['Activity']] = list()
        class_names[PROV['Agent']] = list()

        class_names[None] = list()

        if not classes:
            classes = self.graph.subjects(RDF['type'], OWL['Class'])

            deprecated = self.graph.subjects(
                OWL['deprecated'], term.Literal(True))
            but = set(but).union(set(deprecated))

            # FIXME: Is there a more efficient way?
            if prefix:
                original_classes = classes
                classes = list()
                for class_name in original_classes:
                    if class_name.startswith(prefix):
                        classes.append(class_name)
            if but:
                classes = list(set(classes) - set(but))

            classes = sorted(classes)

        for class_name in classes:
            if not self.is_class(class_name):
                raise Exception('Class '+str(class_name)+' does not exist.')

            if not isinstance(class_name, term.BNode):
                prov_type = self.get_prov_class(class_name)
                if prov_type:
                    class_names.setdefault(prov_type, list())\
                               .append(class_name)
                else:
                    prov_type_found = False
                    parent_classes = self.get_direct_parents(class_name)
                    for parent_class in parent_classes:
                        prov_type = self.get_prov_class(parent_class,
                                                        recursive=3)
                        if prov_type:
                            class_names.setdefault(prov_type, list())\
                                       .append(class_name)
                            prov_type_found = True

                    if not prov_type_found:
                        warnings.warn('No PROV type for class: ' +
                                      self.graph.qname(class_name))
                        class_names.setdefault(None, list()).append(class_name)

        return class_names

    def is_deprecated(self, term):
        deprecated = False
        if (term, OWL['deprecated'], Literal(True)) in self.graph:
            deprecated = True
        return deprecated

    def get_property_names(self):
        properties = set()
        for class_name in self.graph.subjects(
                RDF['type'], OWL['DatatypeProperty']):
            if not self.is_deprecated(class_name):
                properties.add(class_name)
        for class_name in self.graph.subjects(
                RDF['type'], OWL['ObjectProperty']):
            if not self.is_deprecated(class_name):
                properties.add(class_name)
        return properties

    def get_individuals(self, uri=None):
        individuals = set()

        if uri is None:
            individuals = self.graph.subjects(
                RDF['type'], OWL['NamedIndividual'])
        else:
            individuals = self.graph.subjects(
                RDF['type'], uri)

        return list(individuals)

    def get_attributes(self):
        attributes = dict()
        # For each ObjectProperty found out corresponding range
        ranges = dict()

        parent_ranges = dict()

        restrictions = dict()

        # Check owl restrictions on classes
        for class_name in self.graph.subjects(RDF['type'], OWL['Class']):
            for class_restr in self.graph.objects(
                    class_name, RDFS['subClassOf']):
                if isinstance(class_restr, term.BNode):
                    for prp in self.graph.objects(
                            class_restr, OWL['onProperty']):
                        attributes.setdefault(class_name, set()).add(prp)
                        for child_class in self.graph.transitive_subjects(
                                RDFS['subClassOf'], class_name):
                            attributes.setdefault(child_class, set()).add(prp)

        # Attributes that can be found in all classes
        for prp, p, o in self.graph.triples((None, RDF['type'], None)):
            if not self.is_deprecated(prp):
                if o == OWL['DatatypeProperty'] or o == OWL['ObjectProperty']:
                    for class_name in self.graph.objects(prp, RDFS['domain']):
                        # Add attribute to current class
                        attributes.setdefault(class_name, set()).add(prp)

                        # Add attribute to children of current class
                        for child_class in self.graph.transitive_subjects(
                                RDFS['subClassOf'], class_name):
                            # Add attribute to current class
                            attributes.setdefault(child_class, set()).add(prp)

                    for range_name in self.graph.objects(prp, RDFS['range']):
                        # More complex type including restrictions
                        if isinstance(range_name, term.BNode):
                            for restriction_node in self.graph.objects(
                                    range_name, OWL['withRestrictions']):
                                for first_restriction in self.graph.objects(
                                        restriction_node, RDF['first']):
                                    xsd_restrictions = set(
                                        ['minInclusive', 'minExclusive',
                                         'maxInclusive', 'maxExclusive'])
                                    for rct in xsd_restrictions:
                                        for min_incl in self.graph.objects(
                                                first_restriction,
                                                XSD[rct]):
                                            if (prp in restrictions):
                                                if (rct in restrictions[prp]):
                                                    restrictions[prp] = max(
                                                        restrictions[prp][rct],
                                                        min_incl)
                                                else:
                                                    restrictions[prp] = {
                                                        rct: min_incl}
                                            else:
                                                restrictions[prp] = {
                                                    rct: min_incl}

                            for sub_range_name in self.graph.objects(
                                    range_name, OWL['onDatatype']):
                                range_name = sub_range_name

                        parent_ranges.setdefault(prp, set()).add(range_name)

                        # Add child_class to range (for ObjectProperty)
                        for child in self.graph.transitive_subjects(
                                RDFS['subClassOf'], range_name):
                            ranges.setdefault(prp, set()).add(child)

        return list((attributes, ranges, restrictions, parent_ranges))

    def get_graph(self):
        # Read owl (turtle) file
        owl_graph = Graph()
        if self.file[0:4] == "http":
            owl_txt = urllib2.urlopen(self.file).read()
        else:
            owl_txt = open(self.file, 'r').read()

        # This is a workaround to avoid issue with "#" in base prefix as
        # described in https://github.com/RDFLib/rdflib/issues/379. When
        # the fix is introduced in rdflib these 2 lines will be replaced by:
        # self.owl.parse(owl_file, format='turtle')
        owl_txt = owl_txt.replace("http://www.w3.org/2002/07/owl#",
                                  "http://www.w3.org/2002/07/owl")
        owl_graph.parse(data=owl_txt, format='turtle')

        if self.import_files:
            for import_file in self.import_files:
                # Read owl (turtle) file
                import_graph = Graph()
                if self.file[0:4] == "http":
                    import_txt = urllib2.urlopen(import_file).read()
                else:
                    import_txt = open(import_file, 'r').read()

                # This is a workaround to avoid issue with "#" in base prefix
                # as described in https://github.com/RDFLib/rdflib/issues/379,
                # When the fix is introduced in rdflib these 2 lines will be
                # replaced by:
                # self.owl.parse(owl_file, format='turtle')
                import_txt = import_txt.replace(
                    "http://www.w3.org/2002/07/owl#",
                    "http://www.w3.org/2002/07/owl")
                import_graph.parse(data=import_txt, format='turtle')

                owl_graph = owl_graph + import_graph

        return owl_graph

    def get_prov_class(self, owl_term, recursive=3):
        if not isinstance(owl_term, term.BNode) and \
                self.graph.qname(owl_term).startswith("prov:"):
            prov_class = owl_term
        else:
            parent_classes = list(self.graph.objects(
                owl_term, RDFS['subClassOf']))

            prov_class = None
            for parent_class in parent_classes:
                if not isinstance(parent_class, term.BNode):
                    if self.graph.qname(parent_class).startswith("prov:"):
                        prov_class = parent_class
                        break

            if not prov_class:
                if recursive > 0:
                    parent_classes_super = parent_classes
                    for parent_class_super in parent_classes_super:
                        if not isinstance(parent_class_super, term.BNode):
                            prov_class = self.get_prov_class(
                                parent_class_super, recursive=recursive-1)
                            if prov_class is not None:
                                break

        # Get mor generic PROV types
        if prov_class in set([PROV['SoftwareAgent'], PROV['Organization'],
                              PROV['Person']]):
            prov_class = PROV['Agent']
        if prov_class in set([PROV['Collection'], PROV['Location'],
                              PROV['Bundle'], PROV['Plan'],
                              PROV['EmptyCollection']]):
            prov_class = PROV['Entity']
        if prov_class in set([
                PROV['Usage'], PROV['AgentInfluence'],
                PROV['Derivation'], PROV['PrimarySource'],
                PROV['ActivityInfluence'], PROV['Delegation'],
                PROV['Start'], PROV['EntityInfluence'], PROV['Quotation'],
                PROV['End'], PROV['Attribution'], PROV['Association'],
                PROV['Revision'], PROV['Communication'],
                PROV['Generation']]):
            prov_class = PROV['Influence']
        if prov_class == PROV['Invalidation']:
            prov_class = PROV['InstantaneousEvent']

        return prov_class

    def get_definition(self, owl_term, add_links=True):
        definition = list(self.graph.objects(owl_term, OBO_DEFINITION))
        if definition:
            if len(definition) > 1:
                warnings.warn('Multiple definitions for '
                              + self.get_label(owl_term) + ': '
                              + ",".join(definition))
            definition = unicode(definition[0])
        else:
            definition = ""

        # Add link to term in document if the definition refer to a term
        if add_links:
            # definition = re.sub(
                # "("+"|".join(self.labels.keys())+")", "[\\1]", definition)
            terms = re.findall(r'\'.*?\'', definition)
            for mterm in sorted(set(terms), key=len, reverse=True):
                literal = Literal(mterm.replace("'", ""))
                if literal in self.labels:
                    purl = self.labels[literal]

                    if "#" in purl:
                        definition = definition.replace(
                            mterm,
                            "<a title=" +
                            purl.split("#")[1] + ">" +
                            mterm.replace("[", "").replace("]", "")+"</a>")

        # Remove final dot if present
        if definition:
            if definition[-1] == ".":
                definition = definition[:-1]

        return definition

    def get_individual_type(self, owl_term):
        indiv_type = list(self.graph.objects(owl_term, RDF['type']))
        if OWL['NamedIndividual'] in indiv_type:
            indiv_type.remove(OWL['NamedIndividual'])

        if indiv_type:
            indiv_type = ", ".join(map(self.graph.qname, indiv_type))
        else:
            indiv_type = ""
        return indiv_type

    def get_same_as(self, owl_term):
        same_as = list(self.graph.objects(owl_term, OWL['sameAs']))
        if same_as:
            same_as = ", ".join(same_as)
        else:
            same_as = ""
        return same_as

    def get_used_by(self, owl_term):
        used_by = list(self.graph.objects(owl_term, PROV['used']))
        return used_by

    def get_generated_by(self, owl_term):
        generated_by = list(self.graph.objects(
            owl_term, PROV['wasGeneratedBy']))
        return generated_by

    def get_example(self, owl_term, base_repository=None):
        example_list = list()

        examples = list(self.graph.objects(owl_term, OBO_EXAMPLE))

        for example in examples:
            if (base_repository is not None) and \
                    example.startswith(base_repository):
                local_path = example.replace(base_repository, "./")
                fid_ex = open(local_path)
                example = fid_ex.read()
                fid_ex.close()
            elif example.startswith("http"):
                with vcr.use_cassette(
                        os.path.join(NIDM_PATH, 'vcr_cassettes/synopsis.yaml'),
                        record_mode='new_episodes'):
                    # Read file from url
                    example = urllib2.urlopen(example).read()

            title = ""
            if example.startswith("#"):
                title = (example.split('\n', 1)[0]).replace("#", "")
                example = example.replace("#" + title, "")

            example_list.append([title, example])

        return sorted(example_list)

    def get_range(self, owl_term):
        ranges = list(self.graph.objects(owl_term, RDFS['range']))

        range_display = ""

        for range_value in ranges:
            if not isinstance(range_value, term.BNode):
                if isinstance(range_value, term.URIRef):
                    range_display += str(self.graph.qname(range_value))+" "
                else:
                    range_display += str(range_value)
        return range_display

    def get_domain(self, owl_term):
        domains = list(self.graph.objects(owl_term, RDFS['domain']))

        domain_display = ""

        for domain_value in sorted(domains):
            if isinstance(domain_value, term.URIRef):
                domain_display += str(self.graph.qname(domain_value))+" "
            else:
                domain_display += str(domain_value)
        return domain_display

    def get_curation_status(self, owl_term):
        curation_status = list(self.graph.objects(
            owl_term, HAS_CURATION_STATUS))
        if curation_status:
            if len(curation_status) > 1:
                warnings.warn('Multiple curation status for '
                              + self.get_label(owl_term) + ': '
                              + ",".join(curation_status))
            curation_status = curation_status[0]
        else:
            # By default consider that term is "uncurated"
            curation_status = OBO_UNCURATED
        return curation_status

    def get_editor(self, owl_term):
        editor = list(self.graph.objects(owl_term, OBO_TERM_EDITOR))
        if editor:
            if len(editor) > 1:
                warnings.warn('Multiple editors for '
                              + self.get_label(owl_term) + ': '
                              + ",".join(editor))
            editor = " (editor: "+editor[0]+")"
        else:
            editor = ""
        return editor

    def get_editor_note(self, owl_term):
        editor_note = list(self.graph.objects(owl_term, OBO_EDITOR_NOTE))
        if editor_note:
            if len(editor_note) > 1:
                warnings.warn('Multiple editor notes for '
                              + self.get_label(owl_term) + ': '
                              + ",".join(editor_note))
            editor_note = editor_note[0]
        else:
            editor_note = ""
        return editor_note

    def get_sub_class_names(self):
        sub_types = set()

        prov_types = set([PROV['Entity'], PROV['Activity'], PROV['Agent']])
        for prov_type in prov_types:
            for instance_id in self.graph.subjects(RDF.type, prov_type):
                for class_name in self.graph.objects(instance_id, RDF.type):
                    if not class_name == prov_type:
                        sub_types.add(class_name)

        return sub_types

    def check_class_names(self, ex_graph, ex_name, raise_now=False):
        my_exception = dict()
        error_msg = ""
        class_names = self.get_class_names()

        unrecognised_classes = list()
        # for class_name in ex_graph.subjects(RDF['type'], OWL['Class']):
        for class_name in ex_graph.objects(None, RDF.type):
            if not isinstance(class_name, term.BNode):
                if not class_name in class_names:
                    unrecognised_classes.append(class_name)

        for unrecognised_class in unrecognised_classes:
            if not unrecognised_class.startswith(str(PROV)):
                # key = ex_graph.qname(not_recognised_sub_type)
                key = "\n Unrecognised sub-type: " + \
                    ex_graph.qname(unrecognised_class)
                error_msg += key
                if key in my_exception:
                    my_exception[key].add(ex_name)
                else:
                    my_exception[key] = set([ex_name])

        if raise_now:
            if error_msg:
                raise Exception(error_msg)

        return my_exception

    def check_attributes(self, ex_graph, ex_name, raise_now=False):
        ignored_attributes = set([
            RDFS['label'],
            RDF['type'],
            PROV['value'], PROV['atTime'], PROV['used'],
            PROV['wasAssociatedWith'],
            PROV['qualifiedGeneration'], PROV['wasGeneratedBy'],
            PROV['atLocation'],
            PROV['activity'],
            PROV['wasDerivedFrom'],
            CRYPTO['sha512']
            ])

        my_exception = dict()
        my_range_exception = dict()
        my_restriction_exception = dict()

        owl_attributes = self.attributes
        owl_ranges = self.ranges
        owl_restrictions = self.type_restrictions

        # Find all attributes
        for s, p, o in ex_graph.triples((None, None, None)):
            # To be a DataTypeProperty then o must be a literal
            # if isinstance(o, rdflib.term.Literal):
            if p not in ignored_attributes:
                # *** Check domain
                # Get all defined types of current object
                found_attributes = False
                class_names = ""
                for class_name in sorted(ex_graph.objects(
                        s, RDF['type'])):
                    attributes = owl_attributes.get(class_name)

                    # If the current class was defined in the owl file check if
                    # current attribute was also defined.
                    if attributes:
                        if p in attributes:
                            found_attributes = True

                    class_names += ", "+ex_graph.qname(class_name) + \
                                   " (i.e. " + self.get_label(class_name) + ")"

                # if not found_attributes:
                    # if attributes:
                        # if not (p in attributes):
                if not found_attributes:
                    key = "\n Unrecognised attribute: " + \
                          ex_graph.qname(p) + \
                          " (i.e. " + self.get_label(p) + ")" + \
                          " in "+class_names[2:]
                    if not key in my_exception:
                        my_exception[key] = set([ex_name])
                    else:
                        my_exception[key].add(ex_name)

                # *** Check range for ObjectProperties and DataProperties
                if isinstance(o, term.URIRef):
                    # An ObjectProperty can point to an instance, then we look
                    # for its type:
                    found_range = set(ex_graph.objects(o, RDF['type']))

                    # An ObjectProperty can point to a term
                    if not found_range:
                        found_range = set([o])

                        # If the term is an individual, look for its type
                        if OWL['NamedIndividual'] in \
                                set(self.graph.objects(o, RDF['type'])):
                            found_range = set(
                                self.graph.objects(o, RDF['type']))

                elif isinstance(o, term.Literal):
                    found_range = set([o.datatype])

                correct_range = False
                if p in owl_ranges:
                    # If none of the class found for current ObjectProperty
                    # value is part of the range throw an error

                    # If the type of current value is within the authorised
                    # ranges
                    if found_range.intersection(owl_ranges[p]):
                        correct_range = True
                    else:
                        if p in owl_ranges:
                            # A bit more complicated to deal with
                            # "positiveInteger"
                            for owl_range in owl_ranges[p]:
                                # FIXME: we should be able to do better than
                                # that to check that XSD['positiveInteger'] is
                                # in owl_ranges[p]
                                if (XSD['positiveInteger'] == owl_range) \
                                        and (next(iter(found_range)) ==
                                             XSD['int']) \
                                        and (o.value >= 0):
                                    correct_range = True
                    if not correct_range:
                        found_range_line = ""
                        # FIXME: This should be better handled to be able to do
                        # "if found_range"
                        if not None in found_range:
                            found_range_line = ', '.join(
                                map(ex_graph.qname, sorted(found_range)))
                        owl_range_line = ""
                        if p in owl_ranges:
                            owl_range_line = ', '.join(
                                map(ex_graph.qname, sorted(owl_ranges[p])))

                        key = "\n Unrecognised range: " + \
                            found_range_line + \
                            ' for '+self.get_name(p) + \
                            " (i.e. " + self.get_label(p) + ")" + \
                            ' should be ' + \
                            owl_range_line
                else:
                    # No range found for current attribute
                    correct_range = False
                    key = "\n No range defined for: " + ex_graph.qname(p)

                if not correct_range:
                    if not key in my_range_exception:
                        my_range_exception[key] = set([ex_name])
                    else:
                        my_range_exception[key].add(ex_name)

                if p in owl_restrictions:
                    restrictions_ok = True
                    if 'minInclusive' in owl_restrictions[p]:
                        if o.value < owl_restrictions[p]['minInclusive'].value:
                            restrictions_ok = False
                    if 'minExclusive' in owl_restrictions[p]:
                        if o.value <= \
                                owl_restrictions[p]['minExclusive'].value:
                            restrictions_ok = False
                    if 'maxInclusive' in owl_restrictions[p]:
                        if o.value > owl_restrictions[p]['maxInclusive'].value:
                            restrictions_ok = False
                    if 'maxExclusive' in owl_restrictions[p]:
                        if o.value >= \
                                owl_restrictions[p]['maxExclusive'].value:
                            restrictions_ok = False
                    if not restrictions_ok:
                        key = "\n Contraints: value "+str(o.value) + \
                            ' for '+ex_graph.qname(p) + \
                            ' does not observe contraints ' + \
                            ', '.join(sorted(owl_restrictions[p]))
                        if not key in my_restriction_exception:
                            my_restriction_exception[key] = set([ex_name])
                        else:
                            my_restriction_exception[key].add(ex_name)

        if raise_now:
            error_msg = ""
            for exc in my_exception.keys():
                error_msg += exc
            for exc in my_range_exception.keys():
                error_msg += exc
            for exc in my_restriction_exception.keys():
                error_msg += exc

            if error_msg:
                raise Exception(error_msg)

        return list((my_exception, my_range_exception,
                     my_restriction_exception))

    def get_label(self, uri):
        if not isinstance(uri, term.BNode):
            name = self.graph.qname(uri)
        else:
            name = uri

        # If a label is available, use the namespace:label, otherwise qname
        label = list(self.graph.objects(uri, RDFS['label']))
        if label:
            if len(label) > 1:
                warnings.warn('Multiple labels for '+name+': '+",".join(label))
            label = sorted(label)[0]
            name = name.split(":")[0]+":'"+label+"'"

        return name

    def is_external_namespace(self, term_uri):
        term_label = self.get_label(term_uri)

        return not (term_label.startswith("nidm")
                    or term_label.startswith("fsl")
                    or term_label.startswith("spm")
                    or term_label.startswith("afni"))

    def is_prov(self, term_uri):
        term_label = self.get_label(term_uri)

        return term_label.startswith("prov")

    def get_name(self, uri):
        name = self.graph.qname(uri).split(":")[1]
        return name

    def get_preferred_prefix(self, uri):
        prefix_name = self.get_label(uri).replace(" ", "")\
                                         .replace(":", "_")\
                                         .replace("'", "")\
                                         .replace("-", "")
        return prefix_name

    def sorted_by_labels(self, term_list):
        class_labels = map(self.get_label, term_list)
        sorted_term_list = [x for (y, x) in
                            sorted(zip(class_labels, term_list))]

        return sorted_term_list

    def prefixes_as_csv(self, csvfile):
        with open(csvfile, 'wb') as fid:
            writer = csv.writer(fid)
            writer.writerow(["qname", "Preferred prefix"])

            # For anything that has a label
            for s, o in sorted(self.graph.subject_objects(RDFS['label'])):
                writer.writerow([
                    self.graph.qname(s),
                    self.get_preferred_prefix(s)])
