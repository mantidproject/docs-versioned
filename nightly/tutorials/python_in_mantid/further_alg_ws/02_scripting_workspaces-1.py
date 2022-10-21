# import mantid algorithms, matplotlib and plotSpectrum
from mantid.simpleapi import *
import matplotlib.pyplot as plt
from mantid.plots._compatability import plotSpectrum #import needed outside Workbench

ws1 = CreateSampleWorkspace()

# Plot index 1,2 and 3 from ws1, with errorbars and will a waterfall offset
plotSpectrum(ws1,spectrum_nums=[1,2,3],error_bars=True, waterfall=True)