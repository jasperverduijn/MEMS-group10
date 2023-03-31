# -*- coding: utf-8 -*-
import numpy as np

youngs_E = 160 * 10 ** 9  # Pa
poisson = 0.22
lenght_l = 2.5 * 10 ** -3  # m
thickness_t = 25 * 10 ** -6  # m
width_w = 3.5 * 10 ** -6  # m
shear_G = youngs_E / (2 * (1 + poisson))  # Pa
torque_T = 1*10**-8  # Nm
yield_s = 165 * 10 ** 6  # Pa
c = np.sqrt((0.5*thickness_t)**2+(0.5*width_w)**2)
# force_x = (electric_permittivity*num_beams*out_plane_gap*actuation_voltage**2)/gap_spacing
# force_y = ..
# force_z =
# displace_x = force_x/springk_x
# displace_y =
# displace_z =

spring_const = (24 * youngs_E * thickness_t * width_w ** 3) / (12 * lenght_l ** 3)  # N/m

const_J = thickness_t * width_w ** 3 * (
        (1 / 3) - 0.21 * (width_w / thickness_t) * (1 - (width_w ** 4 / (12 * thickness_t ** 4))))
theta = (torque_T * lenght_l) / (shear_G * const_J)
stress = torque_T*c/const_J
print(theta)
if stress > yield_s:
    print("break")
