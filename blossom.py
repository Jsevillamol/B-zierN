#!/usr/bin/env python
# -*- coding: utf-8 -*-

from auxiliary_functions import *

def blossom (control_points, parameters): #parameters = {t0, k, t1}
        #Gets control_points of an auxiliary curve
        auxiliary_control_points = [[0,0]]*(len(control_points)-parameters["k"])
        for i in range (len(auxiliary_control_points)):
                auxiliary_control_points[i] = get_point(control_points[i:i+parameters["k"]], parameters["t0"])
        #Calculates the blossomed point from the auxiliary Bezier curve with the parameter t1
        return get_point (auxiliary_control_points, parameters["t1"])

def restrict (control_points, a=0, b=1):
        parameters = {"t0":a, "t1":b}
        for i in range(len(control_points)):
                parameters ["k"] = i #k is the number of times t0 is used as a parameter in the polarization
                control_points[i] = blossom (control_points, parameters)
        return control_points
