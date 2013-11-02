import FWCore.ParameterSet.Config as cms

# from PhysicsTools.PatAlgos.patSequences_cff import *
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cff import *
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import selectedPatJets

jetSource = 'ak5PFJets'

# corrections 
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import *
patJetCorrFactors.src = jetSource
# will need to add L2L3 corrections in the cfg
patJetCorrFactors.levels = ['L1FastJet', 'L2Relative', 'L3Absolute']
patJetCorrFactors.payload = 'AK5PF'
patJetCorrFactors.useRho = True

patJets.jetSource = jetSource
patJets.addJetCharge = False
patJets.embedCaloTowers = False
patJets.embedPFCandidates = False
patJets.addAssociatedTracks = False

# b tagging 
from RecoJets.JetAssociationProducers.ak5JTA_cff import *
ak5JetTracksAssociatorAtVertex.jets = jetSource
from RecoBTag.Configuration.RecoBTag_cff import * # btagging sequence
softMuonTagInfos.jets = jetSource
softElectronTagInfos.jets = jetSource

## add secondar vertex mass information
## can be used in analysis level: jet->sourcePtr()->get()->userFloat("secvtxMass"); 
patJets.addTagInfos = True
patJets.tagInfoSources = cms.VInputTag(
   cms.InputTag("secondaryVertexTagInfos")
   )
patJets.userData.userFunctions = cms.vstring( "? hasTagInfo('secondaryVertex') && tagInfoSecondaryVertex('secondaryVertex').nVertices() > 0 ? "
                                                     "tagInfoSecondaryVertex('secondaryVertex').secondaryVertex(0).p4().mass() : 0",
                                              "? hasTagInfo('secondaryVertex') && tagInfoSecondaryVertex('secondaryVertex').nVertices() > 0 ? "
                                                     "tagInfoSecondaryVertex('secondaryVertex').flightDistance(0).value() : 0",
                                              "? hasTagInfo('secondaryVertex') && tagInfoSecondaryVertex('secondaryVertex').nVertices() > 0 ? "
                                                     "tagInfoSecondaryVertex('secondaryVertex').flightDistance(0).error() : 0",
)
patJets.userData.userFunctionLabels = cms.vstring('secvtxMass','Lxy','LxyErr')

# parton and gen jet matching

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import *
patJetPartonMatch.src = jetSource
patJetGenJetMatch.src = jetSource
patJetGenJetMatch.matched = 'ak5GenJets'

from PhysicsTools.PatAlgos.mcMatchLayer0.jetFlavourId_cff import *
patJetPartonAssociation.jets = jetSource

jetMCSequence = cms.Sequence(
    patJetPartonMatch +
    patJetGenJetMatch
    )

PATJetSequence = cms.Sequence(
#    ak5PFJetsSel + 
    jetMCSequence +
    ak5JetTracksAssociatorAtVertex + 
    btagging + 
    patJetCorrFactors +
    patJetFlavourId +
    patJets 
    )
