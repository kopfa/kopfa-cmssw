
import FWCore.ParameterSet.Config as cms

source = cms.Source(
	"PoolSource",
	noEventSort = cms.untracked.bool(True),
	duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
	fileNames = cms.untracked.vstring()
)
source.fileNames.extend([
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_0.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_1.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_10.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_11.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_12.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_13.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_14.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_15.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_16.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_17.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_18.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_19.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_2.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_20.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_21.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_22.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_23.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_24.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_25.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_26.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_27.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_28.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_29.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_3.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_30.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_31.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_32.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_33.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_34.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_35.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_36.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_37.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_38.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_39.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_4.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_40.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_41.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_42.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_43.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_44.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_45.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_46.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_47.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_48.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_49.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_5.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_50.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_51.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_52.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_6.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_7.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_8.root',
		'/store/cmst3/user/cmgtools/CMG/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_10_0/cmgTuple_9.root',
])
