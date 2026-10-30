import directtools as dt
from mantid.simpleapi import *

DirectILLCollectData(Run='ILL/IN4/084447.nxs', OutputWorkspace='data')
DirectILLReduction(InputWorkspace='data', OutputWorkspace='SofQW')

fig, ax = dt.plotSofQW('SofQW')
#fig.show()