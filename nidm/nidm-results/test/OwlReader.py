#!/usr/bin/env python
'''Read an owl file and extract interesting information

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2014
'''

from rdflib import Namespace, RDF, term
from rdflib.graph import Graph
from Constants import *
import urllib

class OwlReader():

    def __init__(self, owl_file):
        self.file = owl_file       
        self.graph = self.get_graph()
        
        # Retreive all classes defined in the owl file
        self.classes = self.get_class_names() 
        self.properties = self.get_property_names()
        # For each class find out attribute list as defined by domain in attributes
        attributes_ranges = self.get_attributes()
        self.attributes = attributes_ranges[0]
        self.ranges = attributes_ranges[1]      
        self.type_restrictions = attributes_ranges[2]     


    def get_class_names(self):
        # Add PROV sub-types
        sub_types = set([PROV['Bundle'], PROV['Location'], PROV['Collection']]);

        for class_name in self.graph.subjects(RDF['type'], OWL['Class']):
            if not isinstance(class_name, term.BNode):
                sub_types.add(class_name)

        return sub_types

    def get_class_names_by_prov_type(self, classes=None):
        class_names = dict()
        class_names[PROV['Entity']] = list()
        class_names[PROV['Activity']] = list()
        class_names[PROV['Agent']] = list()

        if not classes:
            classes = self.graph.subjects(RDF['type'], OWL['Class'])

        for class_name in classes:
            if not isinstance(class_name, term.BNode):
                prov_type = self.get_prov_class(class_name)
                if prov_type:
                    class_names[prov_type].append(class_name)
                else:
                    prov_type_found = False
                    parent_classes = list(self.graph.objects(class_name, RDFS['subClassOf']))
                    for parent_class in parent_classes:
                        prov_type = self.get_prov_class(parent_class, recursive=3)
                        if prov_type:
                            class_names[prov_type].append(class_name)
                            prov_type_found = True
                        # else:
                        #     parent_classes_2 = list(self.graph.objects(parent_class, RDFS['subClassOf']))
                        #     for parent_class_2 in parent_classes_2:
                        #         prov_type = self.get_prov_class(parent_class_2)
                        #         if prov_type:
                        #             class_names[prov_type].append(class_name)
                        #             prov_type_found = True
                        #         else:
                        #             parent_classes_3 = list(self.graph.objects(parent_class, RDFS['subClassOf']))
                        #             for parent_class_3 in parent_classes_3:
                        #                 prov_type = self.get_prov_class(parent_class_3)
                        #                 if prov_type:
                        #                     class_names[prov_type].append(class_name)
                        #                     prov_type_found = True

                    if not prov_type_found:
                        raise Exception('No PROV type for class: '+self.graph.qname(class_name))
        return class_names

    def get_property_names(self):
        properties = set();
        for class_name in self.graph.subjects(RDF['type'], OWL['DatatypeProperty']):
            properties.add(class_name)
        for class_name in self.graph.subjects(RDF['type'], OWL['ObjectProperty']):
            properties.add(class_name)
        return properties

    def get_attributes(self):
        attributes = dict()
        # For each ObjectProperty found out corresponding range
        ranges = dict()

        restrictions = dict()

        # Attributes that can be found in all classes
        for data_property,p,o in self.graph.triples((None, RDF['type'], None)):
            if o == OWL['DatatypeProperty'] or o == OWL['ObjectProperty']:
                for class_name in self.graph.objects(data_property, RDFS['domain']):
                    # Add attribute to current class
                    if class_name in attributes:
                        attributes[class_name].add(data_property)
                    else:
                        attributes[class_name] = set([data_property])
                    
                    # Add attribute to children of current class
                    for child_class in self.graph.subjects(RDFS['subClassOf'], class_name):
                        # Add attribute to current class
                        if child_class in attributes:
                            attributes[child_class].add(data_property)
                        else:
                            attributes[child_class] = set([data_property])
                        class_name = child_class
                        
                for range_name in self.graph.objects(data_property, RDFS['range']):
                    # More complex type including restrictions
                    if isinstance(range_name, term.BNode):
                        for restriction_node in self.graph.objects(range_name, OWL['withRestrictions']):
                            for first_restriction in self.graph.objects(restriction_node, RDF['first']):
                                xsd_restrictions = set(['minInclusive', 'minExclusive', 'maxInclusive', 'maxExclusive'])
                                for xsd_restriction in xsd_restrictions:
                                    for min_incl in self.graph.objects(first_restriction, XSD[xsd_restriction]):
                                        if (data_property in restrictions):
                                            if (xsd_restriction in restrictions[data_property]):
                                                restrictions[data_property] = max(restrictions[data_property][xsd_restriction], min_incl)
                                            else:
                                                restrictions[data_property] = { xsd_restriction: min_incl}
                                        else:
                                            restrictions[data_property] = { xsd_restriction: min_incl}

                        for sub_range_name in self.graph.objects(range_name, OWL['onDatatype']):
                            range_name = sub_range_name

                    if data_property in ranges:
                        ranges[data_property].add(range_name)
                    else:
                        ranges[data_property] = set([range_name])
                    # FIXME: more elegant?
                    # Add child_class to range (for ObjectProperty)
                    for child_class in self.graph.subjects(RDFS['subClassOf'], range_name):
                        # Add range to current class
                        if data_property in ranges:
                            ranges[data_property].add(child_class)
                        else:
                            ranges[data_property] = set([child_class])
                        range_name = child_class
                        for child_class in self.graph.subjects(RDFS['subClassOf'], range_name):
                            # Add attribute to current class
                            if data_property in ranges:
                                ranges[data_property].add(child_class)
                            else:
                                ranges[data_property] = set([child_class])
                            range_name = child_class
                            for child_class in self.graph.subjects(RDFS['subClassOf'], range_name):
                                # Add attribute to current class
                                if data_property in ranges:
                                    ranges[data_property].add(child_class)
                                else:
                                    ranges[data_property] = set([child_class])
                                range_name = child_class
                                for child_class in self.graph.subjects(RDFS['subClassOf'], range_name):
                                    # Add attribute to current class
                                    if data_property in ranges:
                                        ranges[data_property].add(child_class)
                                    else:
                                        ranges[data_property] = set([child_class])
                                    range_name = child_class
                
                    

        return list((attributes, ranges, restrictions))

    def get_graph(self):
        # Read owl (turtle) file
        owl_graph = Graph()
        if self.file[0:4] == "http":
            print "url open:"+self.file
            owl_txt = urllib.urlopen(self.file).read()
        else:
            owl_txt = open(self.file, 'r').read()

        # This is a workaround to avoid issue with "#" in base prefix as 
        # described in https://github.com/RDFLib/rdflib/issues/379,
        # When the fix is introduced in rdflib these 2 lines will be replaced by:
        # self.owl.parse(owl_file, format='turtle')
        owl_txt = owl_txt.replace("http://www.w3.org/2002/07/owl#", 
                        "http://www.w3.org/2002/07/owl")
        owl_graph.parse(data=owl_txt, format='turtle')

        return owl_graph


    def get_prov_class(self, owl_term, recursive=3):
        if self.graph.qname(owl_term)[0:5] == "prov:":
            prov_class = owl_term
        else:
            parent_classes = list(self.graph.objects(owl_term, RDFS['subClassOf']))

            prov_class = ""
            for parent_class in parent_classes:
                # FIXME: get namespace instead?
                if self.graph.qname(parent_class)[0:5] == "prov:":
                    prov_class = parent_class
                    break;

            if not prov_class:
                if recursive > 0:
                    parent_classes_super = parent_classes
                    for parent_class_super in parent_class:
                        prov_class = self.get_prov_class(parent_class, recursive=recursive-1)

        # Get mor generic PROV types
        if prov_class == PROV['SoftwareAgent']:
                prov_class = PROV['Agent']
        if prov_class in set([PROV['Collection'], PROV['Location'], PROV['Bundle']]):
                prov_class = PROV['Entity']

        return prov_class

    def get_definition(self, owl_term):
        definition = list(self.graph.objects(owl_term, PROV['definition']))
        if definition:
            definition = str(definition[0])
        else:
            definition = ""
        return definition

    def get_used_by(self, owl_term):
        used_by = list(self.graph.objects(owl_term, PROV['used']))
        return used_by

    def get_generated_by(self, owl_term):
        generated_by = list(self.graph.objects(owl_term, PROV['wasGeneratedBy']))
        return generated_by

    def get_example(self, owl_term):
        example = list(self.graph.objects(owl_term, IAO_EXAMPLE))
        if example:
            example = str(example[0])
        else:
            example = ""
        return example

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
        curation_status = OBO_UNCURATED
        curation_status = list(self.graph.objects(owl_term, HAS_CURATION_STATUS))
        if curation_status:
            curation_status = curation_status[0]
        return curation_status

    def get_editor(self, owl_term):
        editor = list(self.graph.objects(owl_term, NIDM['termEditor']))
        if editor:
            editor = " (editor: "+editor[0]+")"
        else:
            editor = ""
        return editor
