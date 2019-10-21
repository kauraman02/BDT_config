#!/usr/bin/env python
from ROOT import TMVA, TFile, TTree, TCut, TChain
from subprocess import call
from os.path import isfile

import config_cfg as config

# Setup TMVA
def runJob():
    TMVA.Tools.Instance()
    TMVA.PyMethodBase.PyInitialize()

    output = TFile.Open('TMVA.root', 'RECREATE')
    factory = TMVA.Factory('TMVAClassification', output,
            '!V:!Silent:Color:DrawProgressBar:Transformations=D,G:AnalysisType=Classification')

    dataloader = TMVA.DataLoader('dataset')
    for br in config.mvaVariables:
        dataloader.AddVariable(br)

    for sampleName, sample in config.samples.items():
        if config.structure[sampleName]['isData']==1:
            continue

        sample['tree'] = TChain("Events")
        for f in sample['name']:
            sample['tree'].Add(f)

        if config.structure[sampleName]['isSignal']==1:
            dataloader.AddSignalTree(sample['tree'], 1.0)
        else:
            dataloader.AddBackgroundTree(sample['tree'], 1.0)
        # output_dim += 1
    dataloader.PrepareTrainingAndTestTree(TCut(config.cut),'nTrain_Signal=1000:nTrain_Background=7000:SplitMode=Random:NormMode=NumEvents:!V')#SSSF
    factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=25:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=5:NegWeightTreatment=IgnoreNegWeightsInTraining" )#SSSF

    # config.selectedModel(config.modelName, input_dim, output_dim)
    # factory.BookMethod(dataloader, TMVA.Types.kPyKeras, "PyKeras", config.tmvaKerasMethodDetail)

    # Book methods
    # factory.BookMethod(dataloader, TMVA.Types.kFisher, 'Fisher',
            # '!H:!V:Fisher:VarTransform=D,G')

    # Run training, test and evaluation
    factory.TrainAllMethods()
    factory.TestAllMethods()
    factory.EvaluateAllMethods()

    output.Close()

if __name__ == "__main__":
    runJob()
