import numpy as np

rho = 2330  # kg m^-3
radius = 0.5 * 10 ** -3  # m
thickness = 25 * 10 ** -6  # m
volume = thickness * np.pi * radius ** 2
weight = (2 / 3) * 9.81 * rho * volume  # N
offset = 500 * 10 ** -6

moment = weight * offset  # Nm
print(moment)

# moment produced by 160 fingers: 1.55*10**-8, at ten degrees
# moment needed for a 10 degrees initial offset: 8.11776038251366e-09
# offset needed : 500 * 10 ** -6 m
