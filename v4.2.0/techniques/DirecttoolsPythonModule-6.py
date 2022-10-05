import directtools as dt
from mantid.simpleapi import *

DirectILLCollectData(Run='ILL/IN4/084447.nxs', OutputWorkspace='data')
DirectILLReduction(InputWorkspace='data', OutputWorkspace='SofQW', OutputSofThetaEnergyWorkspace='SofTW')
dosFromStw = ComputeIncoherentDOS('SofTW')
dosFromSqw = ComputeIncoherentDOS('SofQW')
fig, axes = dt.plotDOS([dosFromStw, dosFromSqw], labels=[r'from $S(2\theta, E)$', r'from $S(Q,E)$'])
#fig.show()