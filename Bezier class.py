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
		
	def split(self, parameter = 0.5):
		#Returns the control points of a curve that behaves as self in the intervale t = [0, parameter]
		control_points = []
		for i in range(len((self.control_points)):
			control_points += recursive_interpolation (self.control_points [:i+1], parameter)
		return control_points
		
	def transform(self, scalar = 1, vector = [0,0] ):
		for i in range(len(self.control_points)):
			#Scalates
			self.control_points[i][0] *= scalar
			self.control_points[i][1] *= scalar
			#Translates
			self.control_points[i][0] += vector[0]
			self.control_points[i][1] += vector[1]
			
#------------------------------------------------------------------------------	
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

def recursive_interpolation(points, parameter):
	for interpolation in range (len(points[:])-1):
		for i in range(len(points)-1):
			points[i] = interpolate (points[i],points[i+1],parameter)
		points.pop()
	return points

def interpolate(p1,p2,parameter):
    pt = [0,0]
    pt[0] = (1-parameter)*p1[0] + parameter*p2[0]
    pt[1] = (1-parameter)*p1[1] + parameter*p2[1]
    return pt