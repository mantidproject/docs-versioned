import numpy as np
import matplotlib.pyplot as plt

# Set up the data
x = np.linspace(0, 2 * np.pi)
offsets = np.linspace(0, 2*np.pi, 4, endpoint=False)
# Create array with shifted-sine curve along each column
yy = np.transpose([np.sin(x + phi) for phi in offsets])
# Plot the data
fig, ax = plt.subplots()
ax.plot(yy)

## Reset the parameters

import matplotlib as mpl
mpl.rcParams['lines.linewidth'] = 2.0
mpl.rcParams['axes.grid'] = True
mpl.rcParams['axes.facecolor'] = (0.95, 0.95, 0.95)
mpl.rcParams['grid.linestyle'] = '--'
# Plot the data
fig, ax = plt.subplots()
ax.plot(yy)