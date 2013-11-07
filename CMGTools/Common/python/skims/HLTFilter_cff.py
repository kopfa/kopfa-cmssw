import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.hltHighLevel_cfi import *

## to separate for data and MC
#for MuEG dataset
#MC
hltHighLevelFilter = hltHighLevel.clone()
hltHighLevelFilter.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
hltHighLevelFilter.HLTPaths = cms.vstring(
    'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*','HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*',
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*',
    'HLT_Mu17_Mu8_v*','HLT_Mu17_TkMu8_v*'     
)
hltHighLevelFilter.throw = cms.bool(False)

