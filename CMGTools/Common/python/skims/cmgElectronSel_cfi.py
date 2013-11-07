import FWCore.ParameterSet.Config as cms

# do not really on the default cuts implemented here,
# as they are subject to change. 
# you should override these cuts in your analysis.

#cmgElectronSel = cms.EDFilter(
#    "CmgElectronSelector",
#    src = cms.InputTag("cmgElectron"),
#    cut = cms.string( "pt()>20 " )
#    )

cmgElectronSel = cms.EDFilter('CMGElectronProducer',
    applyFilter = cms.untracked.bool(False),
    electronLabel = cms.InputTag("cmgElectron"),
    vertexLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
    rhoIsoLabel =  cms.untracked.InputTag('kt6PFJets','rho'),
    ptcut = cms.untracked.double(20),
    etacut = cms.untracked.double(2.4),
    mvacut = cms.untracked.double(0.5),
    relIso = cms.untracked.double(0.15),
    numberOfHits = cms.untracked.uint32(0),
)

