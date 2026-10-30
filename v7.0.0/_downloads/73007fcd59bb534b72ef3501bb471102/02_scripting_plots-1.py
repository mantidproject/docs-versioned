from mantid.simpleapi import *
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

#Example data
exp_decay = CreateSampleWorkspace(Function='User Defined',
                                  UserDefinedFunction='\
                                  name=ExpDecay,Lifetime = 20,Height = 200;name=Gaussian,\
                                  PeakCentre=50, Height=10, Sigma=3',
                                  XMax=100, BinWidth=2)

#Create figure and axes
fig, axes = plt.subplots(ncols=2,nrows=1,subplot_kw={'projection': 'mantid'})

# Plot with errorbars on the left set of axes
axes[0].plot(exp_decay, specNum=1, color='red', label='400 K', linewidth=1.0, drawstyle='steps')
axes[0].set_title('Steps and Grids')
axes[0].xaxis.set_minor_locator(AutoMinorLocator())
axes[0].grid(True, which = 'both', axis = 'both') # major/minor, x/y

# Add an inset, use trial and error to find the right location
inset = fig.add_axes([0.77, 0.70, 0.18, 0.18],projection='mantid') #[left, bottom, width, height]
inset.plot(exp_decay, specNum=5, color='blue', label='Log Peak', marker ='.')
plt.yscale('log') #only affects the most recently called axes
inset.set_xlim(40, 60), inset.set_ylim(5, 20)
inset.xaxis.set_minor_locator(AutoMinorLocator()) #inserts 5 minor b/w each major
inset.tick_params(which='minor', width = 0.5, length=4, color='b', direction='in', top='on')

#Plot on the right set of axes
axes[1].errorbar(exp_decay, specNum=1, capsize=2.0, errorevery=5, color='green', label='spec 1', linestyle='--')
axes[1].set_xlabel('Time-of-flight ($\mu s$)', fontsize = 12, fontstyle = 'italic', fontweight = 'bold')
axes[1].set_ylabel('Counts ($\mu s$)$^{-1}$')
axes[1].set_title('Errorbars and Insets')

#Use tight layout for subplots and create a legend
plt.tight_layout()
fig.legend(loc='center right')

#fig.show()