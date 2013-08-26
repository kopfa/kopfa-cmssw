import FWCore.ParameterSet.Config as cms

process = cms.Process("PAT")

from CMGTools.Production.datasetToSource import *
datasetInfo = ('cmgtools_group', '/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v2/AODSIM/V5_B','.*root')
process.source = datasetToSource(
    *datasetInfo
    )
process.source.fileNames = process.source.fileNames[:-1]
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )


process.load('CMGTools.Common.PAT.PATCMG_cff')
process.load("KoPFA.CommonTools.genForPartonicFinalState_cff")
process.load("KoPFA.CMGAnalyzer.ttbar2bFilter_cfi")

process.genJet.cfg = cms.PSet(
       inputCollection = cms.InputTag("ak5GenJetsPartonicFinalStateNoNu")
       )

process.ttbar2bFilter.type = cms.untracked.int32(1) 

process.p = cms.Path(
    process.genForPartonicFinalStateNoNu
    +process.genForParticleFinalStateNoNu
    +process.genSequence
    +process.ttbar2bFilter
    )

########################################################

process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('patTuple.root'),
                               # save only events passing the full path
                               SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               # save PAT Layer 1 output; you need a '*' to
                               # unpack the list of commands 'patEventContent'
                               outputCommands = cms.untracked.vstring(
                                  'drop *',
                                  'keep recoGenJets_ak5GenJetsPartonicFinalStateNoNu*_*_*',
                                  'keep recoGenJets_ak5GenJetsParticleFinalStateNoNu*_*_*',
                                  'keep recoGenParticles_*_*_*'
                                 )
                               )

process.outpath = cms.EndPath(
    process.out
    )

########################################################
## Below, stuff that you probably don't want to modify
########################################################
## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

## Options and Output Report
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('vallot.root')
)
