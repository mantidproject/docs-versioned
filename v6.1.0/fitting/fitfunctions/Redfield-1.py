from mantid.simpleapi import FunctionWrapper
import matplotlib.pyplot as plt
import numpy as np
x = np.logspace(-2, 4, num = 1000)
y = FunctionWrapper("Redfield")
fig, ax=plt.subplots()
ax.plot(x, y(x))
ax.set_xlabel('t($\mu$s)')
ax.set_ylabel('A(t)')