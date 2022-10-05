# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

cuboid = " \
<cuboid id='some-cuboid'> \
<height val='2.0'  /> \
<width val='2.0' />  \
<depth  val='0.2' />  \
<centre x='10.0' y='10.0' z='10.0'  />  \
</cuboid>  \
<algebra val='some-cuboid' /> \
"

ws = CreateSampleWorkspace()
SetGoniometer(ws, Axis0="30,0,1,0,-1")
SetSample(ws, Geometry={'Shape': 'CSG', 'Value': cuboid})

sample = ws.sample()
shape = sample.getShape()
mesh = shape.getMesh()

facecolors = ['purple','mediumorchid','royalblue','b','red','firebrick','green', 'darkgreen','grey','black', 'gold', 'orange']

mesh_polygon = Poly3DCollection(mesh, facecolors = facecolors, linewidths=0.1)

fig, axes = plt.subplots(subplot_kw={'projection':'mantid3d'})
axes.add_collection3d(mesh_polygon)

axes.set_title('Sample Shape: Cuboid ws @ 30°')
axes.set_xlabel('X / m')
axes.set_ylabel('Y / m')
axes.set_zlabel('Z / m')

axes.set_mesh_axes_equal(mesh)
axes.view_init(elev=20, azim=80)

plt.show()