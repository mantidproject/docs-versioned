import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def gaussian(x, sigma=2, center=0):
    g = np.exp(-0.5 * ((x - center) / sigma)**2) / (sigma * np.sqrt(2 * np.pi))
    return g

margin = 0.05

def plot_linear_interp():
    """Plot linearly-interpolated Gaussians with wide sigma range"""

    g1_center = 0
    g2_center = 40
    sigma_max = 4
    sigma_min = 1

    x = np.linspace(-10, 50, 401)

    fig, ax = plt.subplots()
    for sigma, color in zip(np.linspace(sigma_min, sigma_max, 5),
                            ['C0', 'C1', 'C2', 'C3', 'C4']):
        center = (g1_center
                  + ((sigma - sigma_min)
                     * (g2_center - g1_center) / (sigma_max - sigma_min)))
        ax.plot(x, gaussian(x, sigma=sigma, center=center), c=color)

        low_ref = gaussian(x, sigma=sigma_min, center=center)
        high_ref = gaussian(x, sigma=sigma_max, center=center)
        mix = (sigma - sigma_min) / (sigma_max - sigma_min)
        ax.plot(x, (1 - mix) * low_ref + mix * high_ref,
                c=color, linestyle='--')

    ax.set_xlim([-10, 50])
    ax.set_ylim([0, None])
    ax.tick_params(labelbottom=False, labelleft=False)

    custom_lines = [Line2D([0], [0], color='k', linestyle='-', lw=2),
                    Line2D([0], [0], color='k', linestyle='--', lw=2)]

    ax.legend(custom_lines, ['Exact', 'Linear interpolation'])
    fig.subplots_adjust(left=margin, bottom=margin,
                        right=(1 - margin), top=(1 - margin))

plot_linear_interp()