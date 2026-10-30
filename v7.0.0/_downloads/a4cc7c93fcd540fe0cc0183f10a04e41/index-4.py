import numpy as np
import matplotlib.pyplot as plt
from mantid import plots
from mantid.simpleapi import CreateWorkspace

# Generate random x and y values for two workspaces
x1 = np.arange(20)
y1 = np.random.uniform(5, 50, len(x1))  # Random values between 5 and 50

x2 = np.arange(20)
y2 = np.random.uniform(10, 55, len(x2))  # Different random values

# Create a marker workspace
w1 = CreateWorkspace(DataX=x1, DataY=y1, NSpec=1)
w1.setPlotType('marker')

# Create a second marker workspace
w2 = CreateWorkspace(DataX=x2, DataY=y2, NSpec=1)
w2.setPlotType('marker')
w2.setMarkerStyle('circle')
w2.setMarkerSize(4)

# Plot using the mantid projection
fig, ax = plt.subplots(subplot_kw={'projection': 'mantid'})
ax.plot(w1)  # First marker workspace
ax.plot(w2)  # Second marker workspace with different style marker

ax.set_title("Marker Workspace Example")  # Set plot title
ax.legend()  # Show the legend
plt.show()