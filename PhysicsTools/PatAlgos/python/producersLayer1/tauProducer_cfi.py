import FWCore.ParameterSet.Config as cms

patTaus = cms.EDProducer("PATTauProducer",
    # input
    tauSource = cms.InputTag("hpsPFTauProducer"),

    # add user data
    userData = cms.PSet(
      # add custom classes here
      userClasses = cms.PSet(
        src = cms.VInputTag('')
      ),
      # add doubles here
      userFloats = cms.PSet(
        src = cms.VInputTag('')
      ),
      # add ints here
      userInts = cms.PSet(
        src = cms.VInputTag('')
      ),
      # add candidate ptrs here
      userCands = cms.PSet(
        src = cms.VInputTag('')
      ),
      # add "inline" functions here
      userFunctions = cms.vstring(),
      userFunctionLabels = cms.vstring()
    ),

    # jet energy corrections
    addTauJetCorrFactors = cms.bool(False),
    tauJetCorrFactorsSource = cms.VInputTag(cms.InputTag("patTauJetCorrFactors")),

    # embedding objects (for Calo- and PFTaus)
    embedLeadTrack = cms.bool(False), ## embed in AOD externally stored leading track
    embedSignalTracks = cms.bool(False), ## embed in AOD externally stored signal tracks
    embedIsolationTracks = cms.bool(False), ## embed in AOD externally stored isolation tracks
    # embedding objects (for PFTaus only)
    embedLeadPFCand = cms.bool(False), ## embed in AOD externally stored leading PFCandidate
    embedLeadPFChargedHadrCand = cms.bool(False), ## embed in AOD externally stored leading PFChargedHadron candidate
    embedLeadPFNeutralCand = cms.bool(False), ## embed in AOD externally stored leading PFNeutral Candidate
    embedSignalPFCands = cms.bool(False), ## embed in AOD externally stored signal PFCandidates
    embedSignalPFChargedHadrCands = cms.bool(False), ## embed in AOD externally stored signal PFChargedHadronCandidates
    embedSignalPFNeutralHadrCands = cms.bool(False), ## embed in AOD externally stored signal PFNeutralHadronCandidates
    embedSignalPFGammaCands = cms.bool(False), ## embed in AOD externally stored signal PFGammaCandidates
    embedIsolationPFCands = cms.bool(False), ## embed in AOD externally stored isolation PFCandidates
    embedIsolationPFChargedHadrCands = cms.bool(False), ## embed in AOD externally stored isolation PFChargedHadronCandidates
    embedIsolationPFNeutralHadrCands = cms.bool(False), ## embed in AOD externally stored isolation PFNeutralHadronCandidates
    embedIsolationPFGammaCands = cms.bool(False), ## embed in AOD externally stored isolation PFGammaCandidates

    # embed IsoDeposits
    isoDeposits = cms.PSet(
        pfAllParticles = cms.InputTag("tauIsoDepositPFCandidates"),
        pfChargedHadron = cms.InputTag("tauIsoDepositPFChargedHadrons"),
        pfNeutralHadron = cms.InputTag("tauIsoDepositPFNeutralHadrons"),
        pfGamma = cms.InputTag("tauIsoDepositPFGammas")
    ),

    # user defined isolation variables the variables defined here will be accessible
    # via pat::Tau::userIsolation(IsolationKeys key) with the key as defined in
    # DataFormats/PatCandidates/interface/Isolation.h
    #
    # (set Pt thresholds for PFChargedHadrons (PFGammas) to 1.0 (1.5) GeV,
    # matching the thresholds used when computing the tau iso. discriminators
    # in RecoTauTag/RecoTau/python/PFRecoTauDiscriminationByIsolation_cfi.py)
    userIsolation = cms.PSet(
        pfAllParticles = cms.PSet(
            src = cms.InputTag("tauIsoDepositPFCandidates"),
            deltaR = cms.double(0.5),
            threshold = cms.double(0.)
        ),
        pfChargedHadron = cms.PSet(
            src = cms.InputTag("tauIsoDepositPFChargedHadrons"),
            deltaR = cms.double(0.5),
            threshold = cms.double(0.)
        ),
        pfNeutralHadron = cms.PSet(
            src = cms.InputTag("tauIsoDepositPFNeutralHadrons"),
            deltaR = cms.double(0.5),
            threshold = cms.double(0.)
        ),
        pfGamma = cms.PSet(
            src = cms.InputTag("tauIsoDepositPFGammas"),
            deltaR = cms.double(0.5),
            threshold = cms.double(0.)
        )
    ),

    # tau ID (for efficiency studies)
    addTauID     = cms.bool(True),
    tauIDSources = cms.PSet(
        # configure many IDs as InputTag <someName> = <someTag>
        # you can comment out those you don't want to save some
        # disk space
        decayModeFinding = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding"),
        byCombinedIsolationDeltaBetaCorrRaw = cms.InputTag("hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr"),
        byVLooseCombinedIsolationDeltaBetaCorr = cms.InputTag("hpsPFTauDiscriminationByVLooseCombinedIsolationDBSumPtCorr"),
        byLooseCombinedIsolationDeltaBetaCorr = cms.InputTag("hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr"),
        byMediumCombinedIsolationDeltaBetaCorr = cms.InputTag("hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr"),
        byTightCombinedIsolationDeltaBetaCorr = cms.InputTag("hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr"),
        byIsolationMVAraw = cms.InputTag("hpsPFTauDiscriminationByIsolationMVAraw"),
        byLooseIsolationMVA = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVA"),
        byMediumIsolationMVA = cms.InputTag("hpsPFTauDiscriminationByMediumIsolationMVA"),
        byTightIsolationMVA = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVA"),
        byIsolationMVA2raw = cms.InputTag("hpsPFTauDiscriminationByIsolationMVA2raw"),
        byLooseIsolationMVA2 = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVA2"),
        byMediumIsolationMVA2 = cms.InputTag("hpsPFTauDiscriminationByMediumIsolationMVA2"),
        byTightIsolationMVA2 = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVA2"), 
        againstElectronLoose = cms.InputTag("hpsPFTauDiscriminationByLooseElectronRejection"),
        againstElectronMedium = cms.InputTag("hpsPFTauDiscriminationByMediumElectronRejection"),
        againstElectronTight = cms.InputTag("hpsPFTauDiscriminationByTightElectronRejection"),
        againstElectronMVA = cms.InputTag("hpsPFTauDiscriminationByMVAElectronRejection"),
        againstElectronMVA2raw = cms.InputTag("hpsPFTauDiscriminationByMVA2rawElectronRejection"),
        againstElectronMVA2category = cms.InputTag("hpsPFTauDiscriminationByMVA2rawElectronRejection:category"),                     
        againstElectronVLooseMVA2 = cms.InputTag("hpsPFTauDiscriminationByMVA2VLooseElectronRejection"),
        againstElectronLooseMVA2 = cms.InputTag("hpsPFTauDiscriminationByMVA2LooseElectronRejection"),
        againstElectronMediumMVA2 = cms.InputTag("hpsPFTauDiscriminationByMVA2MediumElectronRejection"),
        againstElectronTightMVA2 = cms.InputTag("hpsPFTauDiscriminationByMVA2TightElectronRejection"),                             
        againstMuonLoose = cms.InputTag("hpsPFTauDiscriminationByLooseMuonRejection"),
        againstMuonMedium = cms.InputTag("hpsPFTauDiscriminationByMediumMuonRejection"),
        againstMuonTight = cms.InputTag("hpsPFTauDiscriminationByTightMuonRejection"),
        againstMuonLoose2 = cms.InputTag("hpsPFTauDiscriminationByLooseMuonRejection2"),
        againstMuonMedium2 = cms.InputTag("hpsPFTauDiscriminationByMediumMuonRejection2"),
        againstMuonTight2 = cms.InputTag("hpsPFTauDiscriminationByTightMuonRejection2"),
        byCombinedIsolationDeltaBetaCorrRaw3Hits = cms.InputTag("hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits"),
        byLooseCombinedIsolationDeltaBetaCorr3Hits = cms.InputTag("hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits"),
        byMediumCombinedIsolationDeltaBetaCorr3Hits = cms.InputTag("hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits"),
        byTightCombinedIsolationDeltaBetaCorr3Hits = cms.InputTag("hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits"),
        againstElectronMVA3raw = cms.InputTag("hpsPFTauDiscriminationByMVA3rawElectronRejection"),
        againstElectronMVA3category = cms.InputTag("hpsPFTauDiscriminationByMVA3rawElectronRejection:category"),
        againstElectronLooseMVA3 = cms.InputTag("hpsPFTauDiscriminationByMVA3LooseElectronRejection"),
        againstElectronMediumMVA3 = cms.InputTag("hpsPFTauDiscriminationByMVA3MediumElectronRejection"),
        againstElectronTightMVA3 = cms.InputTag("hpsPFTauDiscriminationByMVA3TightElectronRejection"),
        againstElectronVTightMVA3 = cms.InputTag("hpsPFTauDiscriminationByMVA3VTightElectronRejection"),
        againstElectronDeadECAL = cms.InputTag("hpsPFTauDiscriminationByDeadECALElectronRejection")
      ),

    # mc matching configurables
    addGenMatch      = cms.bool(True),
    embedGenMatch    = cms.bool(True),
    genParticleMatch = cms.InputTag("tauMatch"),
    addGenJetMatch   = cms.bool(True),
    embedGenJetMatch = cms.bool(True),
    genJetMatch      = cms.InputTag("tauGenJetMatch"),

    # efficiencies
    addEfficiencies = cms.bool(False),
    efficiencies    = cms.PSet(),

    # resolution
    addResolutions  = cms.bool(False),
    resolutions     = cms.PSet()
)

