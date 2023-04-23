# -*- coding: utf-8 -*-
import numpy as np

E_modulus = 160 * 10 ** 9  # Pa
poisson = 0.22
length = 1 * 10 ** -3  # m
height = 25 * 10 ** -6  # m
width = 3.5 * 10 ** -6  # m
G_modulus = E_modulus / (2 * (1 + poisson))  # Pa
torque = 1.53 * 10 ** -8  # Nm
yield_s = 165 * 10 ** 6  # Pa
constant = np.sqrt((0.5 * height) ** 2 + (0.5 * width) ** 2)
# force_x = (electric_permittivity*num_beams*out_plane_gap*actuation_voltage**2)/gap_spacing
# force_y = ..
# force_z =
# displace_x = force_x/springk_x
# displace_y =
# displace_z =


# const_J = thickness_t * width_w ** 3 * (
#         (1 / 3) - 0.21 * (width_w / thickness_t) * (1 - (width_w ** 4 / (12 * thickness_t ** 4))))
J = (1 / 16) * height * (width ** 3) * ((16 / 3) - 3.36 * (width / height) * (1 - ((width ** 4) / 12 * height ** 4)))
theta = (torque * length) / (2 * G_modulus * J)
k_spring = 2 * G_modulus * J / length
stress = (torque * 3 / (height * width ** 2)) * (
        1 + (0.6095 * width / height) + (0.8865 * (width / height) ** 2) - (1.8023 * (width / height) ** 3) + (0.91 * (width / height) ** 4))
print(1.5 * 10 ** -10 / k_spring)
if stress > yield_s:
    print("break")
