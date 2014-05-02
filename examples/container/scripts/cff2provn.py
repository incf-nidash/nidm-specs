from xml.dom.minidom import parse
import xml.dom.minidom
import urllib2
import prov.model as prov
from uuid import uuid1

dcterms = prov.Namespace("dcterms", "http://purl.org/dc/terms/")
xsd = prov.Namespace("xsd","http://www.w3.org/2001/XMLSchema#")
cff = prov.Namespace("cff", "http://www.connectomics.org/cff-2/")

# uuid method
get_id = lambda : uuid1().hex

# parse cff xml file
filename = "/Users/fariba/Desktop/UCI/freesurfer/scripts/meta.cml"
tree = xml.dom.minidom.parse(filename)
collections = tree.documentElement

g = prov.ProvBundle()
g.add_namespace(xsd)
g.add_namespace(dcterms);
g.add_namespace("prov", "http://www.w3.org/ns/prov-o/")
g.add_namespace(cff)


url_entity = g.entity(cff[get_id()])
url_entity.add_extra_attributes({prov.PROV['type']: 'cml:connectome',
  prov.PROV['location']:prov.Literal(filename,prov.XSD['String'])})

cml_collection = g.collection(cff[get_id()])
cml_collection.add_extra_attributes({prov.PROV['type']: cff['tag_collection'],prov.PROV['label']:filename})
g.wasDerivedFrom(cml_collection,url_entity)

# get species, subject_name, and subject_timepoint
species = tree.getElementsByTagName('cml:species')[0].toxml()
species = species.replace('<cml:species>','').replace('</cml:species>','')

tp = ''
sub = ''
tags = collections.getElementsByTagName("cml:tag")
for t in tags:
  if t.attributes['key'].value == 'subject_name':
    sub = t.toxml()
  if t.attributes['key'].value == 'subject_timepoint':
    tp = t.toxml()
sub = sub.replace('<cml:tag key="subject_name">','').replace('</cml:tag>','')
tp = tp.replace('<cml:tag key="subject_timepoint">','').replace('</cml:tag>','')
#print species + " " + sub + " " + tp

cml_meta = g.entity(cff[get_id()]);
cml_meta.add_extra_attributes({prov.PROV['type']:'cff:cml_tag',prov.PROV['label']:'cml_meta_tag',cff['species']:species,cff['timepoint']:tp,cff['subject_name']:sub})
g.hadMember(cml_collection, cml_meta)

volumes = collections.getElementsByTagName("cml:connectome-volume")
c = 0
for v in volumes:
  c = c + 1
  #print v.getAttribute("src") + " " + v.getAttribute("dtype") + " " + v.getAttribute("name") + " " + v.getAttribute("fileformat")
  #print v.attributes['fileformat'].value
  cml_volume = g.entity(cff[get_id()])
  cml_volume.add_extra_attributes({prov.PROV['type']:'cff:cml_tag',prov.PROV['label']:'cml_volume_tag',cff['dtype']:v.getAttribute("dtype"),cff['src']:v.getAttribute("src"),cff['name']:v.getAttribute("name"),cff['fileformat']:v.getAttribute("fileformat")})
  g.hadMember(cml_collection,cml_volume)

tracks = collections.getElementsByTagName("cml:connectome-track")
c = 0
for t in tracks:
  c = c + 1
  #print t.getAttribute("src") + " " + t.getAttribute("dtype") + " " + t.getAttribute("name") + " " + t.getAttribute("fileformat")
  cml_track = g.entity(cff[get_id()])
  cml_track.add_extra_attributes({prov.PROV['type']:'cff:cml_tag',prov.PROV['label']:'cml_track_tag',cff['dtype']:t.getAttribute("dtype"),cff['src']:t.getAttribute("src"),cff['name']:t.getAttribute("name"),cff['fileformat']:t.getAttribute("fileformat")})
  g.hadMember(cml_collection,cml_track)

networks = collections.getElementsByTagName("cml:connectome-network")
c = 0
for n in networks:
  c = c + 1
  #print n.getAttribute("src") + " " + n.getAttribute("dtype") + " " + n.getAttribute("name") + " " + n.getAttribute("fileformat")
  cml_network = g.entity(cff[get_id()])
  cml_network.add_extra_attributes({prov.PROV['type']:'cff:cml_tag',prov.PROV['label']:'cml_network_tag',cff['dtype']:n.getAttribute("dtype"),cff['src']:n.getAttribute("src"),cff['name']:n.getAttribute("name"),cff['fileformat']:n.getAttribute("fileformat")})
  g.hadMember(cml_collection,cml_network)

surfaces = collections.getElementsByTagName("cml:connectome-surface")
c = 0
for s in surfaces:
  c = c + 1
  #print s.getAttribute("src") + " " + s.getAttribute("dtype") + " " + s.getAttribute("name") + " " + s.getAttribute("fileformat")
  cml_surface = g.entity(cff[get_id()])
  cml_surface.add_extra_attributes({prov.PROV['type']:'cff:cml_tag',prov.PROV['label']:'cml_surface_tag',cff['dtype']:s.getAttribute("dtype"),cff['src']:s.getAttribute("src"),cff['name']:s.getAttribute("name"),cff['fileformat']:s.getAttribute("fileformat")})
  g.hadMember(cml_collection,cml_surface)

data = collections.getElementsByTagName("cml:connectome-data")
c = 0
for d in data:
  c = c + 1
  #print d.getAttribute("src") + " " + d.getAttribute("dtype") + " " + d.getAttribute("name") + " " + d.getAttribute("fileformat")
  cml_data = g.entity(cff[get_id()])
  cml_data.add_extra_attributes({prov.PROV['type']:'cff:cml_tag',prov.PROV['label']:'cml_data_tag',cff['dtype']:d.getAttribute("dtype"),cff['src']:d.getAttribute("src"),cff['name']:d.getAttribute("name"),cff['fileformat']:d.getAttribute("fileformat")})
  g.hadMember(cml_collection,cml_data)


provn = g.get_provn()
with open('cff-sample.provn', 'wt') as fp:
  fp.writelines(provn)

g.rdf().serialize('cff-sample.ttl', format='turtle')
g.rdf().serialize('cff-sample.xml', format='xml')
exit()
