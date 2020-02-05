# example of configuration file

import os

configDir = os.path.expandvars("${CMSSW_BASE}/src/PlotsConfigurations/Configurations/WH3l/BDTconfig/Full2016_nAODv4")

tagName = ''

# luminosity to normalize to (in 1/fb)
lumi = 41.860

# file with list of cuts
cutsFile = os.path.join(configDir,'cuts_BDTTrain.py' )

# file with list of samples
samplesFile = os.path.join(configDir,'samples_BDTTrain.py' )
