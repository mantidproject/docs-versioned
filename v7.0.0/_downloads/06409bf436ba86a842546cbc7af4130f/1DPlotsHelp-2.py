# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
from mantid.plots.utility import MantidAxType

MAR11060 = Load('MAR11060')

fig, axes = plt.subplots(edgecolor='#ffffff', ncols=2, nrows=2, num='MAR11060-1', subplot_kw={'projection': 'mantid'})
axes[0][0].plot(MAR11060, color='#1f77b4', label='MAR11060: spec 1', wkspIndex=0)
axes[0][0].set_xlabel('Time-of-flight ($\\mu s$)')
axes[0][0].set_ylabel('Counts ($\\mu s$)$^{-1}$')
legend = axes[0][0].legend(fontsize=8.0) #.set_draggable(True).legend # uncomment to set the legend draggable

axes[0][1].plot(MAR11060, color='#1f77b4', label='MAR11060: spec 2', wkspIndex=1)
axes[0][1].set_xlabel('Time-of-flight ($\\mu s$)')
axes[0][1].set_ylabel('Counts ($\\mu s$)$^{-1}$')
legend = axes[0][1].legend(fontsize=8.0) #.set_draggable(True).legend # uncomment to set the legend draggable

axes[1][0].plot(MAR11060, color='#1f77b4', label='MAR11060: spec 3', wkspIndex=2)
axes[1][0].set_xlabel('Time-of-flight ($\\mu s$)')
axes[1][0].set_ylabel('Counts ($\\mu s$)$^{-1}$')
legend = axes[1][0].legend(fontsize=8.0) #.set_draggable(True).legend # uncomment to set the legend draggable

axes[1][1].plot(MAR11060, color='#1f77b4', label='MAR11060: spec 4', wkspIndex=3)
axes[1][1].set_xlabel('Time-of-flight ($\\mu s$)')
axes[1][1].set_ylabel('Counts ($\\mu s$)$^{-1}$')
legend = axes[1][1].legend(fontsize=8.0) #.set_draggable(True).legend # uncomment to set the legend draggable

fig.show()