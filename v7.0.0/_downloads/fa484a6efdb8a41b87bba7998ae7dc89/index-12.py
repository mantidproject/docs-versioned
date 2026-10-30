import matplotlib.pyplot as plt
from mantid import plots
from mantid.simpleapi import Load, FilterByTime

w = Load('CNCS_7860')
ws_filtered = FilterByTime(w, StartTime=60, StopTime=120)
fig = plt.figure()
ax1 = fig.add_subplot(211,projection='mantid')
ax2 = fig.add_subplot(212,projection='mantid')
ax1.plot(ws_filtered, LogName='ChopperStatus5',ShowTimeROI=True)
ax1.set_title('From run start')
ax2.plot(ws_filtered, LogName='ChopperStatus5',FullTime=True,ShowTimeROI=True)
ax2.set_title('Absolute time')
fig.tight_layout()
#fig.show()