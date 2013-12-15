def blossom (control_points, parameters): #parameters = {t0, k, t1, j}
	#Gets control_points of an auxiliary curve
	auxiliary_control_points = [[0,0]]*parameters[]
	#
	
def restrict (control_points, a=0, b):
	new_control_points = []
	for i in range(len(control_points)):
		parameters = [a]*(n-i) + [b]*i
		new_control_points += blossom (control_points, parameters)
	return new_control_points
		
def get_point (control_points, parameter):
	bezier_point = [0,0]
	for i in range(len(control_points)):
        #Parametric ecuation of a nth grade bezier line
        bezier_point[0] += binomial_coefficient(n,i)*((1-parameter)**(n-i))*(parameter**i)*(control_points[i][0])
        bezier_point[1] += binomial_coefficient(n,i)*((1-parameter)**(n-i))*(parameter**i)*(control_points[i][1])
	return bezier_point