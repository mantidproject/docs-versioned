from mantid.simpleapi import *
from mantid.plots._compatability import plotSpectrum

# The input data set
inputData = "HRP39182"
# Load the file
Load(Filename=inputData+".RAW",OutputWorkspace=inputData,Cache="If Slow")

# First do the analysis without prompt pulse removal so that we can compare the difference
# Align the detectors (incoporates unit conversion to d-Spacing)
cal_file = "hrpd_new_072_01_corr.cal"
ApplyDiffCal(InstrumentWorkspace=inputData, CalibrationFile=cal_file)
ConvertUnits(InputWorkspace=inputData, OutputWorkspace="aligned-withpulse", Target="dSpacing")
# Focus the data
DiffractionFocussing(InputWorkspace="aligned-withpulse",OutputWorkspace="focussed-withpulse",GroupingFileName=cal_file)

# Remove the prompt pulse, which occurs at at 20,000 microsecond intervals. The bin width comes from a quick look at the data
for i in range(0,5):
  min = 19990 + (i*20000)
  max = 20040 + (i*20000)
  MaskBins(InputWorkspace=inputData,OutputWorkspace=inputData,XMin=min,XMax=max)

# Align the detectors (on the data with the pulse removed incoporates unit conversion to d-Spacing)
ApplyDiffCal(InstrumentWorkspace=inputData, CalibrationFile=cal_file)
ConvertUnits(InputWorkspace=inputData, OutputWorkspace="aligned-withoutpulse", Target="dSpacing")
# Focus the data
DiffractionFocussing(InputWorkspace="aligned-withoutpulse",OutputWorkspace="focussed-withoutpulse",GroupingFileName=cal_file)
# Subract the processed data with and without pulse from eachother
Subtract(LHSWorkspace="focussed-withpulse", RHSWorkspace="focussed-withoutpulse", OutputWorkspace="difference")

# Now plot a focussed spectrum with and without prompt peak removal so that you can see the difference
plotSpectrum(["focussed-withoutpulse","difference", "focussed-withpulse"],0)