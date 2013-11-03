import FWCore.ParameterSet.Config as cms


particleFlowJets = cms.untracked.vstring(
    #'keep *_cmgPFJetSel*_*_*',
    'keep *_cmgPFJetSelCHS_*_*',
    'drop *_cmgPFJetLead*_*_*',    
    'drop *_cmgPFBaseJetLead*_*_*',
    'drop cmgAbstractPhysicsObjects_*PF*Jet*_*_*',
    'drop *_cmgPFJet*JetId*Failed_*_*',
    # here add all PF jet objects, even the base ones. 
    'drop *_cmgStructuredPFJetSel*_*_*',
    )

particleFlowMET = cms.untracked.vstring(
    #'keep  *_cmgPFMET*_*_*',
    'keep  *_cmgPFMET_*_*',
    #'keep *_cmgPFMETSel*_*_*',
    # 'keep  *_cmgMETPFCandidates*_*_*',
    # here add the other PF-based MET objects, even the base ones. 
    )

# to be added to the output module if needed
particleFlowMHT = cms.untracked.vstring(
    'keep  *_cmgMHTPFJet30*_*_*'
    )

particleFlowMuons = cms.untracked.vstring(
    # does not look like PF?     
    'keep *_cmgMuonSel*_*_*',
    'drop *_cmgDiMuonSel*_*_*',
    'drop *_cmg*Muon*AK5NoPUSub*_*_*'
    )

particleFlowTaus = cms.untracked.vstring(
    # does not look like PF?     
    'keep *_cmgTauSel*_*_*',
    'keep *_cmgDiTauSel*_*_*'
    )

particleFlowElectrons = cms.untracked.vstring(
    'keep *_cmgElectronSel*_*_*',
    'drop *_cmgDiElectronSel*_*_*',
    'drop *_cmg*Electron*AK5NoPUSub*_*_*'
    )

particleFlowPhotons = cms.untracked.vstring(
    # does not look like PF? 
    'keep *_cmgPhotonSel*_*_*',
    'keep *_cmgDiPhotonSel*_*_*'
    )

particleFlowW = cms.untracked.vstring(
    # does not look like PF? 
    'keep *_cmgWENuSel*_*_*',
    'keep *_cmgWMuNuSel*_*_*',
    'keep *_cmgWTauNu_*_*'                                  
    )

particleFlowHemispheres = cms.untracked.vstring(
    'keep *_cmgHemi_*_*',
    'keep *_cmgDiHemi_*_*',
    )

particleFlowMisc = cms.untracked.vstring(
    # 'keep *_simpleParticleFlow_*_*',
    'keep *_deltaPhiJetMET_*_*',
    'keep *_pfMetSignificance*_*_*',
    'keep double_kt6PFJets*_rho_*',
    'keep int_*Size_*_*',
    'keep double_vertexWeight*_*_*',
    #Jose: needed for tau embedded samples
    'keep double_generator_weight_EmbeddedRECO'
    )

#particleFlow = particleFlowJets + particleFlowMET + particleFlowMuons + particleFlowTaus + particleFlowElectrons + particleFlowPhotons + particleFlowW + particleFlowHemispheres + particleFlowMisc
particleFlow = particleFlowJets + particleFlowMET + particleFlowMuons + particleFlowElectrons 


particleFlowBase = cms.untracked.vstring(
    'keep *_cmgPFBaseJetSel*_*_*',
    # here add the other generic PF objects
    )
