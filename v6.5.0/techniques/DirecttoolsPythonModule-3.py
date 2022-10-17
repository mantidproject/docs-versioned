import directtools as dt
from mantid.simpleapi import *
import warnings

DirectILLCollectData(Run='ILL/IN4/084447.nxs', OutputWorkspace='data')
DirectILLReduction(InputWorkspace='data', OutputWorkspace='SofQW')

Q = 2.
dQ = 0.2
# plotconstQ produces a warning on some versions of numpy.
# The "with" statement catches this warning so that the automated
# builds don't fail.
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=UserWarning)
    fig, axes, cuts = dt.plotconstQ('SofQW', Q, dQ)
    #fig.show()