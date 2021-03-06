#ifndef DQM_L1TMONITORCLIENT_L1TOCCUPANCYCLIENT_H
#define DQM_L1TMONITORCLIENT_L1TOCCUPANCYCLIENT_H

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include <FWCore/Framework/interface/EDAnalyzer.h>

#include "DQMServices/Core/interface/DQMStore.h"
#include "DQMServices/Core/interface/MonitorElement.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"

#include <memory>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <TH1F.h>
#include <TH1D.h>
#include <TH2F.h>
#include <TF1.h>
#include <TProfile2D.h>

class L1TTestsSummary: public edm::EDAnalyzer {

  public:

    // Constructor
    L1TTestsSummary(const edm::ParameterSet& ps);
  
    // Destructor
    virtual ~L1TTestsSummary();
 
  protected:

    // Job methods
    void beginJob(void);
    void endJob();

    // Run methods
    void beginRun(const edm::Run& r, const edm::EventSetup& c);
    void endRun(const edm::Run& r, const edm::EventSetup& c);

    // Luminosity Block methods
    void beginLuminosityBlock(const edm::LuminosityBlock& lumiSeg,const edm::EventSetup& context);
    void endLuminosityBlock  (const edm::LuminosityBlock& lumiSeg,const edm::EventSetup& c);       // DQM Client Diagnostic

    void analyze(const edm::Event& e, const edm::EventSetup& c) ;

  private:

    DQMStore*         mDBE;        //store service
    edm::ParameterSet mParameters; //parameter set from python

    // bool
    bool mVerbose;             // verbose mode
    bool mMonitorL1TRate;      // If we are going to monitor the L1TRate Module
    bool mMonitorL1TSync;      // If we are going to monitor the L1TSync Module
    bool mMonitorL1TOccupancy; // If we are going to monitor the L1TOccupancy Module

    // int
    int binYRate,binYSync,binYOccpancy; // What bin in Y corresponds to which test in L1TSummary

    // string
    std::string mL1TRatePath;      // Path to histograms produced by L1TRate Module
    std::string mL1TSyncPath;      // Path to histograms produced by L1TSync Module
    std::string mL1TOccupancyPath; // Path to histograms produced by L1TOccupancy Module

    // vector
    std::vector<int> mProcessedLS; // Already processed Luminosity Blocks

    // MonitorElement
    MonitorElement* mL1TRateMonitor;
    MonitorElement* mL1TSyncMonitor;
    MonitorElement* mL1TOccupancyMonitor;
    MonitorElement* mL1TSummary;
    
  // Private Functions
  private:

    void updateL1TRateMonitor();
    void updateL1TSyncMonitor();
    void updateL1TOccupancyMonitor();
    void updateL1TSummary();
};

#endif
