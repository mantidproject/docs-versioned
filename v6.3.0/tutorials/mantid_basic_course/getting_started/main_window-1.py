import numpy as np
import matplotlib.pyplot as plt

neutrons_detected_at = np.array([5,11,15,22,23,25,35,36,37,
                                     38,43,45,49,50,55,58,62,64,
                                     74,76,78,80,85,90])
counts_per_bin=(1,2,3,4,6,5,3)
bin_edges = np.array([0,10,20,30,40,60,80,100])

number_of_bins = len(bin_edges)-1
bin_centres = np.zeros(number_of_bins)

for i in range(number_of_bins):
    bin_centres[i] = (bin_edges[i+1] + bin_edges[i])/2

plt.hist(neutrons_detected_at, bins=bin_edges, align='mid', color='b', edgecolor='black',density = False, label='Bins')
plt.plot(bin_centres,counts_per_bin,color='red', label = 'Line')


# Add axis labels
plt.xlabel("X data      eg. Time ($\mu s$)")
plt.ylabel("Y data      eg. Counts ($\mu s$)$^{-1}$")
plt.title("Bins and Line Plots")
plt.xticks(bin_edges)
plt.legend()
plt.show()