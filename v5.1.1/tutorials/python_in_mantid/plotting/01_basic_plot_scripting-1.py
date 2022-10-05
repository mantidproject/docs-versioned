''' ----------- Image > imshow() ----------- '''

from mantid.simpleapi import *
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

data = Load('MAR11060')

fig, axes = plt.subplots(subplot_kw={'projection':'mantid'})

# IMPORTANT to set origin to lower
c = axes.imshow(data, origin = 'lower', cmap='viridis', aspect='auto', norm=LogNorm())
cbar=fig.colorbar(c)
cbar.set_label('Counts ($\mu s$)$^{-1}$') #add text to colorbar
#plt.show()