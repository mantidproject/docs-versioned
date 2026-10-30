import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from mantid.simpleapi import CreateMDHistoWorkspace
from mantid import plots

# Generate nice (fake) dispersion data
# Gamma to K
q = np.arange(0,0.333,0.01)
e = np.arange(0,60)
x,y = np.meshgrid(q,e)
omega_hh = 20. * np.sin(np.pi*x*1.5)
I_hh = np.exp(-x*5.)
signal = I_hh * np.exp(-(y-omega_hh)**2)
signal[y>25+100*x**2]=np.nan
ws1=CreateMDHistoWorkspace(Dimensionality=2,
                           Extents='0,0.3333,0,60',
                           SignalInput=signal,
                           ErrorInput=np.sqrt(signal),
                           NumberOfBins='{0},{1}'.format(len(q),len(e)),
                           Names='Dim1,Dim2',
                           Units='MomentumTransfer,EnergyTransfer')
# K to M
q = np.arange (0.333,0.5, 0.01)
x,y = np.meshgrid(q,e)
omega_hm2h=20. * np.cos(np.pi*(x-0.333))
signal = np.exp(-(y-omega_hm2h)**2)
signal[y>35]=np.nan
ws2=CreateMDHistoWorkspace(Dimensionality=2,
                           Extents='0.3333,0.5,0,60',
                           SignalInput=signal,
                           ErrorInput=np.sqrt(signal),
                           NumberOfBins='{0},{1}'.format(len(q),len(e)),
                           Names='Dim1,Dim2',
                           Units='MomentumTransfer,EnergyTransfer')


d=6.7
a=2.454
#Gamma is (0,0,0)
#A is (0,0,1/2)
#K is (1/3,1/3,0)
#M is (1/2,0,0)
gamma_a=np.pi/d
gamma_m=2.*np.pi/np.sqrt(3.)/a
m_k=2.*np.pi/3/a
gamma_k=4.*np.pi/3/a

fig=plt.figure(figsize=(12,5))
gs = GridSpec(1, 4,
              width_ratios=[gamma_k,m_k,gamma_m,gamma_a],
              wspace=0)

ax1 = plt.subplot(gs[0],projection='mantid')
ax2 = plt.subplot(gs[1],sharey=ax1,projection='mantid')
ax3 = plt.subplot(gs[2],sharey=ax1)
ax4 = plt.subplot(gs[3],sharey=ax1)

ax1.pcolormesh(ws1)
ax2.pcolormesh(ws2)
ax3.plot([0,0.5],[0,17.])
ax4.plot([0,0.5],[0,10])


#Adjust plotting parameters

ax1.set_ylabel('E (meV)')
ax1.set_xlabel('')
ax1.set_xlim(0,1./3)
ax1.set_ylim(0.,40.)
ax1.set_title(r'$[\epsilon,\epsilon,0], 0 \leq \epsilon \leq 1/3$')
ax1.set_xticks([0,1./3])
ax1.set_xticklabels(['$\Gamma$','$K$'])
#ax1.spines['right'].set_visible(False)
ax1.tick_params(direction='in')

ax2.get_yaxis().set_visible(False)
ax2.set_xlim(1./3,1./2)
ax2.set_xlabel('')
ax2.set_title(r'$[1/3+\epsilon,1/3-2\epsilon,0], 0 \leq \epsilon \leq 1/6$')
ax2.set_xticks([1./2])
ax2.set_xticklabels(['$M$'])
#ax2.spines['left'].set_visible(False)
ax2.tick_params(direction='in')

#invert axis
ax3.set_xlim(1./2,0)
ax3.get_yaxis().set_visible(False)
ax3.set_title(r'$[\epsilon,0,0], 1/2 \geq \epsilon \geq 0$')
ax3.set_xticks([0])
ax3.set_xticklabels(['$\Gamma$'])
ax3.tick_params(direction='in')

ax4.set_xlim(0,1./2)
ax4.get_yaxis().set_visible(False)
ax4.set_title(r'$[0,0,\epsilon], 0 \leq \epsilon \leq 1/2$')
ax4.set_xticks([1./2])
ax4.set_xticklabels(['$A$'])
ax4.tick_params(direction='in')
#fig.show()