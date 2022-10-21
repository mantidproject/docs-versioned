''' ----------- Pseudocolormesh > pcolormesh() ----------- '''

from mantid.simpleapi import *
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

data = Load('CNCS_7860')
data = ConvertUnits(InputWorkspace=data,Target='DeltaE', EMode='Direct', EFixed=3)
data = Rebin(InputWorkspace=data, Params='-3,0.025,3', PreserveEvents=False)
md = ConvertToMD(InputWorkspace=data,QDimensions='|Q|',dEAnalysisMode='Direct')
sqw = BinMD(InputWorkspace=md,AlignedDim0='|Q|,0,3,100',AlignedDim1='DeltaE,-3,3,100')

fig, ax = plt.subplots(subplot_kw={'projection':'mantid'})
c = ax.pcolormesh(sqw, cmap='plasma', norm=LogNorm())
cbar=fig.colorbar(c)
cbar.set_label('Intensity (arb. units)') #add text to colorbar
#plt.show()