# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

cuboid = " \
<cuboid id='some-cuboid'> \
  <width val='2.0' />  \
  <height val='4.0'  /> \
  <depth  val='0.2' />  \
  <centre x='10.0' y='10.0' z='10.0'  />  \
</cuboid>  \
<algebra val='some-cuboid' /> \
"

ws = CreateSampleWorkspace()
SetSample(ws, Geometry={'Shape': 'CSG', 'Value': cuboid})
sample = ws.sample()
shape = sample.getShape()
mesh = shape.getMesh()
facecolors = ['purple','mediumorchid','royalblue','b','red','firebrick','green', 'darkgreen','grey','black', 'gold', 'orange']
mesh_polygon = Poly3DCollection(mesh, facecolors=facecolors)

fig, axes = plt.subplots(subplot_kw={'projection':'mantid3d'})
axes.add_collection3d(mesh_polygon)

axes.set_title('Sample Shape: Cuboid')
axes.set_xlabel('X / m')
axes.set_ylabel('Y / m')
axes.set_zlabel('Z / m')

axes.set_mesh_axes_equal(mesh)
axes.view_init(elev=20, azim=-27)

def arrow(ax, vector, origin = None, factor = None, color = 'r',linestyle = '-'):
    if origin == None:
        origin = (ax.get_xlim3d()[1],ax.get_ylim3d()[1],ax.get_zlim3d()[1])
    ax.quiver(
         origin[0], origin[1], origin[2],
         vector[0], vector[1], vector[2],
         color = color,
         linestyle = linestyle
    )

origins = [[11,10,9.5],[9,8,11.1],[10,12,10.5]]
colors = ['purple','black','b']
vectors = [[0,2,0],[0,0,-1],[1,0,0]]
for i in range(3):
    vector, origin = vectors[i], origins[i]
    arrow(axes, vector=vector, origin=origin, color =colors[i])
    if i == 1:
        origin[2] = 8.9
    arrow(axes, vector=np.multiply(vector,-1), origin=origin, color =colors[i])

axes.text(8,7.2,9.65, "DEPTH", color='black', fontsize=12)
axes.text(10.5,11.5,11, "WIDTH", color='b', fontsize=12)
axes.text(11,9.5,9, "HEIGHT", color='purple', fontsize=12)

fig.show()