#!/usr/bin/env python
# Author: Tae.Jeong.Kim@cern.ch
# How to run: ./produceNtuple data
import os
import re
import sys
import time
import os,commands
import KoPFA.CommonTools.eostools as castortools

from PATCMG_cfg import *

def processSample( sample, dir, geninfo):
  
    name = sample.split("/")
    eosdir = "/eos/cms/store/caf/user/tjkim/ttbb"

    output = eosdir
    for n in range(1,3):
     output = output +"/"+name[n]
     castortools.runEOSCommand(output,'mkdir')
    output = output + "/PAT_CMG_V5_13_0"
    castortools.runEOSCommand(output,'mkdir')

    os.system("mkdir "+dir+"/"+name[1])
    os.system("mkdir "+dir+"/"+name[1]+"/Log")
    log = dir+"/"+name[1]
    out = open(log+'/PATCMG_'+name[1]+'_cfg.py','w')
    datasetInfo = ('cmgtools_group', sample,'.*root')
    process.source = datasetToSource(*datasetInfo)
    process.MessageLogger.cerr.FwkReport.reportEvery = 10000
    process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

    if geninfo is True:
      process.outcmg.outputCommands.append('keep recoGenJets_ak5GenJetsPartonicFinalStateNoNu*_*_*')
      process.outcmg.outputCommands.append('keep recoGenJets_ak5GenJetsNoNu_*_*')
      process.outcmg.outputCommands.append('keep recoGenParticles_genParticles_*_*')
      process.outcmg.outputCommands.append('keep recoGenParticles_genParticlesPruned_*_*')
    else: 
      process.outcmg.outputCommands.append('drop recoGenJets_ak5GenJetsPartonicFinalStateNoNu*_*_*')
      process.outcmg.outputCommands.append('drop recoGenJets_ak5GenJetsNoNu_*_*')
      process.outcmg.outputCommands.append('drop recoGenParticles_genParticles_*_*')
      process.outcmg.outputCommands.append('drop recoGenParticles_genParticlesPruned_*_*')

    print output
    out.write(process.dumpPython())
    out.close()
    os.system("cmsBatch0.py 1 "+log+'/PATCMG_'+name[1]+'_cfg.py'+" -o "+log+"/Log"+" -r "+output+" -b 'bsub -G u_zh -q 2nd < batchScript.sh'")

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--dataset-file", dest="filename",
                  help="dataset list", metavar="FILE")

parser.add_option("","--gen", action="store_true", dest="geninfo",help="save generator level information?")
parser.add_option("","--nogen", action="store_false", dest="geninfo",help="do not save generator level information?")

(options, args) = parser.parse_args()

filename = options.filename
datasets = open(filename,'r').read().split('\n')[:-1]

currdir = commands.getoutput('pwd')
print "you are "+currdir

outdir = currdir+"/Out/"

#to save log information in local
os.system("rfmkdir Out")
os.system("rfmkdir "+outdir)

for s in datasets:
  processSample(s, outdir, options.geninfo)
  #time.sleep(60)
