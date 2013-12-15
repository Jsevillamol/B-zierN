class bezierN:
	def __init__(self, n, control_points = None):
		self.n = n
		if not control_points: #Manual input in case no automatic control_points are provided
			self.control_points = get_control_points(n+1) #Returns array: [[x,y]]*(n+1)
		else:
			self.control_points = control_points
			
	def get_point(self, parameter):
		bezier_point = [0,0]
		for i in range(len(self.control_points)):
			#Parametric ecuation of a nth grade bezier line
			bezier_point[0] += binomial_coefficient(self.n,i)*((1-parameter)**(self.n-i))*(parameter**i)*(self.control_points[i][0])
			bezier_point[1] += binomial_coefficient(self.n,i)*((1-parameter)**(self.n-i))*(parameter**i)*(self.control_points[i][1])
		return bezier_point
		
	def get_points(self, resolution):
		bezier_curve = []
		step = 1/float(resolution)
	
		for parameter in arithmetic_progression(0, 1, step): #Unfortunately, the built-in function range does not accept a float step argument
			bezier_curve.append(self.get_point(parameter))
		
		return bezier_curve
		
	def transform(self, scalar = 1, vector = [0,0] ):
		for i in range(len(self.control_points)):
			#Scalates
			self.control_points[i][0] *= scalar
			self.control_points[i][1] *= scalar
			#Translates
			self.control_points[i][0] += vector[0]
			self.control_points[i][1] += vector[1]
	
	def degree_elevation(control_points):
        n = len(control_points)
        #El primer y último punto de control coinciden con el primer y ultimo punto de control de la nueva curva
        last_point = control_points[-1][:]
        control_points.append(last_point)
        #El resto de puntos son calculados
        for i in xrange(1, n):
            control_points[i][0]=(float(i)/float(n+1))*control_points[i-1][0]+(1-(float(i)/float(n+1)))*control_points[i][0]
            control_points[i][1]=(float(i)/float(n+1))*control_points[i-1][1]+(1-(float(i)/float(n+1)))*control_points[i][1]
        return control_points
#------------------------------------------------------------------------------	
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