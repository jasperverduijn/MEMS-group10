# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 15:45:23 2023

@author: Jasper Verduijn
"""

from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np

freq = 474

def theta_dd(theta,t):
    M = -(1e-10*140)*np.sin(2*np.pi*freq*t)
    K = 4.28e-8 #Nm/rad
    I = 4.8101e-15 
    C = 2*0.95*np.sqrt(K*I)

    return [theta[1], (M-C*theta[1]-K*theta[0])/I]


Cycles= 10
t_start = 0
t_end = Cycles*(1/freq)
step = (1/freq)/50
theta_0 = 0.0035

time = np.arange(t_start, t_end, step)

theta, theta_d = odeint(theta_dd, [theta_0, 0], time).T   
angle = theta*180/np.pi

#plt.figure(1)
#plt.plot(time, theta, 'orange', linewidth = 2)
#plt.xlabel('time (s)')
#plt.ylabel('theta (rad)')
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
#plt.grid(True)

plt.figure(2)
plt.plot(time, angle, 'orange', linewidth = 2)
plt.xlabel('time (s)')
plt.ylabel('angle (deg)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.grid(True)