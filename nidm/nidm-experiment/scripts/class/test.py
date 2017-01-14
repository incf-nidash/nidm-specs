from NIDMExperiment import *

nidm_doc = NIDMExperimentInvestigation()
inv = nidm_doc.addInvestigation("FBIRN_PhaseII","9610","Test investigation")
nidm_doc.addLiteralAttribute(inv,"nidm","isAwesome","15")
nidm_doc.addLiteralAttribute(inv,"nidm", "score", float(2.34))
nidm_doc.addLiteralAttribute(inv, "nidm", "value", long(13412341235))
#add PI to investigation
nidm_doc.addInvestigationPI(inv,"Keator", "David")
print nidm_doc.serializeTurtle()