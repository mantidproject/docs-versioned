import matplotlib.pyplot as plt
import numpy as np
from abins.instruments import broadening

bins = np.linspace(0, 100, 1001, dtype=np.float64)
frequencies = (bins[:-1] + bins [1:]) / 2

# Generate synthetic data with two peaks
intensities = np.zeros_like(frequencies)
peak1_loc = 300
peak2_loc = 600
intensities[peak1_loc] = 1.5
intensities[peak2_loc] = 1

sigma = np.linspace(1, 10, 1000)
peak1_sigma = sigma[peak1_loc]
peak2_sigma = sigma[peak2_loc]

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, sharex=True, figsize=(8,6))

# Original spectrum
ax1.plot(frequencies, intensities, 'k-', label='Unbroadened spectrum')

# Narrow limit
freq_points, spectrum = broadening.broaden_spectrum(
    frequencies, bins, intensities,
    (peak1_sigma * np.ones_like(frequencies)),
    scheme='gaussian')
ax2.plot(freq_points, spectrum, label='Convolve with min(sigma)')

# Broad limit
freq_points, spectrum = broadening.broaden_spectrum(
    frequencies, bins, intensities,
    (peak2_sigma * np.ones_like(frequencies)),
    scheme='gaussian')
ax2.plot(freq_points, spectrum, label='Convolve with max(sigma)')

# Reference method: sum individually
freq_points, spectrum = broadening.broaden_spectrum(
    frequencies, bins, intensities, sigma, scheme='gaussian')
ax3.plot(freq_points, spectrum, 'k-', label='Sum individual peaks')

# Interpolated
freq_points, spectrum = broadening.broaden_spectrum(
    frequencies, bins, intensities, sigma, scheme='interpolate')
ax2.plot(freq_points, spectrum, c='C2', linestyle='--', label='Interpolated', zorder=0.5)
ax3.plot(freq_points, spectrum, c='C2', linestyle='--', label='Interpolated', zorder=0.5)

ax1.legend()
ax2.legend()
ax3.legend()

for ax in ax1, ax2, ax3:
    ax.tick_params(labelbottom=False, labelleft=False)

margin=0.05
fig.subplots_adjust(left=margin, right=(1-margin), bottom=margin, top=(1-margin))

fig.savefig('abins_interp_broadening_schematic.png')