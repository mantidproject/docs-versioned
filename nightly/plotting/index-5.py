import numpy as np
import matplotlib.pyplot as plt
from mantid import plots
from mantid.simpleapi import CreateWorkspace, Fit

# Create a workspace that has a Gaussian peak
x = np.arange(20)
y0 = 10.+50*np.exp(-(x-10)**2/20)
err=np.sqrt(y0)
y = 10.+50*np.exp(-(x-10)**2/20)
y += err*np.random.normal(size=len(err))
err = np.sqrt(y)
w = CreateWorkspace(DataX=x, DataY=y, DataE=err, NSpec=1, UnitX='DeltaE')
result = Fit(Function='name=LinearBackground,A0=10,A1=0.;name=Gaussian,Height=60.,PeakCentre=10.,Sigma=3.',
             InputWorkspace='w',
             Output='w',
             OutputCompositeMembers=True)
# The handle to the output workspace is result.OutputWorkspace. The first spectrum is the data,
# the second is the fit, the third is the difference. Subsequent spectra are the calculated
# functions of each of the components of the fit (here LinearBackground and Gaussian)
# Note that the difference spectrum has 0 errors. One can copy the errors from data
result.OutputWorkspace.setE(2,result.OutputWorkspace.readE(0))

#do the plotting
fig, [ax_top, ax_bottom] = plt.subplots(figsize=(9, 6),
                                        nrows=2,
                                        ncols=1,
                                        sharex=True,
                                        gridspec_kw={'height_ratios':[2,1]},
                                        subplot_kw={'projection':'mantid'})

ax_top.errorbar(result.OutputWorkspace,'rs',wkspIndex=0, label='Data')
ax_top.plot(result.OutputWorkspace,'b-',wkspIndex=1, label='Fit')
ax_top.legend()
ax_top.set_xlabel('')
ax_top.set_ylabel('Neutron counts')
ax_top.tick_params(axis='both', direction='in')
ax_bottom.errorbar(result.OutputWorkspace,'ko',wkspIndex=2)
ax_bottom.tick_params(axis='both', direction='in')
ax_bottom.set_ylabel('Difference')
fig.tight_layout()
#fig.show()