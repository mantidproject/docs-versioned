# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
from mantid.plots.utility import MantidAxType

MAR11060 = Load('MAR11060')

fig, axes = plt.subplots(edgecolor='#ffffff', num='MAR11060-1', subplot_kw={'projection': 'mantid'})
axes.plot(MAR11060, color='#1f77b4', label='MAR11060: spec 1', wkspIndex=0)
axes.plot(MAR11060, color='#ff7f0e', label='MAR11060: spec 2', wkspIndex=1)
axes.plot(MAR11060, color='#2ca02c', label='MAR11060: spec 3', wkspIndex=2)
axes.tick_params(axis='x', which='major', **{'gridOn': False, 'tick1On': True, 'tick2On': False, 'label1On': True, 'label2On': False, 'size': 6, 'tickdir': 'out', 'width': 1})
axes.tick_params(axis='y', which='major', **{'gridOn': False, 'tick1On': True, 'tick2On': False, 'label1On': True, 'label2On': False, 'size': 6, 'tickdir': 'out', 'width': 1})
axes.set_title('MAR11060')
axes.set_xlabel('Time-of-flight ($\\mu s$)')
axes.set_ylabel('Counts ($\\mu s$)$^{-1}$')
legend = axes.legend(fontsize=8.0).set_draggable(True).legend

fig.show()