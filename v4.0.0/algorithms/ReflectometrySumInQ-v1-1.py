import numpy as np
from mantid.simpleapi import *
import matplotlib.pyplot as plt

# Direct beam
noBackground = 'name=LinearBackground, A0=0'
direct = CreateSampleWorkspace(
    Function='User Defined',
    UserDefinedFunction=noBackground,
    NumBanks=1,
    XUnit='Wavelength',
    XMin=0., XMax=20., BinWidth=1.)
# Move the detector such that the beam is right at its center.
MoveInstrumentComponent(
    Workspace=direct,
    ComponentName='bank1',
    X=-0.008 * 4.5, Y= -0.008 * 4.5, Z=0.)
# Fill intensity for pixels in the beam
for i in [44, 45, 54, 55]:
    direct.dataY(i).fill(1.)
    direct.dataE(i).fill(0.1)
# Group detectors to form a 'line detector'. The line is vertical in this case.
groupingPattern=''
for row in range(10):
    for column in range(10):
        groupingPattern = groupingPattern + str(column * 10 + row)
        if column < 9:
            groupingPattern = groupingPattern + '+'
    if row < 9:
        groupingPattern = groupingPattern + ','
direct = GroupDetectors(
    InputWorkspace=direct,
    GroupingPattern=groupingPattern,
    Behaviour='Sum')

#Reflected beam
reflected = CreateSampleWorkspace(
    Function='User Defined',
    UserDefinedFunction=noBackground,
    NumBanks=1,
    XUnit='Wavelength',
    XMin=0., XMax=20., BinWidth=1.)
# Move the detector. This reflectometer moves vertically.
MoveInstrumentComponent(
    Workspace=reflected,
    ComponentName='bank1',
    X=-0.008 * 4.5, Y= 0.008 * 4, Z=0.)
# Create some fake reflected beam data.
Xs = reflected.readX(0)
Xs = (Xs[1:] + Xs[:-1]) / 2  # Bin edges -> points
decay = np.exp(-(Xs - 4.) / 3.)
span = decay < 1.
for i in [44, 45, 54, 55]:
    Ys = reflected.dataY(i)
    Ys.fill(1.)
    Ys[span] = decay[span]
reflected = GroupDetectors(
    InputWorkspace=reflected,
    GroupingPattern=groupingPattern,
    Behaviour='Sum')

# Now we have somewhat realistic data.
# Sum the direct beam (in lambda).
direct=SumSpectra(direct, ListOfWorkspaceIndices=[4, 5])
# Calculate (sum in Q) the reflectivity.
reflected /= direct
reflectivity = ReflectometrySumInQ(
    InputWorkspace=reflected,
    InputWorkspaceIndexSet=[4, 5],
    BeamCentre=4)

reflectivity = CropWorkspace(
    reflectivity,
    XMin=0.1, XMax=19.)

fig, axes = plt.subplots(subplot_kw={'projection': 'mantid'})
axes.plot(reflectivity)
axes.set_ylabel('"Reflectivity"')
# Uncomment to show the plot window.
#fig.show()
mtd.clear()