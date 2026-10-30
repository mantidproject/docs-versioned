# import mantid algorithms, matplotlib and plotSpectrum
from mantid.simpleapi import *
import matplotlib.pyplot as plt

CNCS_7860_event = Load('CNCS_7860_event')

CNCS_7860_event_high = FilterByLogValue(InputWorkspace='CNCS_7860_event', LogName='SampleTemp', MinimumValue=279.94, LogBoundary='Left')
CNCS_7860_event_low = FilterByLogValue(InputWorkspace='CNCS_7860_event', LogName='SampleTemp', MaximumValue=279.94, LogBoundary='Left')

fig, axes = plt.subplots(edgecolor='#ffffff', ncols=2, nrows=3, num='CNCS_7860_even: FilterByLogValue - SampleTemp 279.94', figsize = (7,10), subplot_kw={'projection': 'mantid'})

'''Plot Data'''

axes[0][1].plot(CNCS_7860_event, color='green', label='Full Data: spec 1000', specNum=1000)
axes[0][1].set_xlabel('Time-of-flight ($\\mu s$)')
axes[0][1].set_ylabel('Counts ($\\mu s$)$^{-1}$')
axes[0][1].set_title('Full Temp Range: spec 1000')

axes[1][1].plot(CNCS_7860_event_high, color='green', label='High Temp Data: spec 1000', specNum=1000)
axes[1][1].set_xlabel('Time-of-flight ($\\mu s$)')
axes[1][1].set_ylabel('Counts ($\\mu s$)$^{-1}$')
axes[1][1].set_title('High Temp: spec 1000')

axes[2][1].plot(CNCS_7860_event_low, color='green', label='Low Temp Data: spec 1000', specNum=1000)
axes[2][1].set_xlabel('Time-of-flight ($\\mu s$)')
axes[2][1].set_ylabel('Counts ($\\mu s$)$^{-1}$')
axes[2][1].set_title('Low Temp: spec 1000')

'''Plot Temperature Sample Log'''

axes[0][0].axhline(279.94, color='red')
axes[0][0].plot(CNCS_7860_event, ExperimentInfo=0, Filtered=True, LogName='SampleTemp', color='#1f77b4', drawstyle='steps-post', label='SampleTemp (K)')
axes[0][0].set_xlabel('Time (s)')
axes[0][0].set_ylabel('SampleTemp (K)')
axes[0][0].set_title('Sample Log Temperature: All')
temp_x_limit = axes[0][0].get_xlim()
temp_y_limit = axes[0][0].get_ylim()

axes[1][0].axhline(279.94, color='red')
axes[1][0].plot(CNCS_7860_event_high, ExperimentInfo=0, Filtered=True, LogName='SampleTemp', color='#1f77b4', drawstyle='steps-post', label='SampleTemp (K)')
axes[1][0].set_xlabel('Time (s)')
axes[1][0].set_ylabel('SampleTemp (K)')
axes[1][0].set_title('Sample Log Temperature: High')
axes[1][0].set_ylim(temp_y_limit)
axes[1][0].set_xlim(temp_x_limit[0]-145,temp_x_limit[1]-145)

axes[2][0].axhline(279.94, color='red')
axes[2][0].plot(CNCS_7860_event_low, ExperimentInfo=0, Filtered=True, LogName='SampleTemp', color='#1f77b4', drawstyle='steps-post', label='SampleTemp (K)')
axes[2][0].set_xlabel('Time (s)')
axes[2][0].set_ylabel('SampleTemp (K)')
axes[2][0].set_title('Sample Log Temperature: Low')
axes[2][0].set_xlim(temp_x_limit)
axes[2][0].set_ylim(temp_y_limit)

fig.tight_layout()
fig.show()