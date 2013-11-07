import FWCore.ParameterSet.Config as cms

cmgLeptonFilter = cms.EDFilter("MultiLeptonCounter",
  muonsLabel = cms.untracked.InputTag('cmgMuonSel'),
  electronsLabel = cms.untracked.InputTag('cmgElectronSel'),
  minCount = cms.untracked.uint32(2)
)
