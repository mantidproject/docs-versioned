from mantid.simpleapi import *
import directtools as dt
ws = CreateSampleWorkspace(Function='Quasielastic Tunnelling', NumBanks=1, BankPixelWidth=20)
AddSampleLog(ws, 'wavelength', '6.26', 'Number', 'Angstrom')
SetInstrumentParameter(ws, ParameterName='l2', ParameterType='String', Value='5')
SofTT = SofTwoThetaTOF(ws, AngleStep=1)
fig, axes = dt.subplots()
axes.pcolor(SofTT)
axes.set_xlim(0.)
# Uncomment the line below to show the plot.
#fig.show()