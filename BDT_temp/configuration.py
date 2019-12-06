# example of configuration file

import os

configDir = os.path.expandvars("${CMSSW_BASE}/src/PlotsConfigurations/Configurations/WH3l/Full2016_nanoAODv4_BDT/")

tagName = ''

# luminosity to normalize to (in 1/fb)
lumi = 41.860

# file with list of variables
variablesFile = os.path.join(configDir,'variables.py')

# file with list of cuts
cutsFile = os.path.join(configDir,'cuts.py' )

# file with list of samples
samplesFile = os.path.join(configDir,'samples.py' )

# structure file for datacard
structureFile = os.path.join(configDir,'structure.py')
