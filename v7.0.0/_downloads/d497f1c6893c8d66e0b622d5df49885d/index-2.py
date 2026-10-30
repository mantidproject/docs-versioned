import numpy as np
import matplotlib.pyplot as plt
from mantid import plots
from mantid.simpleapi import CreateWorkspace

# Create a workspace that has a Gaussian peak
x = np.arange(20)
y0 = 10.+50*np.exp(-(x-10)**2/20)
err=np.sqrt(y0)
y = 10.+50*np.exp(-(x-10)**2/20)
y += err*np.random.normal(size=len(err))
err = np.sqrt(y)
w = CreateWorkspace(DataX=x, DataY=y, DataE=err, NSpec=1, UnitX='DeltaE')

# Plot - note that the projection='mantid' keyword is passed to all axes
fig, ax = plt.subplots(subplot_kw={'projection':'mantid'})
ax.errorbar(w,'rs') # plot the workspace with errorbars, using red squares
ax.plot(x,y0,'k-', label='Initial guess') # plot the initial guess with black line
ax.legend() # show the legend
#fig.show()