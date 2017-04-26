from NIDMExperiment import *

nidm_doc = NIDMExperimentProject()
inv = nidm_doc.addProject("FBIRN_PhaseII","9610","Test investigation")
nidm_doc.addLiteralAttribute(inv,"nidm","isAwesome","15")
nidm_doc.addLiteralAttribute(inv,"nidm", "score", float(2.34))
nidm_doc.addLiteralAttribute(inv, "nidm", "value", long(13412341235))
#add PI to investigation
nidm_doc.addProjectPI(inv,"Keator", "David")
print nidm_doc.serializeTurtle()
print nidm_doc.serializeJSONLD()