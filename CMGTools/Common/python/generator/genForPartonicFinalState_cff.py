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

# for comparison
ak5GenJetsParticleFinalState = ak5GenJets.clone( src = cms.InputTag("genParticlesForJets") )
ak5GenJetsParticleFinalStateNoNu = ak5GenJets.clone( src = cms.InputTag("genParticlesForJetsNoNu") )

genForParticleFinalState = cms.Sequence(
    genParticlesForJets +
    ak5GenJetsParticleFinalState
    )

genForParticleFinalStateNoNu = cms.Sequence(
    genParticlesForJetsNoNu +
    ak5GenJetsParticleFinalStateNoNu
    )
