# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

ws = CreateSampleWorkspace()

merge_xml = ' \
<cylinder id="stick"> \
<centre-of-bottom-base x="-0.5" y="0.0" z="0.0" /> \
<axis x="1.0" y="0.0" z="0.0" />  \
<radius val="0.05" /> \
<height val="1.0" /> \
</cylinder> \
\
<sphere id="some-sphere"> \
<centre x="0.7"  y="0.0" z="0.0" /> \
<radius val="0.2" /> \
</sphere> \
\
<rotate-all x="90" y="-45" z="0" /> \
<algebra val="some-sphere (: stick)" /> \
'

SetSample(ws, Geometry={'Shape': 'CSG', 'Value': merge_xml})

sample = ws.sample()
shape = sample.getShape()
mesh = shape.getMesh()

mesh_polygon = Poly3DCollection(mesh, edgecolors = 'blue', linewidths=0.1)
mesh_polygon.set_facecolor((1,0,0,0.5))

fig, axes = plt.subplots(subplot_kw={'projection':'mantid3d'})
axes.add_collection3d(mesh_polygon)

axes.set_mesh_axes_equal(mesh)
axes.view_init(elev=10, azim=-150)

axes.set_title('Sample Shape: Microphone')
axes.set_xlabel('X / m')
axes.set_ylabel('Y / m')
axes.set_zlabel('Z / m')

plt.show()