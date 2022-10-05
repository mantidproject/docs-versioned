''' ----------- Wireframe plot ----------- '''

from mantid.simpleapi import *
import matplotlib.pyplot as plt

data = Load('PG3_733.nxs')

fig, ax = plt.subplots(subplot_kw={'projection':'mantid3d'})
ax.plot_wireframe(data, color='green')
#plt.show()