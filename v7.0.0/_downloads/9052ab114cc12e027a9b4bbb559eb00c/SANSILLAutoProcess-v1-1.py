from mantid.simpleapi import *
import matplotlib.pyplot as plt

config.setFacility('ILL')
config['default.instrument'] = 'D33'
config.appendDataSearchSubDir('ILL/D33/')

absorber = '002227'

tr_beam = '002192'

can_tr = '002193'

empty_beam = '002219'

can = '002228'

mask = 'D33Mask2.nxs'

sample_names = ['H2O', 'D2O', 'AgBE', 'F127_D2O', 'F127_D2O_Anethol']
sample_legends = ['H$_2$O', 'D$_2$O', 'AgBE', 'F127 D$_2$O', 'F127 D$_2$O Anethol']

samples = ['002229', '001462', '001461', '001463', '001464']

transmissions = ['002194', '002195', '', '002196', '002197']

# Autoprocess every sample
for i in range(len(samples)):
    SANSILLAutoProcess(
        SampleRuns=samples[i],
        SampleTransmissionRuns=transmissions[i],
        MaskFiles=mask,
        AbsorberRuns=absorber,
        BeamRuns=empty_beam,
        ContainerRuns=can,
        ContainerTransmissionRuns=can_tr,
        TransmissionBeamRuns=tr_beam,
        CalculateResolution='None',
        OutputWorkspace=sample_names[i]
    )

fig, ax = plt.subplots(subplot_kw={'projection':'mantid'})

plt.yscale('log')
plt.xscale('log')

# Plot the result of every autoprocess
for wName in sample_names:
    ax.errorbar(mtd[wName][0])

plt.legend(sample_legends)
ax.set_ylabel('d$\sigma$/d$\Omega$ ($cm^{-1}$)')

#fig.show()