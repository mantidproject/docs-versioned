import matplotlib.pyplot as plt
from mantid import plots
from mantid.simpleapi import Load
w=Load('CNCS_7860')
fig, ax = plt.subplots(subplot_kw={'projection':'mantid'})
ax.plot(w,LogName='ChopperStatus5')
axt=ax.twiny()
plots.plotfunctions.plot(axt,w,LogName='ChopperStatus5', FullTime=True)
#fig.show()