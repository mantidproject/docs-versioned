import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def gaussian(x, sigma=2, center=0):
    g = np.exp(-0.5 * ((x - center) / sigma)**2) / (sigma * np.sqrt(2 * np.pi))
    return g

margin = 0.05

def plot_optimised_interp(sigma_max=4):
    g1_center = 0
    g2_center = 40
    sigma_min = 1

    x = np.linspace(-10, 10, 101)
    npts = 7

    fig, [ax1, ax2, ax3] = plt.subplots(nrows=3,
                                        sharex=True,
                                        gridspec_kw={
                                            'height_ratios': [3, 1, 1]})
    mix1_list, mix2_list = [], []

    def gaussian_mix(x, w1, w2):
        """Return a linear combination of two Gaussians with weights"""
        return (w1 * gaussian(x, sigma=sigma_min)
                + w2 * gaussian(x, sigma=sigma_max))


    for sigma, color in zip(np.linspace(sigma_min, sigma_max, npts),
                            ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6']):
        ydata = gaussian(x, sigma=sigma)
        (mix1, mix2), _ = curve_fit(gaussian_mix, x, ydata, p0=[0.5, 0.5])

        x_offset = (g1_center
                    + ((sigma - sigma_min)
                       * (g2_center - g1_center) / (sigma_max - sigma_min)))
        actual = gaussian(x, sigma=sigma)
        est = gaussian_mix(x, mix1, mix2)
        rms = np.sqrt(np.mean((actual - est)**2))
        ax1.plot(x + x_offset, actual, color=color)
        ax1.plot(x + x_offset, est, color=color, linestyle='--')
        ax2.plot([x_offset], [rms], 'o', c='C0')

        mix1_list.append(mix1)
        mix2_list.append(mix2)


    custom_lines = [Line2D([0], [0], color='k', linestyle='-', lw=2),
                    Line2D([0], [0], color='k', linestyle='--', lw=2)]

    ax1.legend(custom_lines, ['Exact', 'Optimised interpolation'])

    ax2.set_ylabel('RMS error')

    ax3.plot(np.linspace(g1_center, g2_center, npts), mix1_list)
    ax3.plot(np.linspace(g1_center, g2_center, npts), mix2_list)
    ax3.set_ylabel('Weights')
    ax3.set_ylim([0, 1])

plot_optimised_interp(sigma_max=np.sqrt(2))