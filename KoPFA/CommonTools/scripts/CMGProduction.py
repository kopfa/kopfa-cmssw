#!/usr/bin/env python
# Author: Tae.Jeong.Kim@cern.ch
# How to run: ./produceNtuple data
import os
import re
import sys
import imp
import fnmatch
import time
import os,commands
import KoPFA.CommonTools.eostools as castortools

def processSample( sampleline, dir, geninfo, tag):
  
    sample = sampleline.split("%")
    name = sample[1].split("/")
    eosdir = "/eos/cms/store/caf/user/tjkim/ttbb"

    output = eosdir
    for n in range(1,3):
     output = output +"/"+name[n]
     castortools.runEOSCommand(output,'mkdir')
    output = output + "/"+tag
    print output
    castortools.runEOSCommand(output,'mkdir')

    os.system("mkdir "+dir+"/"+name[1])
    os.system("mkdir "+dir+"/"+name[1]+"/"+tag)
    os.system("mkdir "+dir+"/"+name[1]+"/"+tag+"/Log")
    log = dir+"/"+name[1]+"/"+tag
    out = open(log+'/run_'+name[1]+'_cfg.py','w')
    print sample[0]
    print sample[1]

    toInsert = [
       "\n",
       "datasetInfo = ('"+sample[0]+"','"+sample[1]+"',"+"'.*root')\n",
       "process.MessageLogger.cerr.FwkReport.reportEvery = 10000\n",
       "process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )\n"
       "process.source = datasetToSource( *datasetInfo ) \n"
    ]

    outputContent = []
    if geninfo is True:
       outputContent = [
         "\n"
         "process.outcmg.outputCommands.append('keep recoGenJets_ak5GenJetsPartonicFinalStateNoNu*_*_*')\n",
         "process.outcmg.outputCommands.append('keep recoGenJets_ak5GenJetsNoNu_*_*')\n",
         "process.outcmg.outputCommands.append('keep recoGenParticles_genParticles_*_*')\n",
         "process.outcmg.outputCommands.append('keep recoGenParticles_genParticlesPruned_*_*')\n"
       ]
    else: 
      outputContent = [
         "\n"
         "process.outcmg.outputCommands.append('drop recoGenJets_ak5GenJetsPartonicFinalStateNoNu*_*_*')\n",
         "process.outcmg.outputCommands.append('drop recoGenJets_ak5GenJetsNoNu_*_*')\n",
         "process.outcmg.outputCommands.append('drop recoGenParticles_genParticles_*_*')\n",
         "process.outcmg.outputCommands.append('drop recoGenParticles_genParticlesPruned_*_*')\n"
       ]

    print output
    out.writelines(config)
    out.writelines( toInsert )
    out.writelines( outputContent )
    out.close()
    os.system("cmsBatch0.py 1 "+log+'/run_'+name[1]+'_cfg.py'+" -o "+log+"/Log"+" -r "+output+" -b 'bsub -G u_zh -q 2nd < batchScript.sh'")

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--dataset-file", dest="filename", help="dataset list", metavar="FILE")
parser.add_option("", "--cfg", dest="cfg", help="template config", metavar="FILE")
parser.add_option("-t", "", dest="tag", help="release tag")

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

# load cfg script
config = file(options.cfg).readlines()

for s in datasets:
  processSample(s, outdir, options.geninfo, options.tag)
  #time.sleep(60)
