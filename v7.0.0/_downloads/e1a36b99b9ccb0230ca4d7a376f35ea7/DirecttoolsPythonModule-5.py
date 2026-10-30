import directtools as dt
from mantid.simpleapi import *

DirectILLCollectData(Run='ILL/IN4/084447.nxs', OutputWorkspace='data')
DirectILLReduction(InputWorkspace='data', OutputWorkspace='SofQW')

E1 = 8.
dE = 2.
cut1 = LineProfile('SofQW', E1, dE, 'Horizontal')
label1 = 'At E = {} meV'.format(E1)
E2 = E1 - 4.
cut2 = LineProfile('SofQW', E2, dE, 'Horizontal')
label2 = 'At E = {} meV'.format(E2)
fig, axes = dt.plotprofiles([cut1, cut2], [label1, label2], style='m')
axes.legend()
#fig.show()