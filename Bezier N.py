from math import *
from datetime import *
import pdb

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

def binomial_coefficient(m,n):
    return factorial(m)/(factorial(m-n)*factorial(n))

def get_control_points(n):
    control_points = [[0,0]]*n
    for i in range(n):
        print "Control point %d" %i
        control_points[i][0] = float(raw_input("x = "))
        control_points[i][1] = float(raw_input("y = "))
    return control_points

def arithmetic_progression(a1, stop, step):
    progression = []
    while a1 <= stop:
        progression.append(a1)
        a1 += step
    return progression
	
test = [[0,0],[10,10],[24,69],[74,0],[58,58],[0,100]]*100+[[24,32]]

#--------------------------------------------------------------------------------
def recursiveBezierN(n, resolution, control_points = None):

    if not control_points:#Manual entry of points
        control_points = get_control_points(n+1) #Returns array: [[x,y]]*(n+1)
		
    tstart = datetime.now()
    bezier_curve = []
    step = 1/float(resolution)
	
    for t in arithmetic_progression(0,1,step):
        anchors = control_points[:]
        for interpolations in range(n): #For a n grade curve we'll need n recursive interpolations
            for i in range(len(anchors)-1): #Interpolates P0 with P1 and stores the result in P0, then repeats with P1 and P2, etc
                anchors[i] = interpolate(anchors[i],anchors[i+1],t)
            anchors.pop()#Eliminates the last point, no longer needed
        bezier_curve.append(anchors[0])
		
    tend = datetime.now()
    print tend - tstart
    return bezier_curve

def interpolate(p1,p2,parameter):
    pt = [0,0]
    pt[0] = (1-parameter)*p1[0] + parameter*p2[0]
    pt[1] = (1-parameter)*p1[1] + parameter*p2[1]
    return pt
