# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt

MAR11060 = Load('MAR11060')

fig, axes = plt.subplots(edgecolor='#ffffff', ncols=2, nrows=2, num='MAR11060-1', subplot_kw={'projection': 'mantid'})
axes[0][0].plot(MAR11060, color='#1f77b4', label='MAR11060: spec 1', specNum=1)
axes[0][0].set_xlabel('Time-of-flight ($\mu s$)')
axes[0][0].set_ylabel('Counts ($\mu s$)$^{-1}$')
axes[0][0].legend()   #.draggable() # uncomment to set the legend draggable

axes[0][1].plot(MAR11060, color='#1f77b4', label='MAR11060: spec 2', specNum=2)
axes[0][1].set_xlabel('Time-of-flight ($\mu s$)')
axes[0][1].set_ylabel('Counts ($\mu s$)$^{-1}$')
axes[0][1].legend()   #.draggable() # uncomment to set the legend draggable

axes[1][0].plot(MAR11060, color='#1f77b4', label='MAR11060: spec 3', specNum=3)
axes[1][0].set_xlabel('Time-of-flight ($\mu s$)')
axes[1][0].set_ylabel('Counts ($\mu s$)$^{-1}$')
axes[1][0].legend()   #.draggable() # uncomment to set the legend draggable

axes[1][1].plot(MAR11060, color='#1f77b4', label='MAR11060: spec 4', specNum=4)
axes[1][1].set_xlabel('Time-of-flight ($\mu s$)')
axes[1][1].set_ylabel('Counts ($\mu s$)$^{-1}$')
axes[1][1].legend()   #.draggable() # uncomment to set the legend draggable

plt.show()