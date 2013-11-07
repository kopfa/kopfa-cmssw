import FWCore.ParameterSet.Config as cms

# do not really on the default cuts implemented here,
# as they are subject to change. 
# you should override these cuts in your analysis.

#cmgMuonSel = cms.EDFilter(
#    "CmgMuonSelector",
#    src = cms.InputTag( "cmgMuon" ),
#    cut = cms.string( "pt()>15" )
#    )

cmgMuonSel = cms.EDFilter('CMGMuonProducer',
    applyFilter = cms.untracked.bool(False),
    muonLabel = cms.InputTag("cmgMuon"),
    vertexLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
    ptcut = cms.untracked.double(20),
    etacut = cms.untracked.double(2.4),
    relIso = cms.untracked.double(0.15),
)
