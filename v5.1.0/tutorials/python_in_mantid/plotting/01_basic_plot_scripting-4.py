''' ----------- Surface plot ----------- '''

from mantid.simpleapi import *
import matplotlib.pyplot as plt

data = Load('MUSR00015189.nxs')
data = mtd['data_1'] # Extract individual workspace from group

fig, ax = plt.subplots(subplot_kw={'projection':'mantid3d'})
ax.plot_surface(data)
#plt.show()