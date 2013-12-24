#!/usr/bin/env python
# -*- coding: utf-8 -*-

from auxiliary_functions import *
from datetime import *

def bezierN(n, resolution, control_points = None):
#Returns a list in which each element is the X and Y components
#of a point that conforms a Bezier curve of nth grade
    
    if not control_points: #Manual input in case no automatic control_points are provided
        control_points = get_control_points(n+1) #Returns array: [[x,y]]*(n+1)
		
    tstart = datetime.now()
    bezier_curve = []
    step = 1/float(resolution)
	
    for parameter in arithmetic_progression(0, 1, step): #Unfortunately, the built-in function range does not accept a float step argument
        bezier_point = [0,0]
        for i in range(len(control_points)):
        #Parametric ecuation of a nth grade bezier line
            bezier_point[0] += binomial_coefficient(n,i)*((1-parameter)**(n-i))*(parameter**i)*(control_points[i][0])
            bezier_point[1] += binomial_coefficient(n,i)*((1-parameter)**(n-i))*(parameter**i)*(control_points[i][1])
        bezier_curve.append(bezier_point)
		
    tend = datetime.now()
    print tend - tstart
	
    return bezier_curve

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
def recursiveBezierN(n, resolution, control_points = None):
	# Manual entry of points
    if not control_points:
        control_points = get_control_points(n+1) # Returns array: [[x,y]]*(n+1)
		
    tstart = datetime.now()
    bezier_curve = []
    step = 1/float(resolution)
	
    for t in arithmetic_progression(0,1,step):
        anchors = control_points[:]
        for interpolations in range(n): #For a n grade curve we'll need n recursive interpolations
			# Interpolates P0 with P1 and stores the result in P0, then repeats with P1 and P2, etc
            for i in range(len(anchors)-1): 
                anchors[i] = interpolate(anchors[i],anchors[i+1],t)
			# Eliminates the last point, no longer needed
            anchors.pop()
        bezier_curve.append(anchors[0])
		
    tend = datetime.now()
    print tend - tstart
    return bezier_curve