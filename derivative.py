#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Calculates the control polygon of the nth derivative of a Bézier curve
def derivate(control_points,n):
    grade = len(control_points)-1
    for iteration in range(n):
        grade -= 1
        for j in range(len(control_points)-1):
            control_points[j][0] = grade*(control_points[j+1][0]-control_points[j][0])
			control_points[j][1] = grade*(control_points[j+1][1]-control_points[j][1])
        control_points.pop()
    return control_points
        
# Calculates the control polygon of the nth derivative of a Bézier curve without recursion. 
# Equivalent to last function
def derivate(control_points, n):

# Calculates the derivative when parameter equals t
def tangent (control_points, t):
    

# Calcula el polígono de control de la derivada de una curva de Bézier
def differentiate (control_points):
    grade = len(control_points)-1
    derivative_control_points = []
    for i in range(len(control_points)-1):
        derivative_control_points += [grade*(control_points[i+1][0] - control_points[i][0]),
                                      grade*(control_points[i+1][1] - control_points[i][1])]
    return derivative_control_points