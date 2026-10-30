from mantid.simpleapi import *
import matplotlib.pyplot as plt

data = Load('MAR11060.nxs')

fig, ax = plt.subplots(subplot_kw={'projection':'mantid3d'})
ax.plot_wireframe(data, color='#1f77b4')

fig.show()