import FWCore.ParameterSet.Config as cms

elToMuAssMaker = cms.EDFilter("ElToMuAssMaker",
    # min DR
    minDR = cms.double(0.1)
)

