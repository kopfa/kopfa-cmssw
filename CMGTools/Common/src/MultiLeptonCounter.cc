#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "AnalysisDataFormats/CMGTools/interface/Lepton.h"
#include "AnalysisDataFormats/CMGTools/interface/Muon.h"
#include "AnalysisDataFormats/CMGTools/interface/Electron.h"

#include <memory>

using namespace edm;
using namespace std;
using namespace cmg;

class MultiLeptonCounter : public edm::EDFilter
{
public:
  MultiLeptonCounter(const edm::ParameterSet& pset);
  ~MultiLeptonCounter() {};

private:
  void beginJob() {};
  void endJob() {};
  bool filter(edm::Event& event, const edm::EventSetup& eventSetup);

  bool applyFilter_;
  edm::InputTag muonsLabel_;
  edm::InputTag electronsLabel_;
  unsigned int minCount_, maxCount_;
};

MultiLeptonCounter::MultiLeptonCounter(const edm::ParameterSet& pset)
{
  applyFilter_ = pset.getUntrackedParameter<bool>("applyFilter", true);

  muonsLabel_ = pset.getUntrackedParameter<edm::InputTag>("muonsLabel");
  electronsLabel_ = pset.getUntrackedParameter<edm::InputTag>("electronsLabel");
  minCount_ = pset.getUntrackedParameter<unsigned int>("minCount", 1);
  maxCount_ = pset.getUntrackedParameter<unsigned int>("maxCount", 999);
  
}

bool MultiLeptonCounter::filter(edm::Event& event, const edm::EventSetup& eventSetup)
{
  if ( !applyFilter_ ) return true;

  unsigned int nCount = 0;

  edm::Handle<vector<cmg::Muon> > muons_;
  edm::Handle<vector<cmg::Electron> > electrons_;
  event.getByLabel(muonsLabel_, muons_);
  event.getByLabel(electronsLabel_, electrons_);

  if ( muons_.isValid() ) nCount += muons_->size();
  if ( electrons_.isValid() ) nCount += electrons_->size();

  return nCount >= minCount_ && nCount <= maxCount_;
}

DEFINE_FWK_MODULE(MultiLeptonCounter);


