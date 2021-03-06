import FWCore.ParameterSet.Config as cms

patMETHistograms = cms.EDAnalyzer(
    "GenericPatMETHistograms",
    inputCollection = cms.InputTag("patMETsAK5"),
    histograms = cms.untracked.PSet(
        met = cms.untracked.VPSet(
            cms.untracked.PSet( 
               var = cms.untracked.string('pt()'),
               nbins = cms.untracked.int32(100),
               low = cms.untracked.double(0),
               high = cms.untracked.double(1000)
               )
            ),
    
        sumEt = cms.untracked.VPSet(
            cms.untracked.PSet( 
               var = cms.untracked.string('sumEt()'),
               nbins = cms.untracked.int32(100),
               low = cms.untracked.double(0),
               high = cms.untracked.double(2000)
               )
            ),
        
        phi = cms.untracked.VPSet(
            cms.untracked.PSet( 
               var = cms.untracked.string('phi()'),
               nbins = cms.untracked.int32(100),
               low = cms.untracked.double(-3.15),
               high = cms.untracked.double(3.15)
               )
            ),
        )
    
    )
