from NIDMExperiment import *

inv_test = NIDMExperimentInvestigation()
inv_test.addInvestigation("FBIRN_PhaseII","9610","Test investigation")
inv_test.addLiteralAttribute("nidm","isAwesome","15")
inv_test.addLiteralAttribute("nidm", "score", float(2.34))
inv_test.addLiteralAttribute("nidm", "value", long(13412341235))
print inv_test.serializeTurtle()