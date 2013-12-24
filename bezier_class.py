#!/usr/bin/env python
# -*- coding: utf-8 -*-

from auxiliary_functions import *

class bezierN:
	def __init__(self, n, control_points = None):
		self.n = n
		# Manual input in case no automatic control_points are provided
		if not control_points:
			self.control_points = get_control_points(n+1) #Returns array: [[x,y]]*(n+1)
		else:
			self.control_points = control_points
			
	def get_point(self, parameter):
		bezier_point = [0,0]
		for i in range(len(self.control_points)):
			#Parametric ecuation of a nth grade bezier line
			bezier_point[0] += binomial_coefficient(self.n,i)*((1-parameter)**(self.n-i))*(parameter**i)*(self.control_points[i][0])
			bezier_point[1] += binomial_coefficient(self.n,i)*((1-parameter)**(self.n-i))*(parameter**i)*(self.control_points[i][1])
		return bezier_point
		
	def get_points(self, resolution):
		bezier_curve = []
		step = 1/float(resolution)
	
		for parameter in arithmetic_progression(0, 1, step): #Unfortunately, the built-in function range does not accept a float step argument
			bezier_curve.append(self.get_point(parameter))
		
		return bezier_curve
		
	def transform(self, scalar = 1, vector = [0,0] ):
		for i in range(len(self.control_points)):
			#Scalates
			self.control_points[i][0] *= scalar
			self.control_points[i][1] *= scalar
			#Translates
			self.control_points[i][0] += vector[0]
			self.control_points[i][1] += vector[1]
	
	def degree_elevation(control_points):
        n = len(control_points)
        #El primer y último punto de control coinciden con el primer y ultimo punto de control de la nueva curva
        last_point = control_points[-1][:]
        control_points.append(last_point)
        #El resto de puntos son calculados
        for i in xrange(1, n):
            control_points[i][0]=(float(i)/float(n+1))*control_points[i-1][0]+(1-(float(i)/float(n+1)))*control_points[i][0]
            control_points[i][1]=(float(i)/float(n+1))*control_points[i-1][1]+(1-(float(i)/float(n+1)))*control_points[i][1]
        return control_points
#------------------------------------------------------------------------------	
