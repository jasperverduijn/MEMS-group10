import numpy as np
from Overlap import dC_dAngle
import matplotlib.pyplot as plt

overlap_start = 40 * 10 ** -6
overlap_stop = 80 * 10 ** -6
thickness = 25 * 10 ** -6
non_overlap_start = 5 * 10 ** -6
non_overlap_stop = 20 * 10 ** -6
overlap_range = np.arange(overlap_start, overlap_stop, 5 * 10 ** -6)
non_overlap_range = np.arange(non_overlap_start, non_overlap_stop, 5 * 10 ** -6)
voltage = 80
j = 68.75 * 10 ** -6  # final non-overlapping length

for i in overlap_range:
    T = abs(160*((voltage ** 2) * dC_dAngle(i + j, thickness, j, 0.75, 1000, 3.5 * 10 ** -6)))
    angles = np.linspace(0, 0.75, 999)
    # plt.axhline(y=4*10**-9, color='r', linestyle='-')
    plt.axvline(x=0.19, color='r', linestyle='-')
    #plt.axvline(x=-0.19, color='r', linestyle='-')
    plt.plot(angles, T, label=f'OL: {round(i*10**6,2)} \u03BCm')
    plt.pause(0.1)
plt.xlabel("angle (rad)")
plt.ylabel("Moment (Nm)")
plt.legend()
plt.show()
