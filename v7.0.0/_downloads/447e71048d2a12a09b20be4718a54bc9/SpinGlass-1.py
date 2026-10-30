from mantid.simpleapi import FunctionWrapper
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0.0,16,0.01)
y = FunctionWrapper("SpinGlass")
fig, ax=plt.subplots()
ax.plot(x, y(x))
ax.set_xlabel('t($\mu$s)')
ax.set_ylabel('A(t)')