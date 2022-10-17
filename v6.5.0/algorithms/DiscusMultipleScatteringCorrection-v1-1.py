# import mantid algorithms, numpy and matplotlib
from mantid import mtd
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

# S(Q) consisting of single spike at q=1
# Spike height gives same normalisation as isotropic (integral of Q.S(Q) the same)
X=[0.99,1.0,1.01]
Y=[0.,100,0.]
Sofq=CreateWorkspace(DataX=X,DataY=Y,UnitX="MomentumTransfer")

# Isotropic S(Q)
X=[1.0]
Y=[1.0]
Sofq_isotropic=CreateWorkspace(DataX=X,DataY=Y,UnitX="MomentumTransfer")

two_thetas=[]
for i in range(180):
    two_thetas.append(i)

# workspace with single bin centred at k=1 Angstrom-1
ws = CreateSampleWorkspace(WorkspaceType="Histogram",
                           XUnit="Momentum",
                           Xmin=0.5,
                           Xmax=1.5,
                           BinWidth=1.0,
                           NumBanks=len(two_thetas)//4,
                           BankPixelWidth=2,
                           InstrumentName="testinst")

ids = list(range(1,len(two_thetas)+1))
EditInstrumentGeometry(ws,
    PrimaryFlightPath=14.0,
    SpectrumIDs=ids,
    L2=[2.0] * len(two_thetas),
    Polar=two_thetas,
    Azimuthal=[90.0] * len(two_thetas),
    DetectorIDs=ids,
    InstrumentName="testinst")

sphere_xml = " \
<sphere id='some-sphere'> \
    <centre x='0.0'  y='0.0' z='0.0' /> \
    <radius val='0.01' /> \
</sphere> \
<algebra val='some-sphere' /> \
"
SetSample(InputWorkspace=ws,
          Geometry={'Shape': 'CSG', 'Value': sphere_xml},
          Material={'NumberDensity': 0.02, 'AttenuationXSection': 0.0,
                    'CoherentXSection': 0.0, 'IncoherentXSection': 0.0, 'ScatteringXSection': 80.0})

results_group = DiscusMultipleScatteringCorrection(InputWorkspace=ws, StructureFactorWorkspace=Sofq,
                                                   OutputWorkspace="MuscatResults", NeutronPathsSingle=1000,
                                                   NeutronPathsMultiple=10000, ImportanceSampling=True)
# Can't index into workspace group by name (yet) so just get the members from the ADS instead
Scatter_1_DeltaFunction = CloneWorkspace('MuscatResults_Scatter_1')
Scatter_2_DeltaFunction = CloneWorkspace('MuscatResults_Scatter_2')
DeleteWorkspace('MuscatResults')

DiscusMultipleScatteringCorrection(InputWorkspace=ws, StructureFactorWorkspace=Sofq_isotropic,
                                   OutputWorkspace="MuscatResultsIsotropic", NeutronPathsSingle=1000,
                                   NeutronPathsMultiple=10000, ImportanceSampling=True)
Scatter_2_Isotropic = CloneWorkspace('MuscatResultsIsotropic_Scatter_2')


# q=2ksin(theta), so q spike corresonds to single scatter spike at ~60 degrees, double scatter spikes at 0 and 120 degrees
msplot = plotBin('Scatter_2_DeltaFunction',0)
msplot = plotBin('Scatter_1_DeltaFunction',0, window=msplot)
msplot = plotBin('Scatter_2_Isotropic',0, window=msplot)
axes = plt.gca()
axes.set_xlabel('Spectrum (~scattering angle in degrees)')
axes.set_ylim(-0.05,0.6)
plt.title("Single and Double Scatter Intensities")
mtd.clear()