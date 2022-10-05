import directtools as dt
from mantid.simpleapi import *

DirectILLCollectData(Run='ILL/IN4/084447.nxs', OutputWorkspace='data')
DirectILLReduction(InputWorkspace='data', OutputWorkspace='SofQW')

Q1 = 2.
Q2 = 3.
dQ = 0.2
fig, axes, cuts = dt.plotconstQ('SofQW', [Q1, Q2], dQ)
#fig.show()