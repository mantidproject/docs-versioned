from mantid.simpleapi import *
import matplotlib.pyplot as plt

try:
   trans1 = Load('INTER00013463')
   trans2 = Load('INTER00013464')

   trans1_wav = CreateTransmissionWorkspaceAuto(trans1)
   trans2_wav = CreateTransmissionWorkspaceAuto(trans2)

   stitched_wav, y = Stitch1D(trans1_wav, trans2_wav, UseManualScaleFactor=True, ManualScaleFactor=0.85)

   # plot the individual and stitched workspaces next to each other
   fig, axs = plt.subplots(nrows=1, ncols=2, subplot_kw={'projection':'mantid'})

   axs[0].plot(trans1_wav, wkspIndex=0, label=str(trans1_wav))
   axs[0].plot(trans2_wav, wkspIndex=0, label=str(trans2_wav))
   axs[0].legend()
   # use same y scale on both plots
   ylimits = axs[0].get_ylim()
   axs[1].plot(stitched_wav, wkspIndex=0, color='k', label='stitched')
   axs[1].legend()
   axs[1].set_ylim(ylimits)

   # uncomment the following line to show the plot window
   #fig.show()
except ValueError:
   print("Cannot load data")