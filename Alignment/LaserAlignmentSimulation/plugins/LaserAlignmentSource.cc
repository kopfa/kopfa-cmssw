/** \file LaserAlignmentSource.cc
 *  Source to be used for the Simulation of the Laser Alignment System
 *  an empty MCHepEvent will be generated (needed by OscarProducer). The actual simulation of 
 *  the laser beams is done in the SimWatcher attached to OscarProducer
 *
 *  $Date: 2009/01/05 11:05:26 $
 *  $Revision: 1.5 $
 *  \author Maarten Thomas
 */
// system include files
#include "FWCore/Framework/interface/Event.h"

// user include files
#include "Alignment/LaserAlignmentSimulation/plugins/LaserAlignmentSource.h"
#include "FWCore/Framework/interface/InputSourceMacros.h" 

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"

//
// constructors and destructor
//
LaserAlignmentSource::LaserAlignmentSource(const edm::ParameterSet& iConfig, 
					   const edm::InputSourceDescription& iDescription) :
  GeneratedInputSource(iConfig, iDescription),
  theEvent(0)
{
  //register your products
  produces<edm::HepMCProduct>();

  //now do what ever other initialization is needed
}


LaserAlignmentSource::~LaserAlignmentSource()
{
  // no need to cleanup theEvent since it's done in HepMCProduct
}

// ------------ method called to produce the event  ------------
bool LaserAlignmentSource::produce(edm::Event& iEvent)
{
  // create the event
  theEvent = new HepMC::GenEvent();

  // create a primary vertex
  HepMC::GenVertex * theVtx = new HepMC::GenVertex(HepMC::FourVector(0.,0.,0.));

  // add a particle to the vertex; this is needed to avoid crashes in OscarProducer. Use a 
  // electron neutrino, with zero energy and mass
  HepMC::GenParticle * theParticle = new HepMC::GenParticle(HepMC::FourVector(0.,0.,0.,0.),12,1);
  
  theVtx->add_particle_out(theParticle);

  // add the vertex to the event
  theEvent->add_vertex(theVtx);

  // set the event number
  theEvent->set_event_number(event());
  // set the signal process id
  theEvent->set_signal_process_id(20);

  // create an empty output collection
  std::auto_ptr<edm::HepMCProduct> theOutput(new edm::HepMCProduct());
  theOutput->addHepMCData(theEvent);
   
  // put the output to the event
  iEvent.put(theOutput);

  return true;
}

//define this as a plug-in

DEFINE_FWK_INPUT_SOURCE(LaserAlignmentSource);
