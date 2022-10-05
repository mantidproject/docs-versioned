from mantid.api import mtd
from mantid.simpleapi import ExtractMonitors, LoadILLReflectometry
import matplotlib.pyplot as plt
import numpy

ws = LoadILLReflectometry('ILL/D17/317370.nxs')
ExtractMonitors(ws, DetectorWorkspace='ws')
ws=mtd['ws']
det0 = ws.getDetector(0)
det1 = ws.getDetector(ws.getNumberHistograms() - 1)
theta0 = numpy.rad2deg(ws.detectorSignedTwoTheta(det0))
theta1 = numpy.rad2deg(ws.detectorSignedTwoTheta(det1))
fig, ax = plt.subplots(subplot_kw={'projection': 'mantid'})
ax.pcolor(ws, cmap='Oranges')
ax.set_xlim(xmin=3, xmax=27)
ax.set_ylim(ymin=0, ymax=ws.getNumberHistograms())
ax.set_ylabel('Pixel (workspace index)')
ax.axhspan(238, 250, color='red', alpha=0.15)
ax.text(4.5, 241, 'LowAngleBkgWidth')
ax.text(5, 223, 'LowAngleBkgOffset')
ax.axhspan(185, 215, color='blue', alpha=0.15)
ax.text(5.5, 206, 'ForegroundWidth [0]')
ax.axhline(203, linestyle=':', color='k')  # Line position
ax.text(22, 200, 'LinePosition')
ax.text(5.5, 190, 'ForegroundWidth [1]')
ax.text(5, 162, 'HighAngleBkgOffset')
ax.axhspan(75, 145, color='red', alpha=0.15)
ax.text(4.5, 108, 'HighAngleBkgWidth')
ax2 = ax.twinx()
ax2.set_ylim(ymin=theta0, ymax=theta1)
ax2.set_ylabel('Angle (degrees)')