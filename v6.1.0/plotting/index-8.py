import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np

Cmap_Name = 'Beach' # Colormap name
Res = 500 # Resolution of your Colormap (number of steps in colormap)

Re = Res-1
Cmap = np.zeros((Res,4))
for i in range(Res):
  '''Input functions inside float(), Divide by Res to normalise'''
  Cmap[i][0] = float(Res)   / Res       #Red   #just 1
  Cmap[i][1] = float(i)     / Re        #Green #+ve i divisible by Res-1 = Re
  Cmap[i][2] = float(Res-i)**2 / Res**2 #Blue  #Make sure Norm_factor correct
  Cmap[i][3] = 1
  '''Checks all values b/w 0 and 1'''
  for j in range(4):
      if Cmap[i][j] > 1:
          print(Cmap[i])
          raise ValueError('Values must be between 0 and 1, one of the above is > 1')
      if Cmap[i][j] < 0:
          print(Cmap[i])
          raise ValueError('Values must be between 0 and 1, one of the above is Negative')
      else:
          pass

#np.savetxt("C:\Path\to\File\Filename.txt",Cmap) #uncomment to save to file

Listed_CustomCmap = ListedColormap(Cmap, name = Cmap_Name)
plt.register_cmap(name = Cmap_Name, cmap = Listed_CustomCmap)

# Create and register the reverse colormap
Reverse = np.zeros((Res,4))
for i in range(Res):
  for j in range(4):
      Reverse[i][j] = Cmap[Res-(i+1)][j]

Listed_CustomCmap_r = ListedColormap(Reverse, name=(Cmap_Name + '_r') )
plt.register_cmap(name=(Cmap_Name + '_r'), cmap= Listed_CustomCmap_r)

from mantid.simpleapi import Load, ConvertToMD, BinMD, ConvertUnits, Rebin
from mantid import plots
from matplotlib.colors import LogNorm
data = Load('CNCS_7860')
data = ConvertUnits(InputWorkspace=data,Target='DeltaE', EMode='Direct', EFixed=3)
data = Rebin(InputWorkspace=data, Params='-3,0.025,3', PreserveEvents=False)
md = ConvertToMD(InputWorkspace=data,QDimensions='|Q|',dEAnalysisMode='Direct')
sqw = BinMD(InputWorkspace=md,AlignedDim0='|Q|,0,3,100',AlignedDim1='DeltaE,-3,3,100')

fig, ax = plt.subplots(subplot_kw={'projection':'mantid'})
c = ax.pcolormesh(sqw, cmap='Beach', norm=LogNorm())
cbar=fig.colorbar(c)
cbar.set_label('Intensity (arb. units)') #add text to colorbar
#fig.show()