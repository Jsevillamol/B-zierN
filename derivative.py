#Calculates the control poligone of the nth derivate of a Bézier curve
def derivate(control_points,n):
        grade = len(control_points)
        for iteration in range(n):
                grade -= 1
                for j in range(len(control_points)-1):
                        control_points[j][0] = grade*(control_points[j+1][0]-control_points[j][0])
                control_points.pop()
        return control_points
        
#Calculates the control poligone of the nth derivate of a Bézier curve without recursion. 
#Equivalent to last function
def derivate(control_points, n):

#Calculates the derivative when parameter equals t
def tangent (control_points, t):
        
