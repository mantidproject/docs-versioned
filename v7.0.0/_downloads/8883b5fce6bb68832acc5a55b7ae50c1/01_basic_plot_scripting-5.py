''' ----------- Wireframe plot ----------- '''

from mantid.simpleapi import *
import matplotlib.pyplot as plt

data = Load('164198.nxs')
data=ExtractSpectra(data, XMin=470, XMax=490, StartWorkspaceIndex=260, EndWorkspaceIndex=270)

fig, ax = plt.subplots(subplot_kw={'projection':'mantid3d'})
ax.plot_wireframe(data, color='green')
#fig.show()