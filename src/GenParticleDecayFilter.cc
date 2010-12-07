#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include <vector>

class GenParticleDecayFilter : public edm::EDFilter
{
public:
  GenParticleDecayFilter(const edm::ParameterSet& pset);
  ~GenParticleDecayFilter() {};

  void beginJob() {};
  bool filter(edm::Event& event, const edm::EventSetup& eventSetup);
  void endJob() {};

private:
  unsigned int motherPdgId_, pdgId_;
  std::vector<unsigned int> daughterPdgIds_;
  unsigned int minCount_, maxCount_;
};

GenParticleDecayFilter::GenParticleDecayFilter(const edm::ParameterSet& pset)
{
  motherPdgId_ = pset.getUntrackedParameter<unsigned int>("motherPdgId", 0);
  pdgId_ = pset.getUntrackedParameter<unsigned int>("pdgId");
  daughterPdgIds_ = pset.getUntrackedParameter<std::vector<unsigned int> >("daughterPdgIds");
  minCount_ = pset.getUntrackedParameter<unsigned int>("minCount", 0);
  maxCount_ = pset.getUntrackedParameter<unsigned int>("maxCount", 9999);
}

bool GenParticleDecayFilter::filter(edm::Event& event, const edm::EventSetup& eventSetup)
{
  using namespace std;
  using namespace edm;
  using namespace reco;

  edm::Handle<edm::View<reco::Candidate> > particles;
  event.getByLabel(edm::InputTag("genParticles"), particles);

  unsigned int count = 0;
  for ( edm::View<reco::Candidate>::const_iterator particle = particles->begin();
        particle != particles->end(); ++particle )
  {
    if ( particle->status() != 3 ) continue;
    if ( (unsigned int)abs(particle->pdgId()) != pdgId_ ) continue;

    if ( motherPdgId_ != 0 )
    {
      // Find mother particle with status == 3
      const reco::Candidate* mother = particle->mother();
      while ( mother != 0 and mother->status() != 3 )
      {
        mother = mother->mother();
      }
      if ( !mother or mother->status() != 3 ) continue;
      if ( (unsigned int)abs(mother->pdgId()) != motherPdgId_ ) continue;
    }

    // Loop over daughters and try to match
    // At least one of daughterPdgIds matches, we accept the genParticle
    const unsigned int nDau = particle->numberOfDaughters();
    const unsigned int nPdgId = daughterPdgIds_.size();
    bool isAnythingMatched = false;
    for ( unsigned int i = 0; i < nDau; ++i )
    {
      const reco::Candidate* dau = particle->daughter(i);
      if ( !dau or dau->status() != 3 ) continue;

      for ( unsigned int j = 0; j < nPdgId; ++j )
      {
        if ( (unsigned int)abs(dau->pdgId()) == daughterPdgIds_[j] )
        {
          isAnythingMatched = true;
          break;
        }
      }
      if ( isAnythingMatched ) break;
    }
    if ( !isAnythingMatched ) continue;

    // Now we can say this particle is matching to any pdgId's in the PSet
    ++count;
  }

  if ( count < minCount_ or count > maxCount_ ) return false;

  return true;
}

DEFINE_FWK_MODULE(GenParticleDecayFilter);

