''' ----------- Contour overlay ----------- '''

from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

data = Load('SANSLOQCan2D.nxs')

fig, axes = plt.subplots(subplot_kw={'projection':'mantid'})

# IMPORTANT to set origin to lower
c = axes.imshow(data, origin = 'lower', cmap='viridis', aspect='auto')

# Overlay contours
axes.contour(data, levels=np.linspace(10, 60, 6), colors='yellow', alpha=0.5)

cbar=fig.colorbar(c)
cbar.set_label('Counts ($\mu s$)$^{-1}$') #add text to colorbar
#plt.show()