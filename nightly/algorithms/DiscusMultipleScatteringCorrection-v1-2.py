# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np
import math

# parameterised Lorentzian S(Q,w) from Discus pdf
# wavelength = 4 Angstroms, k=1.57
X,Y, SpecAxis =[],[],[]
qmin, qmax = 0.,4.0
nqpts = 9
wmin, wmax = -5.85, 5.85 # meV
nwpts = 79 # negative w is given explicitly so ~double number of pts in Discus
D = 0.15 # Angstom-2 meV -1 = 2.3E-05 cm2 s-1
TEMP=300
HOVERT = 11.6087/TEMP
for iq in range(nqpts):
   q = iq * (qmax-qmin)/(nqpts-1) + qmin
   SpecAxis.append(q)
   for iw in range(nwpts):
     w = iw * (wmax-wmin)/(nwpts-1) + wmin
     X.append(w)
     if (w*w + (D*q*q)**2==0.):
        # Discus S(Q,w) has zero here so do likewise
        print("Denominator zero so outputting S(q,w)=0")
        Y.append(0.)
     else:
        Sqw = D*q*q/(math.pi*(w*w + (D*q*q)**2))
        # Apply detailed balance, neutrons more likely to lose energy in each scatter
        # Mantid has w = Ei-Ef
        if (w > 0.):
           Sqw = Sqw * math.exp(HOVERT * w)
        # S(Q,w) is capped at exactly 4.0 for some reason in Discus example
        Y.append(min(Sqw,4.0))

sqw = CreateWorkspace(DataX=X,DataY=Y,UnitX="DeltaE",
                      VerticalAxisUnit="MomentumTransfer",
                      VerticalAxisValues=SpecAxis, NSpec=nqpts)

two_thetas = [20.0, 40.0, 60.0, 90.0]

ws = CreateSampleWorkspace(WorkspaceType="Histogram",
                           XUnit="DeltaE",
                           Xmin=wmin-0.5*(wmax-wmin)/(nwpts-1),
                           Xmax=wmax+0.5*(wmax-wmin)/(nwpts-1),
                           BinWidth=(wmax-wmin)/(nwpts-1),
                           NumBanks=len(two_thetas),
                           BankPixelWidth=1,
                           InstrumentName="testinst")

# set up ring of detectors in yz plane
ids = list(range(1,len(two_thetas)+1))
EditInstrumentGeometry(ws,
    PrimaryFlightPath=14.0,
    SpectrumIDs=ids,
    L2=[2.0] * len(two_thetas),
    Polar=two_thetas,
    #azimuthal angle=phi, phi=0 along x axis and increases as move towards vertical y axis
    Azimuthal=[-90.0] * len(two_thetas),
    DetectorIDs=ids,
    InstrumentName="testinst")

# flat plate sample 5cm x 5cm x 0.065cm
cuboid_xml = " \
<cuboid id='flatplate'> \
  <width val='0.05' /> \
  <height val='0.05'  /> \
  <depth  val='0.00065' /> \
  <centre x='0.0' y='0.0' z='0.0'  /> \
  <rotate x='45' y='0' z='0' /> \
</cuboid> \
"
SetSample(InputWorkspace=ws,
          Geometry={'Shape': 'CSG', 'Value': cuboid_xml},
          Material={'NumberDensity': 0.02, 'AttenuationXSection': 0.0,
                    'CoherentXSection': 0.0, 'IncoherentXSection': 0.0, 'ScatteringXSection': 80.0})

#match Ei value from DISCUS pdf Figure 1
ws.run().addProperty("deltaE-mode", "Direct", True);
ws.run().addProperty("Ei", 5.1, True);

DiscusMultipleScatteringCorrection(InputWorkspace=ws, StructureFactorWorkspace=sqw,
                                   OutputWorkspace="MuscatResults", NeutronPathsSingle=200,
                                   NeutronPathsMultiple=1000)

# reverse w axis because Discus w = Ef-Ei (opposite to Mantid)
for i in range(mtd['MuscatResults_Scatter_1'].getNumberHistograms()):
    y = np.flip(mtd['MuscatResults_Scatter_1'].dataY(i),0)
    e = np.flip(mtd['MuscatResults_Scatter_1'].dataE(i),0)
    mtd['MuscatResults_Scatter_1'].setY(i,y.tolist())
    mtd['MuscatResults_Scatter_1'].setE(i,e)
for i in range(mtd['MuscatResults_Scatter_2'].getNumberHistograms()):
    y = np.flip(mtd['MuscatResults_Scatter_2'].dataY(i),0)
    e = np.flip(mtd['MuscatResults_Scatter_2'].dataE(i),0)
    mtd['MuscatResults_Scatter_2'].setY(i,y.tolist())
    mtd['MuscatResults_Scatter_2'].setE(i,e)

plt.rcParams['figure.figsize'] = (5, 6)
fig, ax = plt.subplots(subplot_kw={'projection':'mantid'})
for i, tt in enumerate(two_thetas):
    ax.plot(mtd['MuscatResults_Scatter_1'], wkspIndex=i, label='Single: ' + str(tt) + ' degrees')
for i, tt in enumerate(two_thetas):
    ax.plot(mtd['MuscatResults_Scatter_2'], wkspIndex=i, label='Double: ' + str(tt) + ' degrees', linestyle='--')
plt.yscale('log')
ax.set_xlim(-1,1)
ax.set_ylim(1e-4,1e-1)
ax.legend(fontsize=7.0)
plt.title("Inelastic Double\\Single Scattering Weights")
fig.show()
mtd.clear()