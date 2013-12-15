from math import *

#Obtiene manualmente los puntos de control de una curva de Bezier a través de la consola
def get_control_points(n):
    control_points = [[0,0]]*n
    for i in range(n):
        print "Control point %d" %i
        control_points[i][0] = float(raw_input("x = "))
        control_points[i][1] = float(raw_input("y = "))
    return control_points

#-----------------------------------------------------------

def binomial_coefficient(m,n):
    return factorial(m)/(factorial(m-n)*factorial(n))

def arithmetic_progression(a1, stop, step):
    progression = []
    while a1 <= stop:
        progression.append(a1)
        a1 += step
    return progression

#Calculates a point from a Bezier curve using a parameter. It is equivalent to a recursive interpolation, albeit significantly faster.
def get_point (control_points, parameter):
        bezier_point = [0,0]
        n = len(control_points)
        for i in range(n):
        #Parametric equation of a nth grade bezier line
                bezier_point[0] += binomial_coefficient(n,i)*((1-parameter)**(n-i))*(parameter**i)*(control_points[i][0])
                bezier_point[1] += binomial_coefficient(n,i)*((1-parameter)**(n-i))*(parameter**i)*(control_points[i][1])
        return bezier_point
#--------------------------------------------------------------
	
#Interpola linealmente dos puntos aplicando un parámetro
def interpolate(p1,p2,parameter):
        pt = [0,0]
        pt[0] = (1-parameter)*p1[0] + parameter*p2[0]
        pt[1] = (1-parameter)*p1[1] + parameter*p2[1]
        return pt

#Interpola recursivamente una lista de puntos hasta que se reduce a un punto
def recursive_interpolation(points, parameter):
        newpoints = points[:]
        for interpolation in range (len(points)-1):
                for i in range(len(newpoints)-1):
                        newpoints[i] = interpolate (newpoints[i],newpoints[i+1],parameter)
                        #Cada nuevo punto se obtiene interpolando un par de puntos
                newpoints.pop() #Eliminates the last point
        return newpoints

#------------------------------------------------------------
#For testing purposes
test = [[0,0],[10,10],[24,69],[74,0],[58,58],[0,100]]*100+[[24,32]]
