import matplotlib.pyplot as plt
from mantid import plots
from mantid.simpleapi import *

ws=Load('GEM40979.raw')
Number = 12 # How many Spectra to Plot

prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color'] # 10 colors in default cycle

'''Change the following two parameters as you wish'''
custom_colors = ['#0000ffff', 'salmon','#00ff00ff'] # I've chosen Blue, Salmon, Green

fig = plt.figure(figsize = (10,10))
ax1 = plt.subplot(211,projection='mantid')
for i in range(Number):
   ax1.plot(ws, specNum = i+1, color=colors[i%len(colors)])
ax1.set_title('Default')
ax1.legend()

ax2 = plt.subplot(212,projection='mantid')
for i in range(Number):
   ax2.plot(ws, specNum= i+1, color=custom_colors[i%len(custom_colors)])
ax2.set_title('Custom')
ax2.legend()

fig.suptitle('Line Plots: Color Cycle', fontsize='x-large')
#fig.show()