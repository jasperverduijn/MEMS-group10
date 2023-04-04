youngs_E = 160 * 10 ** 9  # Pa
poisson = 0.22
shear_G = youngs_E / (2 * (1 + poisson))  # Pa
# Grote meneer
L1 = 500 * 10 ** -6 #halve lengte beam
h1 = 25 * 10 ** -6
b1 = 3.5 * 10 ** -6
I1 = (b1 * h1 ** 3) / 12
k1 = (3 * I1 * youngs_E)/L1

# Kleine meneer
L2 = 500 * 10 ** -6
h2 = 25 * 10 ** -6
b2 = 3.5 * 10 ** -6
J2 = (1 / 16) * h2 * (b2 ** 3) * ((16 / 3) - 3.36 * (b2 / h2) * (1 - ((b2 ** 4) / 12 * h2 ** 4)))
I2 = (b2 * h2 ** 3) / 12
k_veertje = shear_G * J2 / L2
n = 1
#k_3 = 4 / ((1/k1)+(1/(2*k_veertje)))  # Nm/rad
k_3 = 4*k1
moment_needed = k_3 * 0.17
print(k_3)
