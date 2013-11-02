import FWCore.ParameterSet.Config as cms

gen = cms.untracked.vstring(
    #'keep recoGenParticles_genParticlesStatus3_*_*',
    'keep recoGenParticles_genParticlesPruned_*_*',
    #'keep recoGenParticles_genParticles_*_*',
    #'keep recoGenParticles_genLeptonsStatus2_*_*',
    #'keep recoGenParticles_genLeptonsStatus1_*_*',    
    'keep recoGenJetedmPtrcmgPhysicsObjectWithPtrs_genJetSel_*_*',
    'keep recoGenJets_tauGenJetsSelectorAllHadrons*_*_PAT',
    'keep recoGenJets_ak5GenJetsNoNu_*_*',
    'keep *_addPileupInfo_*_*',
    'keep GenEventInfoProduct_*_*_*',
    'keep LHEEventProduct_*_*_*'
    )

