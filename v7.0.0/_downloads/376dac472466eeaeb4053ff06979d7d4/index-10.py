import matplotlib.pyplot as plt
from mantid import plots
from mantid.simpleapi import Load

w=Load('CNCS_7860')
fig = plt.figure()
ax1 = fig.add_subplot(211,projection='mantid')
ax2 = fig.add_subplot(212,projection='mantid')
ax1.plot(w, LogName='ChopperStatus5')
ax1.set_title('From run start')
ax2.plot(w, LogName='ChopperStatus5',FullTime=True)
ax2.set_title('Absolute time')
fig.tight_layout()
#fig.show()