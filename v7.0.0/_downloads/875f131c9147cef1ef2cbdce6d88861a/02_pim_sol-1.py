# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

_164198 = Load('164198.nxs')

fig, axes = plt.subplots(edgecolor='#ffffff', num='164198-1', subplot_kw={'projection': 'mantid'})
axes.plot(_164198, color='#2ca02c', label='164198: spec 100', linewidth=1.0, specNum=100, zorder=2.1)
axes.plot(_164198, color='#1f77b4', label='164198: spec 200', linewidth=1.0, specNum=200, zorder=2.1)
axes.errorbar(_164198, capsize=1.0, color='#ff7f0e', label='A funky label', linewidth=1.0, specNum=50)
axes.plot(_164198, color='#000000', label='164198: spec 300', linewidth=1.0, markeredgecolor='#d62728', markerfacecolor='#d62728', specNum=300, zorder=2.1)
axes.set_title('My Beautiful Plot')
axes.set_xlabel(r'Time-of-flight ($\mu s$)')
axes.set_ylabel('Counts')
axes.set_xlim([460.0, 600.0])
axes.set_ylim([1.0, 2000.0])
axes.set_yscale('log')
axes.legend() #.draggable()

#fig.show()