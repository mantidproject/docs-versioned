import directtools as dt
from mantid.simpleapi import *

DirectILLCollectData(Run='ILL/IN4/084447.nxs', OutputWorkspace='data')
DirectILLReduction(InputWorkspace='data', OutputWorkspace='SofQW')

EMin = -20.
QMax = dt.validQ('SofQW', EMin)[1]
VMax = 0.5 * dt.nanminmax('SofQW')[1]

fig, axes = dt.plotSofQW('SofQW', QMax=QMax, EMin=EMin, VMax=VMax)
#fig.show()