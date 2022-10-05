# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

# Load the data
run = Load('Training_Exercise3a_SNS.nxs')

fig, axes = plt.subplots(subplot_kw={'projection': 'mantid'})

# Choose legend labels and colors for each curve
labels = ("sp-1", "sp-2", "sp-3", "sp-4", "sp-5")
colors = ('#FFCFC4', '#FE886F','#FE4A23', '#B82405', '#6A1300')

# Plot the first 5 spectra
for i in range(5):
    axes.plot(run, wkspIndex=i, color=colors[i], label=labels[i])

# Plot the 9th spectrum with errorbars
axes.errorbar(run, specNum=9, capsize=2.0, color='blue', label='Peak of Interest', linewidth=1.0)

# Set the X-axis limts and the Y-axis scale
axes.set_xlim(-1.5, 1.8)
plt.yscale('log')

# Give the plot a title
plt.title("Peak Evolution", fontsize=20)

# Add a legend with the chosen labels and show the plot
axes.legend()
#plt.show() #uncomment to show the plot

# Note with the Direct Matplotlib method,
# there are many more options for formatting the plot