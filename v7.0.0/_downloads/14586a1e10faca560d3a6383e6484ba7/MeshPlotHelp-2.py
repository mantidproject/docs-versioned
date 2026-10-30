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
SetGoniometer(ws, Axis0="45,0,1,0,-1")
SetSample(ws, Geometry={'Shape': 'CSG', 'Value': cuboid})
sample = ws.sample()

SetUB(ws, a=1, b=1, c=2, alpha=90, beta=90, gamma=60)
if not sample.hasOrientedLattice():
   raise Exception("There is no valid lattice")

UB = np.array(ws.sample().getOrientedLattice().getUB())
hkl = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
QSample = np.matmul(UB,hkl)
Goniometer = ws.getRun().getGoniometer().getR()
reciprocal_lattice = np.matmul(Goniometer,QSample)#QLab
real_lattice = (2.0*np.pi)*np.linalg.inv(np.transpose(reciprocal_lattice))

shape = sample.getShape()
mesh = shape.getMesh()

facecolors = ['purple','mediumorchid','royalblue','b','red','firebrick','green', 'darkgreen','grey','black', 'gold', 'orange']
mesh_polygon = Poly3DCollection(mesh, facecolors = facecolors, linewidths=0.1)

fig, axes = plt.subplots(subplot_kw={'projection': 'mantid3d', 'proj_type': 'ortho'})
axes.add_collection3d(mesh_polygon)

axes.set_title('Cuboid Sample \n with Real and Reciprocal lattice vectors')
axes.set_xlabel('X / m')
axes.set_ylabel('Y / m')
axes.set_zlabel('Z / m')

axes.set_mesh_axes_equal(mesh)
axes.set_box_aspect((1, 1, 1))

def arrow(ax, vector, origin = None, factor = None, color = 'black',linestyle = '-'):
   if origin == None:
      origin = (ax.get_xlim3d()[1],ax.get_ylim3d()[1],ax.get_zlim3d()[1])
   if factor == None:
      lims = ax.get_xlim3d()
      factor = (lims[1]-lims[0]) / 3.0
   vector_norm = vector / np.linalg.norm(vector)
   ax.quiver(
         origin[0], origin[1], origin[2],
         vector_norm[0]*factor, vector_norm[1]*factor, vector_norm[2]*factor,
         color = color,
         linestyle = linestyle
   )

colors = ['r','g','b']
for i in range(3): # plot real_lattice with '-' solid linestyle
   arrow(axes, real_lattice[:,i], color = colors[i])
for i in range(3): # plot reciprocal_lattice with '--' dashed linestyle
   arrow(axes, reciprocal_lattice[:,i], color = colors[i], linestyle = '--')

axes.view_init(vertical_axis='y', elev=27, azim=50)
fig.show()