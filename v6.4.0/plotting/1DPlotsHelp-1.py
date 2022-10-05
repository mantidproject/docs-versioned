# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt

MAR11060 = Load('MAR11060')

fig, axes = plt.subplots(edgecolor='#ffffff', num='MAR11060-1', subplot_kw={'projection': 'mantid'})
axes.plot(MAR11060, color='#1f77b4', label='MAR11060: spec 1', specNum=1)
axes.plot(MAR11060, color='#ff7f0e', label='MAR11060: spec 2', specNum=2)
axes.plot(MAR11060, color='#2ca02c', label='MAR11060: spec 3', specNum=3)
axes.set_title('MAR11060')
axes.set_xlabel('Time-of-flight ($\mu s$)')
axes.set_ylabel('Counts ($\mu s$)$^{-1}$')
axes.legend()   #.draggable() # uncomment to set the legend draggable

plt.show()