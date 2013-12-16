#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimp import *
from auxiliary_functions import *

register(
        "Bezier N",#Name
        "Draws a nth grade bezier curve",#Description
        "Draws a path of cubic bezier curve identical to a nth grade bezier curve constructed from a given set of anchor points", #Long description
        "Jaime Sevilla",#Author
        "Jaime Sevilla",#Copyright
        "2013",#Date
        "<Tools>/Paths/BezierN",#Menu path
        "*", #Type of images it works with
        [],#Arguments
        [], #Results
        bezier_N)
		

Calculate nth bezier line
Calculate anchor points of cubic lines