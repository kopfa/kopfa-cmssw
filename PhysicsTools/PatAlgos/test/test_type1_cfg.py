------------------------------------------------------------
INFO   : cleaning has been removed. Switching output from
         clean PAT candidates to selected PAT candidates.
Adapting PF Muons 
***************** 
WARNING: particle based isolation must be studied

 muon source: cms.InputTag("pfIsolatedMuonsPFlow")
 isolation  : cms.PSet(
    pfNeutralHadrons = cms.InputTag("muPFIsoValueNeutral04PFlow"),
    pfChargedAll = cms.InputTag("muPFIsoValueChargedAll04PFlow"),
    pfPUChargedHadrons = cms.InputTag("muPFIsoValuePU04PFlow"),
    pfPhotons = cms.InputTag("muPFIsoValueGamma04PFlow"),
    pfChargedHadrons = cms.InputTag("muPFIsoValueCharged04PFlow")
)
 isodeposits: 
cms.PSet(
    pfNeutralHadrons = cms.InputTag("muPFIsoDepositNeutralPFlow"),
    pfChargedAll = cms.InputTag("muPFIsoDepositChargedAllPFlow"),
    pfPUChargedHadrons = cms.InputTag("muPFIsoDepositPUPFlow"),
    pfPhotons = cms.InputTag("muPFIsoDepositGammaPFlow"),
    pfChargedHadrons = cms.InputTag("muPFIsoDepositChargedPFlow")
)

Adapting PF Electrons 
********************* 
WARNING: particle based isolation must be studied

 PF electron source: cms.InputTag("pfIsolatedElectronsPFlow")
 isolation  :
cms.PSet(
    pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral04PFIdPFlow"),
    pfChargedAll = cms.InputTag("elPFIsoValueChargedAll04PFIdPFlow"),
    pfPUChargedHadrons = cms.InputTag("elPFIsoValuePU04PFIdPFlow"),
    pfPhotons = cms.InputTag("elPFIsoValueGamma04PFIdPFlow"),
    pfChargedHadrons = cms.InputTag("elPFIsoValueCharged04PFIdPFlow")
)
 isodeposits: 
cms.PSet(
    pfNeutralHadrons = cms.InputTag("elPFIsoDepositNeutralPFlow"),
    pfChargedAll = cms.InputTag("elPFIsoDepositChargedAllPFlow"),
    pfPUChargedHadrons = cms.InputTag("elPFIsoDepositPUPFlow"),
    pfPhotons = cms.InputTag("elPFIsoDepositGammaPFlow"),
    pfChargedHadrons = cms.InputTag("elPFIsoDepositChargedPFlow")
)

removing traditional isolation
Temporarily switching off photons completely
WARNING: called applyPostfix for module/sequence cleanPatCandidateSummary which is not in patDefaultSequencePFlow!
---------------------------------------------------------------------
INFO   : some objects have been removed from the sequence. Switching 
         off PAT cross collection cleaning, as it might be of limited
         sense now. If you still want to keep object collection cross
         cleaning within PAT you need to run and configure it by hand
WARNING: called applyPostfix for module/sequence countPatCandidates which is not in patDefaultSequencePFlow!
WARNING: called applyPostfix for module/sequence cleanPatMuons which is not in patDefaultSequencePFlow!
WARNING: called applyPostfix for module/sequence cleanPatJets which is not in patDefaultSequencePFlow!
WARNING: called applyPostfix for module/sequence cleanPatPhotons which is not in patDefaultSequencePFlow!
WARNING: called applyPostfix for module/sequence cleanPatElectrons which is not in patDefaultSequencePFlow!
WARNING: called applyPostfix for module/sequence cleanPatTaus which is not in patDefaultSequencePFlow!
WARNING: called applyPostfix for module/sequence cleanPatCandidateSummary which is not in patDefaultSequencePFlow!
------------------------------------------------------------
INFO   : cleaning has been removed. Switching output from
         clean PAT candidates to selected PAT candidates.
Switching to PFJets,   AK5
************************ 
input collection:  cms.InputTag("pfNoTauPFlow")

The btaginfo below will be written to the jet collection in the PATtuple (default is all, see PatAlgos/PhysicsTools/python/tools/jetTools.py)

impactParameterTagInfos
secondaryVertexTagInfos
softMuonTagInfos
secondaryVertexNegativeTagInfos
secondaryVertexNegativeTagInfos
inclusiveSecondaryVertexFinderTagInfos
softElectronTagInfos

The bdiscriminators below will be written to the jet collection in the PATtuple (default is all, see PatAlgos/PhysicsTools/python/tools/jetTools.py)
jetBProbabilityBJetTags
jetProbabilityBJetTags
trackCountingHighPurBJetTags
trackCountingHighEffBJetTags
simpleSecondaryVertexHighEffBJetTags
simpleSecondaryVertexHighPurBJetTags
combinedSecondaryVertexBJetTags
combinedSecondaryVertexMVABJetTags
softMuonBJetTags
softMuonByPtBJetTags
softMuonByIP3dBJetTags
simpleSecondaryVertexNegativeHighEffBJetTags
simpleSecondaryVertexNegativeHighPurBJetTags
negativeTrackCountingHighEffJetTags
negativeTrackCountingHighPurJetTags
combinedInclusiveSecondaryVertexBJetTags
combinedMVABJetTags
