
import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import * 
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    RandomizedParameters = cms.VPSet(),
)

points = [{'processParameters': ['4900023:m0 = 1500', '4900023:mMin = 1499', '4900023:mMax = 1501', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-1500_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 1700', '4900023:mMin = 1699', '4900023:mMax = 1701', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-1700_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 1900', '4900023:mMin = 1899', '4900023:mMax = 1901', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-1900_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 2100', '4900023:mMin = 2099', '4900023:mMax = 2101', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-2100_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 2300', '4900023:mMin = 2299', '4900023:mMax = 2301', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-2300_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 2500', '4900023:mMin = 2499', '4900023:mMax = 2501', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-2500_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 2700', '4900023:mMin = 2699', '4900023:mMax = 2701', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-2700_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 2900', '4900023:mMin = 2899', '4900023:mMax = 2901', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-2900_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 3100', '4900023:mMin = 3099', '4900023:mMax = 3101', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-3100_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 3300', '4900023:mMin = 3299', '4900023:mMax = 3301', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-3300_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 3500', '4900023:mMin = 3499', '4900023:mMax = 3501', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-3500_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 3700', '4900023:mMin = 3699', '4900023:mMax = 3701', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-3700_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 3900', '4900023:mMin = 3899', '4900023:mMax = 3901', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-3900_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 4100', '4900023:mMin = 4099', '4900023:mMax = 4101', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-4100_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 4300', '4900023:mMin = 4299', '4900023:mMax = 4301', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-4300_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 4500', '4900023:mMin = 4499', '4900023:mMax = 4501', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-4500_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 4700', '4900023:mMin = 4699', '4900023:mMax = 4701', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-4700_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 4900', '4900023:mMin = 4899', '4900023:mMax = 4901', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-4900_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}, {'processParameters': ['4900023:m0 = 5100', '4900023:mMin = 5099', '4900023:mMax = 5101', '4900023:mWidth = 0.01', '4900023:oneChannel = 1 0.982 102 4900101 -4900101', '4900023:addChannel = 1 0.003 102 1 -1', '4900023:addChannel = 1 0.003 102 2 -2', '4900023:addChannel = 1 0.003 102 3 -3', '4900023:addChannel = 1 0.003 102 4 -4', '4900023:addChannel = 1 0.003 102 5 -5', '4900023:addChannel = 1 0.003 102 6 -6', '4900001:m0 = 50000', '4900002:m0 = 50000', '4900003:m0 = 50000', '4900004:m0 = 50000', '4900005:m0 = 50000', '4900006:m0 = 50000', '4900011:m0 = 50000', '4900012:m0 = 50000', '4900013:m0 = 50000', '4900014:m0 = 50000', '4900015:m0 = 50000', '4900016:m0 = 50000', 'HiddenValley:ffbar2Zv = on', '4900101:m0 = 10', '4900111:m0 = 20', '4900211:m0 = 20', '51:m0 = 0.0', '51:isResonance = false', '4900113:m0 = 20', '4900213:m0 = 20', '53:m0 = 0.0', '53:isResonance = false', 'HiddenValley:Ngauge = 2', 'HiddenValley:spinFv = 0', 'HiddenValley:FSR = on', 'HiddenValley:fragment = on', 'HiddenValley:alphaOrder = 1', 'HiddenValley:Lambda = 35.1539', 'HiddenValley:nFlav = 2', 'HiddenValley:probVector = 0.75', '4900111:oneChannel = 1 0.05 0 51 -51', '4900111:addChannel = 1 0.0543388 91 4 -4', '4900111:addChannel = 1 0.895661 91 5 -5', '4900211:oneChannel = 1 0.05 0 51 -51', '4900211:addChannel = 1 0.0543388 91 4 -4', '4900211:addChannel = 1 0.895661 91 5 -5', '4900113:oneChannel = 1 0.05 0 53 -53', '4900113:addChannel = 1 0.19 91 2 -2', '4900113:addChannel = 1 0.19 91 1 -1', '4900113:addChannel = 1 0.19 91 3 -3', '4900113:addChannel = 1 0.19 91 4 -4', '4900113:addChannel = 1 0.19 91 5 -5', '4900213:oneChannel = 1 0.05 0 53 -53', '4900213:addChannel = 1 0.19 91 2 -2', '4900213:addChannel = 1 0.19 91 1 -1', '4900213:addChannel = 1 0.19 91 3 -3', '4900213:addChannel = 1 0.19 91 4 -4', '4900213:addChannel = 1 0.19 91 5 -5'], 'name': 'SVJ_s-channel_mMed-5100_mDark-20_rinv-0.05_alpha-peak_13TeV-pythia8', 'weight': 1.0}]

for point in points:
    basePythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock, 
        pythia8CUEP8M1SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(point['processParameters']),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'pythia8PSweightsSettings',
            'processParameters',
        )
    )

    generator.RandomizedParameters.append(
        cms.PSet(
            ConfigWeight = cms.double(point['weight']),
            ConfigDescription = cms.string(point['name']),
            PythiaParameters = basePythiaParameters,
        ),
    )

darkhadronZ2filter = cms.EDFilter("MCParticleModuloFilter",
    moduleLabel = cms.InputTag('generator'),
    particleIDs = cms.vint32(51,53),
    multipleOf = cms.uint32(4),
    absID = cms.bool(True),
)

darkquarkFilter = cms.EDFilter("MCParticleModuloFilter",
    moduleLabel = cms.InputTag('generator'),
    particleIDs = cms.vint32(4900101),
    multipleOf = cms.uint32(2),
    absID = cms.bool(True),
    min = cms.uint32(2),
    status = cms.int32(23),
)

ProductionFilterSequence = cms.Sequence(generator+darkhadronZ2filter+darkquarkFilter)
