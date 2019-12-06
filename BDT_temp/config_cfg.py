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
if isDEV:
    for sampleName, sample in samples.items():
        if sampleName not in ['WZ','WW','ZZ','VVV','Vg','WH_hww','WH_htt','DY','top']:
            samples.pop(sampleName)
            continue

        if len(sample['name']) > 2:
            sample['name'] = sample['name'][0:1]
            if 'weights' in sample.keys():
                sample['weights'] = sample['weights'] [0:1]


# Define data to be loaded
with open("./preselections.py") as handle:
    exec handle
cut="(({0})".format(preselections['ALL'])
mvaVariables = [
   'WH3l_dphilllmet',
   'WH3l_drOSll[0]',
   'WH3l_drOSll[1]',
   'WH3l_ZVeto',
   'WH3l_mOSll[0]',
   'WH3l_mOSll[1]',
   'WH3l_ptlll',
   'WH3l_mtlmet[0]',
   'WH3l_mtlmet[1]',
   'WH3l_ptOSll[0]',
   'WH3l_ptOSll[1]',
   'WH3l_dphilmet[0]',
   'WH3l_dphilmet[1]',
   'WH3l_ptWWW',
   'WH3l_mtWWW',
   'WH3l_mlll',
   'PuppiMET_pt',
   'Alt$(CleanJet_pt[0],0)',
   'Alt$(Lepton_pt[0],0)',
   'Alt$(Lepton_pt[1],0)',
   'Alt$(Lepton_pt[2],0)'
]

