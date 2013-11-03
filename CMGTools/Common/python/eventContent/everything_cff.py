import FWCore.ParameterSet.Config as cms

from CMGTools.Common.eventContent.particleFlow_cff import *
from CMGTools.Common.eventContent.traditional_cff import *
from CMGTools.Common.eventContent.trigger_cff import *
from CMGTools.Common.eventContent.gen_cff import *
from CMGTools.Common.eventContent.eventCleaning_cff import *
from CMGTools.Common.eventContent.runInfoAccounting_cff import *

patObjects = cms.untracked.vstring(
    'drop patTaus_selectedPat*_*_*',
    'drop patElectrons_*_*_*',
    'keep patElectrons_patElectronsWithTrigger_*_*',
    'drop patMuons_*_*_*',
    'keep patMuons_patMuonsWithTrigger_*_*',
    'drop patElectrons_*AK5NoPUSub_*_*',
    'drop patMuons_*AK5NoPUSub_*_*',    
    #COLIN : the following should be in traditional_cff
    'keep edmMergeableCounter_*_*_*',
    'drop cmgPhotons_selectedPat*_*_*',
    'keep recoVertexs_offlinePrimaryVertices_*_*',
    'drop recoPFMETs_pfMetForRegression__*',
    #'keep double_*_rho_*',
    'keep double_ak5PFJets_rho_RECO',
    'keep double_kt6PFJets_rho_RECO',
    'drop *_nJetsPtGt1_*_*',
    'drop recoPFMETs_nopuMet__*',
    'drop recoPFMETs_puMet__*',
    'drop recoPFMETs_pcMet__*',    
    'drop recoPFMETs_tkMet__*',
    'drop recoCaloMETs_*_*_*',
    'drop *_ak5SoftTrackJetsForVbfHbb__*'
    )

#everything = particleFlow + traditional + patObjects + runInfoAccounting + trigger + gen + eventCleaning
everything = particleFlow + patObjects + trigger + gen + eventCleaning

MHT = particleFlowMHT + traditionalMHT
