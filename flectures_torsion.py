# -*- coding: utf-8 -*-
import numpy as np

youngs_E = 160 * 10 ** 9  # Pa
poisson = 0.22
L2= 1 * 10 ** -3  # m
h2 = 25 * 10 ** -6  # m
b2 = 3.5 * 10 ** -6  # m
shear_G = youngs_E / (2 * (1 + poisson))  # Pa
torque_T = 4*10**-9 # Nm
yield_s = 165 * 10 ** 6  # Pa
c = np.sqrt((0.5*h2)**2+(0.5*b2)**2)
# force_x = (electric_permittivity*num_beams*out_plane_gap*actuation_voltage**2)/gap_spacing
# force_y = ..
# force_z =
# displace_x = force_x/springk_x
# displace_y =
# displace_z =



# const_J = thickness_t * width_w ** 3 * (
#         (1 / 3) - 0.21 * (width_w / thickness_t) * (1 - (width_w ** 4 / (12 * thickness_t ** 4))))
const_J = (1 / 16) * h2 * (b2 ** 3) * ((16 / 3) - 3.36 * (b2 / h2) * (1 - ((b2 ** 4) / 12 * h2 ** 4)))
theta = (torque_T * L2) / (shear_G * const_J)
k_veertje = 2*shear_G * const_J / L2
stress = (torque_T*3/(h2*b2**2))*(1+(0.6095*b2/h2)+(0.8865*(b2/h2)**2)-(1.8023*(b2/h2)**3)+(0.91*(b2/h2)**4))
print(theta)
if stress > yield_s:
    print("break")
