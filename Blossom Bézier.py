from math import *

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

def get_point (control_points, parameter):
        bezier_point = [0,0]
        n = len(control_points)
        for i in range(n):
        #Parametric equation of a nth grade bezier line
                bezier_point[0] += binomial_coefficient(n,i)*((1-parameter)**(n-i))*(parameter**i)*(control_points[i][0])
                bezier_point[1] += binomial_coefficient(n,i)*((1-parameter)**(n-i))*(parameter**i)*(control_points[i][1])
        return bezier_point

def binomial_coefficient(m,n):
    return factorial(m)/(factorial(m-n)*factorial(n))

test = [[0,0],[10,10],[24,69],[74,0],[58,58],[0,100]]
