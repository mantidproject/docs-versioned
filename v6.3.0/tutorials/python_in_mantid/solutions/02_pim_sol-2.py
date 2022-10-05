# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

Load(Filename=r'EQSANS_6071_event.nxs',OutputWorkspace='run',LoadMonitors='1')
ConvertUnits(InputWorkspace='run_monitors',OutputWorkspace='run_monitors_lambda',Target='Wavelength')
Rebin(InputWorkspace='run_monitors_lambda',OutputWorkspace='run_monitors_lambda_rebinned',Params='2.5,0.1,5.5')
ConvertUnits(InputWorkspace='run',OutputWorkspace='run_lambda',Target='Wavelength')
Rebin(InputWorkspace='run_lambda',OutputWorkspace='run_lambda_rebinned',Params='2.5,0.1,5.5')
SumSpectra(InputWorkspace='run_lambda_rebinned', OutputWorkspace='run_lambda_summed')
Divide(LHSWorkspace='run_lambda_summed', RHSWorkspace='run_monitors_lambda_rebinned', OutputWorkspace='normalized')

from mantid.api import AnalysisDataService as ADS

run_lambda_summed = ADS.retrieve('run_lambda_summed')
run_monitors_lambda_rebinned = ADS.retrieve('run_monitors_lambda_rebinned')
normalized = ADS.retrieve('normalized')

fig, axes = plt.subplots(edgecolor='#ffffff', num='run_lambda_summed-1', subplot_kw={'projection': 'mantid'})
axes.plot(run_lambda_summed, color='#1f77b4', label='run_lambda_summed: spec 1', linewidth=1.0, specNum=1)
axes.plot(run_monitors_lambda_rebinned, color='#ff7f0e', label='run_monitors_lambda_rebinned: spec 1', linewidth=1.0, specNum=1)
axes.plot(normalized, color='#2ca02c', distribution=False, label='normalized: spec 1', linewidth=1.0, specNum=1)
axes.set_title('run_lambda_summed')
axes.set_xlabel('Wavelength ($\AA$)')
axes.set_ylabel('($\AA$)$^{-1}$')
axes.set_xlim([2.405, 4.5])
axes.set_yscale('log')
axes.legend() #.draggable()

#plt.show()

# NOTE: This script could be improved further with adding comments,
# and extracting and logging values for filename and binning params,
# as in Exercise 2A above.