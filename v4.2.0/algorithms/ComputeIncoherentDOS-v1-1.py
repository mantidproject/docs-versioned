from mantid import mtd
from mantid.simpleapi import *
import matplotlib.pyplot as plt

ws = DirectILLCollectData('ILL/IN4/087294.nxs')
DirectILLReduction(ws, OutputWorkspace='sqw', OutputSofThetaEnergyWorkspace='stw')
temperature = ws.run().getProperty('sample.temperature').value
dos = ComputeIncoherentDOS('stw',  Temperature=temperature, EnergyBinning='0, Emax')

fig, axis = plt.subplots(subplot_kw={'projection':'mantid'})
axis.errorbar(dos)
axis.set_title('Density of states from $S(2\\theta,W)$')
# Uncomment the line below to show the plot.
#fig.show()
mtd.clear()