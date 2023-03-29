import numpy as np
from Overlap import dC_dAngle
import matplotlib.pyplot as plt

# this we will get from overlap
def capacitance(thickness, oferlap_length, non_overlap_length):
    return 2


def angle(overlap, non_overlap, thickness):
    return thickness / (overlap + non_overlap)


overlap_start = 5 * 10 ** -9
overlap_stop = 30 * 10 ** -9
thickness = 25 * 10 ** -9
non_overlap_start = 5 * 10 ** -9
non_overlap_stop = 20 * 10 ** -9
overlap_range = np.arange(overlap_start, overlap_stop, 5 * 10 ** -9)
non_overlap_range = np.arange(non_overlap_start, non_overlap_stop, 5 * 10 ** -9)
voltage = 40
plt.ion()
plt.figure(1)
t = True
while t == True:
    for i in overlap_range:
        for j in non_overlap_range:
            T = ((voltage ** 2) * dC_dAngle(i+j, thickness, j, 0.75, 1000, 5*10**-9)) / 2
            angles = np.linspace(0, 0.75, 999)
            plt.plot(angles, T)
            plt.pause(0.1)


