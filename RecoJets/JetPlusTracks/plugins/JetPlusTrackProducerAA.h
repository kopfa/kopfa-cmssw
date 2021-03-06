// -*- C++ -*-
//
// Package:    JetPlusTracks
// Class:      JetPlusTrackProducerAA
// 
/**\class JetPlusTrackProducerAA JetPlusTrackProducerAA.cc RecoJets/JetPlusTracks/src/JetPlusTrackProducerAA.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Olga Kodolova,40 R-A12,+41227671273,
//         Created:  Fri Feb 19 10:14:02 CET 2010
// $Id: JetPlusTrackProducerAA.h,v 1.1 2010/03/04 13:12:37 kodolova Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "RecoJets/JetPlusTracks/interface/JetPlusTrackCorrector.h"
#include "RecoJets/JetPlusTracks/interface/ZSPJPTJetCorrector.h"
#include "DataFormats/JetReco/interface/JPTJetCollection.h"
#include "DataFormats/JetReco/interface/JPTJet.h"

//=>
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "DataFormats/Math/interface/Point3D.h"
#include <vector>
#include "RecoJets/JetAssociationAlgorithms/interface/JetTracksAssociationDR.h"
#include "DataFormats/JetReco/interface/TrackExtrapolation.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "DataFormats/HcalDetId/interface/HcalDetId.h"
//=>

#include <string>

//
// class declaration
//

class JetPlusTrackProducerAA : public edm::EDProducer {
   public:
      explicit JetPlusTrackProducerAA(const edm::ParameterSet&);
      ~JetPlusTrackProducerAA();
      virtual void beginJob();
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob();
////     reco::TrackRefVector calculateBGtracksJet(reco::JPTJetCollection&, std::vector <reco::TrackRef>&);

      reco::TrackRefVector calculateBGtracksJet(reco::JPTJetCollection&, std::vector <reco::TrackRef>&,  
                                                 edm::Handle <std::vector<reco::TrackExtrapolation> >&,
                                                                                 reco::TrackRefVector&);

 private:
      
// Data      
      JetPlusTrackCorrector*        mJPTalgo;
      ZSPJPTJetCorrector*              mZSPalgo; 
      edm::InputTag                 src;
      edm::InputTag                 srcPVs_;
      std::string                   alias;
      bool                          vectorial_;  
      bool                          useZSP;
      edm::InputTag                 mTracks;
      double                        mConeSize;
      reco::TrackBase::TrackQuality trackQuality_;

//=>
      edm::InputTag mExtrapolations;
//=>
      // ----------member data ---------------------------
};
