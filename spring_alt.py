# These calculations were not used in the final design, but
# for an earlier iteration. Calculations are kept here as
# reference

# outside springs
youngs_E = 160 * 10 ** 9  # Pa
poisson = 0.22
lenght_l = 2.5 * 10 ** -3  # m
thickness_t = 25 * 10 ** -6  # m
width_w = 3.5 * 10 ** -6  # m
shear_G = youngs_E / (2 * (1 + poisson))  # Pa
torque_T = 1 * 10 ** -8  # Nm
yield_s = 165 * 10 ** 6  # Pa
length_h = 250 * 10 ** (-6)  # m

inertia_I = (thickness_t * width_w ** 3) / 12
springstif_k = (48 * youngs_E * inertia_I) / (length_h ** 3)
spring_triple = 1 / ((1 / springstif_k) + (1 / springstif_k) + (1 / springstif_k))  # m/N

# inside leaf springs
length_h = 25 * 10 ** (-6)  # m
width_w = 10*10**-6

inertia_I = (width_w * thickness_t ** 3) / 12
springstif_k = (48 * youngs_E * inertia_I) / (length_h ** 3)
print(spring_triple)
