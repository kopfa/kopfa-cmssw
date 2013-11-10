import FWCore.ParameterSet.Config as cms

# To reconstruct genjets without the neutrinos
from RecoJets.Configuration.GenJetParticles_cff import *
from RecoJets.Configuration.RecoGenJets_cff import *

genParticlesForPartonicFinalState = genParticlesForJets.clone()
genParticlesForPartonicFinalState.partonicFinalState = cms.bool(True)

genParticlesForPartonicFinalStateNoNu = genParticlesForJetsNoNu.clone()
genParticlesForPartonicFinalStateNoNu.partonicFinalState = cms.bool(True)

ak5GenJetsPartonicFinalState = ak5GenJets.clone( src = cms.InputTag("genParticlesForPartonicFinalState") )
ak5GenJetsPartonicFinalStateNoNu = ak5GenJets.clone( src = cms.InputTag("genParticlesForPartonicFinalStateNoNu") )

genForPartonicFinalState = cms.Sequence(
    genParticlesForPartonicFinalState +
    ak5GenJetsPartonicFinalState
    )

genForPartonicFinalStateNoNu = cms.Sequence(
    genParticlesForPartonicFinalStateNoNu +
    ak5GenJetsPartonicFinalStateNoNu
    )
