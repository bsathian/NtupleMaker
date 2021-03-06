import FWCore.ParameterSet.Config as cms

pfCandidateMaker = cms.EDProducer("PFCandidateMaker",
                                  #pfCandidatesTag     = cms.InputTag("particleFlow"),
                                  # pfCandidatesTag     = cms.InputTag("packedPFCandidates"),
                                  aliasPrefix         = cms.untracked.string("pfcands"),
                                  pfCandidatesTag     = cms.InputTag("packedPFCandidates"),
                                  minPt  = cms.double(5.0),
                                  #pfElectronsTag      = cms.InputTag("particleFlow","electrons"),
                                  #tracksInputTag      = cms.InputTag("generalTracks"),
                                  #vertexInputTag      = cms.InputTag("offlinePrimaryVertices"),
                                  #minDRelectron       = cms.double(0.1)
)
