# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np
from mantid.plots._compatability import plotSpectrum #import needed outside Workbench

'''Processing'''

# Load the spectral range of the interest of the data
ws=Load(Filename="GEM40979.raw", SpectrumMin=431, SpectrumMax=750)

# Convert to dSpacing
ws=ConvertUnits(InputWorkspace=ws, Target= "dSpacing")

# Smooth the data
ws=SmoothData(InputWorkspace=ws, NPoints=20)

'''Plotting'''

# Plot three spectra
PLOT_WINDOW = plotSpectrum(ws, [0,1,2])

# Get Figure and Axes for formatting
fig, axes = plt.gcf(), plt.gca()

# Set the scales on the x- and y-axes
axes.set_xlim(4, 6)
axes.set_ylim(0, 5e3)

# Plot index 5
plotSpectrum(ws,5, window= PLOT_WINDOW, clearWindow= False)

# Alter the Y label
axes.set_ylabel('Neutron Counts ($\AA$)$^{-1}$')

# Optionally rename the curve titles
axes.legend(["bank2 sp-431", "bank2 sp-432", "bank2 sp-433", "bank2 sp-436"])

# Give the plot a title
plt.title("Oscillations", fontsize=20)