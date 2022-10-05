from mantid.simpleapi import *
config['default.facility'] = 'ILL'
config['default.instrument'] = 'D17'
config.appendDataSearchSubDir('ILL/D17/')
name = 'Thick_HR_5'
directBeams = '397812,397806,397808'
reflectedBeams = '397826+397827,397828,397829+397830+397831+397832'
foregroundWidth = [4,5,8]
wavelengthLower = [3., 1.6, 2.]
wavelengthUpper = [27., 25., 25.]
angleOffset = 2
angleWidth = 10
ReflectometryILLAutoProcess(
    Run=reflectedBeams,
    DirectRun=directBeams,
    OutputWorkspace=name,
    SummationType='Incoherent',
    AngleOption='SampleAngle',
    DirectLowAngleFrgHalfWidth=foregroundWidth,
    DirectHighAngleFrgHalfWidth=foregroundWidth,
    DirectLowAngleBkgOffset=angleOffset,
    DirectLowAngleBkgWidth=angleWidth,
    DirectHighAngleBkgOffset=angleOffset,
    DirectHighAngleBkgWidth=angleWidth,
    ReflLowAngleFrgHalfWidth=foregroundWidth,
    ReflHighAngleFrgHalfWidth=foregroundWidth,
    ReflLowAngleBkgOffset=angleOffset,
    ReflLowAngleBkgWidth=angleWidth,
    ReflHighAngleBkgOffset=angleOffset,
    ReflHighAngleBkgWidth=angleWidth,
    WavelengthLowerBound=wavelengthLower,
    WavelengthUpperBound=wavelengthUpper,
    DeltaQFractionBinning=0.5
)
import matplotlib.pyplot as plt
from mantid import plots
plt.style.use('classic')
plt.rcParams['figure.figsize'] = (12, 7)
plt.rcParams['font.size'] = 18
wsMantid = mtd['Thick_HR_5_stitched']
fig, ax = plt.subplots(subplot_kw={'projection':'mantid'})
ax.plot(wsMantid, 'b', label="RoundRobin")
ax.errorbar(wsMantid,'rs', 'b', markersize=0.1, label=None)
ax.set_xlim(0.01, 0.2)
ax.set_ylim(0.000001, 2.)
ax.set_yscale("log")
ax.set_xscale("log")
ax.set_xlabel('Q [$\AA^{-1}$]')
ax.set_ylabel('R')
ax.legend()
#fig.show()