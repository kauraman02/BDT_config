#!/usr/bin/env python

from __future__ import print_function
import os
from ROOT import gROOT, TFile, TChain, TCut

# import models
import preselections

isDEV=True

# Load configuration
with open("configuration.py") as handle:
    exec handle

samples={}
structure={}
cuts={}
for f in [samplesFile, structureFile, cutsFile]:
    with open(f) as handle:
        exec handle


# Reduce sample files for fast dev
# DY_2
                         # : Add Tree Events of type Background with 635 events
# top_3
                         # : Add Tree Events of type Background with 975 events
# top_2
                         # : Add Tree Events of type Background with 2834 events
# top_6
                         # : Add Tree Events of type Background with 4389 events
# Vg_1
                         # : Add Tree Events of type Background with 2101 events
# top_4
                         # : Add Tree Events of type Background with 956 events
# top_5
                         # : Add Tree Events of type Background with 2306 events



if isDEV:
    for sampleName, sample in samples.items():
        if sampleName not in ['WZ','ZZ','Vg_1','Vg_2','WH_hww_1','WH_hww_2','WH_htt_1','WH_htt_2','DY_1','DY_2','top_1','top_2','top_3','top_4','top_5','top_6']:
        # if sampleName not in ['WZ','WW','ZZ','VVV','Vg_1','Vg_2','WH_hww_1','WH_hww_2','WH_htt_1','WH_htt_2','DY_1','DY_2','top_1','top_2','top_3','top_4','top_5','top_6']:
        # if sampleName not in ['WZ','WW','ZZ','VVV','Vg','WH_hww','WH_htt','DY','top']:
            samples.pop(sampleName)
            continue

        if sampleName not in ['WH_htt_1','DY_2','top_3','top_2','top_6','Vg_1','top_4','top_5']:
        # if len(sample['name']) > 2:
            sample['name'] = sample['name'][0:1]
            if 'weights' in sample.keys():
                sample['weights'] = sample['weights'] [0:1]

# Define data to be loaded
with open("./preselections.py") as handle:
    exec handle
cut="(({0}) && ({1}))".format(supercut,preselections['OSSF'])
mvaVariables = [
   'WH3l_dphilllmet',
   'MinIf$( WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0)',
   'MinIf$( WH3l_ptOSll[], WH3l_ptOSll[Iteration$] > 0)',
   'MinIf$( WH3l_drOSll[], WH3l_drOSll[Iteration$] > 0)',
   # 'WH3l_drOSll[0]',
   # 'WH3l_drOSll[1]',
   'WH3l_ZVeto',
   # 'WH3l_mOSll[0]',
   # 'WH3l_mOSll[1]',
   'WH3l_ptlll',
   'WH3l_mtlmet[0]',
   'WH3l_mtlmet[1]',
   'WH3l_mtlmet[2]',
   # 'WH3l_ptOSll[0]',
   # 'WH3l_ptOSll[1]',
   'WH3l_dphilmet[0]',
   'WH3l_dphilmet[1]',
   'WH3l_dphilmet[2]',
   'WH3l_ptWWW',
   'WH3l_mtWWW',
   'WH3l_mlll',
   'PuppiMET_pt',
   'Alt$(Lepton_pt[0],0)',
   'Alt$(Lepton_pt[1],0)',
   'Alt$(Lepton_pt[2],0)'
]
# :    1 : WH3l_ZVeto                                      : 8.013e-02
# :    2 : MinIf$(WH3l_mOSll[],WH3l_mOSll[Iteration$]>0)   : 6.387e-02
# :    3 : MinIf$(WH3l_ptOSll[],WH3l_ptOSll[Iteration$]>0) : 6.168e-02
# :    4 : WH3l_dphilmet[0]                                : 5.700e-02
# :    5 : Alt$(Lepton_pt[0],0)                            : 5.583e-02
# :    6 : WH3l_dphilmet[2]                                : 5.460e-02
# :    7 : WH3l_ptlll                                      : 5.448e-02
# :    8 : WH3l_dphilllmet                                 : 5.393e-02
# :    9 : WH3l_mtWWW                                      : 5.162e-02
# :   10 : WH3l_mlll                                       : 5.103e-02
# :   11 : WH3l_ptWWW                                      : 5.083e-02
# :   12 : MinIf$(WH3l_drOSll[],WH3l_drOSll[Iteration$]>0) : 4.966e-02
# :   13 : PuppiMET_pt                                     : 4.907e-02
# :   14 : WH3l_mtlmet[1]                                  : 4.747e-02
# :   15 : WH3l_dphilmet[1]                                : 4.527e-02
# :   16 : Alt$(Lepton_pt[1],0)                            : 4.456e-02
# :   17 : WH3l_mtlmet[2]                                  : 4.388e-02
# :   18 : WH3l_mtlmet[0]                                  : 4.260e-02
# :   19 : Alt$(Lepton_pt[2],0)                            : 4.250e-02
