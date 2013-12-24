#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from math import *

# Obtiene manualmente los puntos de control de una curva de Bezier a travÃ©s de la consola
def get_control_points(n):
    control_points = [[0,0]]*n
    for i in range(n):
        print "Control point %d" %i
        control_points[i][0] = float(raw_input("x = "))
        control_points[i][1] = float(raw_input("y = "))
    return control_points

#-----------------------------------------------------------
"""
def binomial_coefficient_factorial(m,n):
    return factorial(m)/(factorial(m-n)*factorial(n))
"""

# Construye la fila m del triangulo de Pascal y devuelve el elemento n de ella
# Equivalente a la funciÃ³n comentada
def binomial_coefficient(m,n):
	# First row of Pascal's triangle
	row = [1,1]
	
	while m > 1:
		# Construye una nueva lÃ­nea del triángulo de Pascal
		new_row = [1]+[row[i]+row[i-1]for i in range(1,len(row))]+[1]
		row = new_row
		m-=1
	return row[n]

def arithmetic_progression(a1, stop, step):
    progression = []
    while a1 <= stop:
        progression.append(a1)
        a1 += step
    return progression

# Calculates a point from a Bezier curve using a parameter. 
# It is equivalent to a recursive interpolation, albeit significantly faster.
def get_point (control_points, parameter):
    bezier_point = [0,0]
    n = len(control_points)

    # Parametric equation of a nth grade bezier line
    for i in range(n):
        bezier_point[0] += bernstein_polynomial(n,i,parameter)*(control_points[i][0])
        bezier_point[1] += bernstein_polynomial(n,i,parameter)*(control_points[i][1])
	
    return bezier_point
#--------------------------------------------------------------
	
# Interpola linealmente dos puntos aplicando un parÃ¡metro
def interpolate(p1,p2,parameter):
    pt = [0,0]
    pt[0] = (1-parameter)*p1[0] + parameter*p2[0]
    pt[1] = (1-parameter)*p1[1] + parameter*p2[1]
    return pt

# Interpola recursivamente una lista de puntos hasta que se reduce a un punto
def recursive_interpolation(points, parameter):
    newpoints = points[:]
    for interpolation in range (len(points)-1):
        for i in range(len(newpoints)-1):
		    # Cada nuevo punto se obtiene interpolando un par de puntos
            newpoints[i] = interpolate (newpoints[i],newpoints[i+1],parameter)
        # Each iteration needs a polynomial with one less control point
        newpoints.pop()
    return newpoints[0]

#------------------------------------------------------------
# Calculates the ith Bernstein polynomial of grade n at t (0 >= t >= 1)
def bernstein_polynomial(n,i,t):
	return binomial_coefficient(n,i)*(t**i)*(1-t)**(n-i)

#------------------------------------------------------------
# For testing purposes
test = [[0,0],[10,10],[24,69],[74,0],[58,58],[0,100]]*100+[[24,32]]
testparam = {"t0": 0.4, "t1": 0.5, "k": 3}