NoUpdateDiscriminators=False
try:
    from RecoTauTag.Configuration.updateHPSPFTaus_cff import *
except ImportError:
    NoUpdateDiscriminators=True

if NoUpdateDiscriminators:
    patTaus.tauIDSources = cms.PSet(
                         decayModeFinding = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding"),
                         byVLooseCombinedIsolationDeltaBetaCorr = cms.InputTag("hpsPFTauDiscriminationByVLooseCombinedIsolationDBSumPtCorr"),
                         byLooseCombinedIsolationDeltaBetaCorr = cms.InputTag("hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr"),
                         byMediumCombinedIsolationDeltaBetaCorr = cms.InputTag("hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr"),
                         byTightCombinedIsolationDeltaBetaCorr = cms.InputTag("hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr"),
                         againstElectronLoose = cms.InputTag("hpsPFTauDiscriminationByLooseElectronRejection"),
                         againstElectronMedium = cms.InputTag("hpsPFTauDiscriminationByMediumElectronRejection"),
                         againstElectronTight = cms.InputTag("hpsPFTauDiscriminationByTightElectronRejection"),
                         againstElectronMVA = cms.InputTag("hpsPFTauDiscriminationByMVAElectronRejection"),
                         againstMuonLoose = cms.InputTag("hpsPFTauDiscriminationByLooseMuonRejection"),
                         againstMuonMedium = cms.InputTag("hpsPFTauDiscriminationByMediumMuonRejection"),
                         againstMuonTight = cms.InputTag("hpsPFTauDiscriminationByTightMuonRejection")
                     )
