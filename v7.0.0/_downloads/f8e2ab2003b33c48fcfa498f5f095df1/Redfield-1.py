from mantid.simpleapi import FunctionWrapper
import matplotlib.pyplot as plt
import numpy as np
x = np.logspace(-1, 3.4, num = 200)
h = np.linspace(0.05, 0.2, 5)
y = []
Redfield = FunctionWrapper("Redfield")
for hloc in h:
        y.append(Redfield(x, hloc))

fig, ax = plt.subplots()
ax.plot(x, np.array(y).T, label=['{:.2f}'.format(item) for item in h])
ax.legend(title='$H_{loc}$ (G)')
ax.set_xscale("log")
ax.set_xlabel('$H_{LF}$ (Gauss)')
ax.set_ylabel('$\Lambda(\mu s^{-1})$')