# -*- coding: utf-8 -*-
youngs_E = 150*10**9 # Pa
lenght_l = 25*10**-6 # m
thickness_t = 3*10**-6 # m
width_w = 25*10**-6 # m
shear_G = 60*10**9 # Pa
torque_T = 5*10**-13 # Nm
#force_x = (electric_permittivity*num_beams*out_plane_gap*actuation_voltage**2)/gap_spacing 
#force_y = ..
#force_z =
#displace_x = force_x/springk_x
#displace_y =  
#displace_z =  
 
spring_const = (24*youngs_E*thickness_t*width_w**3)/(12*lenght_l**3) # N/m

const_J = thickness_t*width_w**3*((1/3)-0.21*(width_w/thickness_t)*(1-(width_w**4/(12*thickness_t**4))))
theta = (torque_T*lenght_l)/(shear_G*const_J)
