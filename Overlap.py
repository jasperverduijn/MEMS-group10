# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:02:45 2023

@author: jaspe
"""

from shapely.geometry import Polygon
import numpy as np
import matplotlib.pyplot as plt
from numpy import diff

def area_disp(width,height,offset,theta_max,n):
    #Define static rectangle 
    static = Polygon([(0,-height/2),(width,-height/2),(width,height/2),(0,height/2)])
    
    #Define arrays 
    arr_theta = np.linspace(0,np.pi/2,n)
    area = np.zeros(n)
    
    #Loop over all angles
    for i in range(0,len(arr_theta)):
        theta = arr_theta[i]
             
        p1 = ((height/2)*np.sin(theta)-offset,-height/2*np.cos(theta))
        p2 = (width*np.cos(theta)+height/2*np.sin(theta)-offset,width*np.sin(theta)-height/2*np.cos(theta))
        p3 = (width*np.cos(theta)-height/2*np.sin(theta)-offset,width*np.sin(theta)+height/2*np.cos(theta))
        p4 = ((-height/2)*np.sin(theta)-offset,height/2*np.cos(theta))
        
        #Calculate new rectangle
        dynamic = Polygon([p1,p2,p3,p4])
        
        #Find intersection
        poly_intersection = static.intersection(dynamic)
        #Save area from intersection
        area[i] = poly_intersection.area
    return [arr_theta,area] 


def derivative(x,y):
    return diff(y)/diff(x)

def dC_dAngle(width,height,offset,theta_max,n,z):
    Curve = area_disp(20,4,5,np.pi/2,100)
    Angles = Curve[0]    
    Derivative = derivative(Angles,Curve[1])
        
    eta = 8.854e-12
    
    return eta*Derivative / z

Curve = area_disp(20,4,5,np.pi/2,100)
Angles = Curve[0]    
Derivative = derivative(Angles,Curve[1])
plt.plot(Angles,Curve[1])
plt.plot(Angles[:len(Derivative)],Derivative)
