#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from auxiliary_functions import *

# Translates
def translate(control_points, vector=[0,0]):
    for i in range(len(control_points)):
        control_points[i][0] += vector[0]
        control_points[i][1] += vector[1]
    return control_points

# Escalates
def escale(control_points, scalar=1):
    for i in range(len(control_points)):
        control_points[i][0] *= scalar
        control_points[i][1] *= scalar
    return control_points

# Rotates with centre in [0,0]
def rotate (control_points, angle=0):
    new_control_points = [[0,0]]*len(control_points)
    for i in range(len(control_points)):
        new_control_points[i][0] = (control_points[i][0]*math.cos(angle) +
                                    control_points[i][1]*math.sin(angle))
        new_control_points[i][1] = (control_points[i][1]*math.cos(angle) -
                                    control_points[i][0]*math.sin(angle))
    return new_control_points
