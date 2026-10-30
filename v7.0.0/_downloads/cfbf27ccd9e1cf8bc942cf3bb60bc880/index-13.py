import matplotlib.pyplot as plt
import numpy as np
from mantid import plots
from mantid.simpleapi import CreateWorkspace, FFT
from matplotlib import rcParams
import warnings

x=np.linspace(0,10,250)
y=np.cos(2*np.pi*1.1*x)*np.exp(-x/7.)
err=np.sqrt(0.01+x/200.)
w=CreateWorkspace(x,y,err,UnitX='tof')
fft=FFT(w)

# make all ticks point in
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'

fig, ax = plt.subplots(subplot_kw={'projection':'mantid'})
ax.errorbar(w,'ks')
ax.set_ylabel('Asymmetry')
ax.set_ylim(-1.5,2)
ax_inset=fig.add_axes([0.7,0.72,0.2,0.2],projection='mantid')
ax_inset.plot(fft,specNum=6)
ax_inset.set_xlim(0,2)
ax_inset.set_xlabel('Frequency (MHz)')
ax_inset.set_ylabel('|FFT|')
# note that thight_layout will produce a warning here "This figure includes
# Axes that are not compatible with tight_layout, so its results might be incorrect."
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=UserWarning)
    fig.tight_layout()
#fig.show()