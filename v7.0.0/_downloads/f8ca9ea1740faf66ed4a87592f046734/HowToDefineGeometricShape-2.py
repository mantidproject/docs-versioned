# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

cuboid = ' \
<cuboid id="shape"> \
  <left-front-bottom-point x="1" y="-0.4" z="-0.3"  /> \
  <left-front-top-point  x="1" y="-0.4" z="0.3"  /> \
  <left-back-bottom-point  x="-1" y="-0.4" z="-0.3"  /> \
  <right-front-bottom-point  x="1" y="0.4" z="-0.3"  /> \
</cuboid> \
<algebra val="shape" /> \
'

ws = CreateSampleWorkspace()
SetSample(ws, Geometry={'Shape': 'CSG', 'Value': cuboid})
sample = ws.sample()
shape = sample.getShape()
mesh = shape.getMesh()

mesh_polygon = Poly3DCollection(mesh, edgecolor = 'black' , linewidths=0.2)
mesh_polygon.set_facecolor((1,0,0,0.1))

fig, axes = plt.subplots(subplot_kw={'projection':'mantid3d'}, figsize = (8,6))
axes.add_collection3d(mesh_polygon)

axes.set_title('Cuboid defined by \n Points')
axes.set_xlabel('X / m')
axes.set_ylabel('Y / m')
axes.set_zlabel('Z / m')

axes.set_mesh_axes_equal(mesh)
axes.view_init(elev=29, azim=-22)

colors = ('darkorange','darkgreen','#33638DFF', '#440154FF')
points = [[1,-0.4,-0.3], [1,-0.4,0.3], [-1,-0.4,-0.3], [1,0.4,-0.3]]
point_names = ('left-front-\nbottom-point', 'left-front-\ntop-point', 'left-back-\nbottom-point', 'right-front-\nbottom-point')
for i in range(4):
    axes.scatter(points[i][0],points[i][1],points[i][2], color=colors[i])
    text_points = points[i]
    if i % 2 == 0:
        text_points[1] -= 0.7
        text_points[2] -= 0.2
    if i == 1:
        text_points[1] -= 0.7
        text_points[2] -= 0.2
    if i == 3:
        text_points[1] -= 0.1
        text_points[2] -= 0.4
    axes.text(text_points[0],text_points[1],text_points[2],point_names[i], color=colors[i], fontsize=14)

axes.scatter(0,0,0, color='b')
axes.text(0,0.1,-0.15, "ORIGIN", color='b', fontsize=12)

fig.show()