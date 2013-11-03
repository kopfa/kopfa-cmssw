import FWCore.ParameterSet.Config as cms

patLeptonFilter = cms.EDFilter("MultiLeptonCounter",
  leptons = cms.untracked.VInputTag('patMuonsWithTrigger','patElectronsWithTrigger'),
  minCount = cms.untracked.uint32(2)
)
