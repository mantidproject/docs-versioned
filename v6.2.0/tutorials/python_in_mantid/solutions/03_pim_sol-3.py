# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

# Load the data and extract the region of interest
data=Load('164198.nxs')
data=ExtractSpectra(data, XMin=470, XMax=490, StartWorkspaceIndex=199, EndWorkspaceIndex=209)

'''2D Plotting - Colorfill and Contour'''

# Get a figure and axes for
figC,axC = plt.subplots(ncols=2, subplot_kw={'projection':'mantid'}, figsize = (6,4))

# Plot the data as a 2D colorfill: IMPORTANT to set origin to lower
c=axC[0].imshow(data,cmap='jet', aspect='auto', origin = 'lower')

# Change the title
axC[0].set_title("Colorfill")

# Plot the data as a 2D colorfill: IMPORTANT to set origin to lower
c=axC[1].imshow(data,cmap='jet', aspect='auto', origin = 'lower')

# Overlay Contour lines
axC[1].contour(data, levels=np.linspace(0, 10000, 7), colors='white', alpha=0.5)

# Change the title
axC[1].set_title("Contour")

# Add a Colorbar with a label
cbar=figC.colorbar(c)
cbar.set_label('Counts ($\mu s$)$^{-1}$')

'''3D Plotting - Surface and Wireframe'''

# Get a different set of figure and axes with 3 subplots for 3D plotting
fig3d,ax3d = plt.subplots(ncols=2, subplot_kw={'projection':'mantid3d'}, figsize = (8,3))

# 3D plot the data, and choose colormaps and colors
ax3d[0].plot_surface(data, cmap='summer')
ax3d[1].plot_wireframe(data, color='darkmagenta')

# Add titles to the 3D plots
ax3d[0].set_title("Surface")
ax3d[1].set_title("Wireframe")

#plt.show()# uncomment to show the plots