from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

def gaussian(x, mu, sigma):
  """Creates a Gaussian peak centered on mu and with width sigma."""
  return (1/ sigma * np.sqrt(2 * np.pi)) * np.exp( - (x-mu)**2  / (2*sigma**2))

# create two histograms with a single peak in each one
x1 = np.arange(-1, 1, 0.02)
x2 = np.arange(0.4, 1.6, 0.02)
ws1 = CreateWorkspace(UnitX="1/q", DataX=x1, DataY=gaussian(x1, 0, 0.1)+1)
ws2 = CreateWorkspace(UnitX="1/q", DataX=x2, DataY=gaussian(x2, 1, 0.05)+1)

# stitch the histograms together
stitched, scale = Stitch1D(LHSWorkspace=ws1, RHSWorkspace=ws2, StartOverlap=0.4, EndOverlap=0.6)

# plot the individual workspaces alongside the stitched one
fig, axs = plt.subplots(nrows=1, ncols=2, subplot_kw={'projection':'mantid'})

axs[0].plot(mtd['ws1'], wkspIndex=0, label='ws1')
axs[0].plot(mtd['ws2'], wkspIndex=0, label='ws2')
axs[0].legend()
axs[1].plot(mtd['stitched'], wkspIndex=0, color='k', marker='.', ls='', label='stitched')
axs[1].legend()

# uncomment the following line to show the plot window
#fig.show()