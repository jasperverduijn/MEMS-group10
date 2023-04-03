youngs_E = 160 * 10 ** 9  # Pa
poisson = 0.22
L1 = 300 * 10 ** -6
h1 = 25 * 10 ** -6
b1 = 30 * 10 ** -6
I1 = (b1 * h1 ** 3) / 12
L2 = 500 * 10 ** -6
h2 = 3.5 * 10 ** -6
b2 = 25 * 10 ** -6
I2 = (b2 * h2 ** 3) / 12
n = 1
k_3 = 1 / ((L1 / (8 * I1 * youngs_E)) + (L2 / (n * I2 * youngs_E)))  # Nm/rad
moment_needed = k_3 * 0.17
print(k_3)
