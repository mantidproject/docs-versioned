from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np
from mantid.plots._compatability import plotSpectrum

# Load and Read data
ws = Load(Filename="HRP39182.RAW")
x = ws.readX(0)
y = ws.readY(0)
e = ws.readE(0)

# Alter the x data
new_x = x * 1e-3

# Create a new Matrix Workspace with the altered data
new_ws = CreateWorkspace(DataX=new_x, DataY=y, DataE=e, NSpec=1,UnitX='Label')

# Set the Label for the AxisUnit
unit = new_ws.getAxis(0).getUnit()
unit.setLabel("Time-of-flight", "Milliseconds")

# Plot the new workspace
plotSpectrum(new_ws,0)