import numpy as np
import matplotlib.pyplot as plt
from mantid.simpleapi import CreateWorkspace
from mantid import plots

# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)
ws1=CreateWorkspace(t,data1,UnitX='MomentumTransfer')
ws2=CreateWorkspace(t,data2,UnitX='MomentumTransfer')

fig, ax1 = plt.subplots(subplot_kw={'projection':'mantid'})
color = 'red'
ax1.plot(ws1,'r-')
ax1.set_ylabel('exp', color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'blue'
ax2.plot(ws2, color=color)
ax2.set_ylabel('sin', color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
#fig.show()