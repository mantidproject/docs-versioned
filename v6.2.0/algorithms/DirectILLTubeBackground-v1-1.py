from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np
# Load and preprocess some IN5 data
DirectILLCollectData('ILL/IN5/104007.nxs',
    OutputWorkspace='ws', OutputEPPWorkspace='epp')
# Get default hard mask + beam stop mask
DirectILLDiagnostics('ws', OutputWorkspace='diagnostics_mask')
DirectILLTubeBackground('ws', OutputWorkspace='bkg',
    EPPWorkspace='epp', DiagnosticsWorkspace='diagnostics_mask')
bkg = mtd['bkg']
# Apply the background
ws_bkg_subtracted = Subtract('ws', bkg)
# Plot the background levels of tubes in the forward direction
bkg_y = bkg.extractY()
fig, ax = plt.subplots(subplot_kw={'projection':'mantid'})
xs = np.arange(0, bkg.getNumberHistograms())
ax.plot(xs, bkg_y[:, 0])
ax.set_xlim(xmin=70000)
ax.set_xlabel('Workspace index')
ax.set_ylabel('Background')
# Uncomment the following to show the plot
#fig.show()
# Remove all workspaces
mtd.clear()