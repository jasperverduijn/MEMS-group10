import numpy as np
from Overlap import dC_dAngle
import matplotlib.pyplot as plt


# this we will get from overlap
def capacitance(thickness, oferlap_length, non_overlap_length):
    return 2


def angle(overlap, non_overlap, thickness):
    return thickness / (overlap + non_overlap)


overlap_start = 50 * 10 ** -6
overlap_stop = 100 * 10 ** -6
thickness = 25 * 10 ** -6
non_overlap_start = 5 * 10 ** -6
non_overlap_stop = 20 * 10 ** -6
overlap_range = np.arange(overlap_start, overlap_stop, 5 * 10 ** -6)
non_overlap_range = np.arange(non_overlap_start, non_overlap_stop, 5 * 10 ** -6)
voltage = 40
j = 25 * 10 ** -6  # final non-overlapping length
t = True

for i in overlap_range:
    T = ((voltage ** 2) * dC_dAngle(i + j, thickness, j, 0.75, 1000, 3.5 * 10 ** -6))
    angles = np.linspace(0, 0.75, 999)
    # plt.axhline(y=-4.857500543980081e-09, color='r', linestyle='-')
    plt.plot(angles, T, label=f'overlapping length: {i} m')
    plt.pause(0.1)
plt.xlabel("angle (rad)")
plt.ylabel("Moment (Nm)")
plt.legend()
plt.show()
