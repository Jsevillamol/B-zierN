#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Applies affine transformations
def transform(control_points, scalar = 1, vector = [0,0] ):
    for i in range(len(control_points)):
        # Scalates
        control_points[i][0] *= scalar
        control_points[i][1] *= scalar
        # Translates
        control_points[i][0] += vector[0]
        control_points[i][1] += vector[1]
	return control_points