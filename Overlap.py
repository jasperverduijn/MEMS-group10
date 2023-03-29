# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:02:45 2023

@author: jaspe
"""

from shapely.geometry import Polygon
import numpy as np
import matplotlib.pyplot as plt

def area_disp(width,height,theta_max,n):
    #Define static rectangle 
    static = Polygon([(0,-height/2),(width,-height/2),(width,height/2),(0,height/2)])
    
    #Define arrays 
    arr_theta = np.linspace(0,np.pi/2,n)
    area = np.zeros(n)
    
    #Loop over all angles
    for i in range(0,len(arr_theta)):
        theta = arr_theta[i]
             
        p1 = ((height/2)*np.sin(theta),-height/2*np.cos(theta))
        p2 = (width*np.cos(theta)+height/2*np.sin(theta),width*np.sin(theta)-height/2*np.cos(theta))
        p3 = (width*np.cos(theta)-height/2*np.sin(theta),width*np.sin(theta)+height/2*np.cos(theta))
        p4 = ((-height/2)*np.sin(theta),height/2*np.cos(theta))
        
        #Calculate new rectangle
        dynamic = Polygon([p1,p2,p3,p4])
        
        #Find intersection
        poly_intersection = static.intersection(dynamic)
        #Save area from intersection
        area[i] = poly_intersection.area
    return [arr_theta,area] 





Curve = area_disp(10,10,np.pi/2,100)
plt.plot(Curve[0],Curve[1])