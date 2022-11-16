# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# A fake host workspace, replace this with your real one.
ws = CreateSampleWorkspace()
LoadInstrument(Workspace=ws,RewriteSpectraMap=True,InstrumentName="Pearl")
SetSample(ws, Environment={'Name': 'Pearl'})

sample = ws.sample()
environment = sample.getEnvironment()

mesh = sample.getShape().getMesh()
container_mesh = environment.getContainer().getShape().getMesh()

mesh_polygon_a = Poly3DCollection(mesh, facecolors = 'green', edgecolors='blue',alpha = 0.5, linewidths=0.1, zorder = 0.3)
mesh_polygon_b = Poly3DCollection(container_mesh, edgecolors='red', alpha = 0.1, linewidths=0.05, zorder = 0.5)
mesh_polygon_b.set_facecolor((1,0,0,0.5))

fig, axes = plt.subplots(subplot_kw={'projection': 'mantid3d', 'proj_type': 'ortho'})
axes.add_collection3d(mesh_polygon_a)
axes.add_collection3d(mesh_polygon_b)

for i in (1,3,5):
   print(i)
   mesh_polygon_i = Poly3DCollection(environment.getComponent(i).getMesh(), edgecolors='red', alpha = 0.1, linewidths=0.05, zorder = 0.5)
   mesh_polygon_i.set_facecolor((1,0,0,0.5))
   axes.add_collection3d(mesh_polygon_i)

# Auto scale to the mesh size
axes_lims = (-0.03,0.03)
axes.auto_scale_xyz(axes_lims, axes_lims, axes_lims)

axes.set_title('Pearl Sample in Container and Components(1,3,5) with black beam arrow')
axes.set_xlabel('X / m')
axes.set_ylabel('Y / m')
axes.set_zlabel('Z / m')
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
# Add arrow along beam direction
source = ws.getInstrument().getSource().getPos()
sample = ws.getInstrument().getSample().getPos() - source
arrow(axes, sample, origin=(0,0,-0.04))
axes.view_init(vertical_axis='y', elev=30, azim=-135)
plt.show()