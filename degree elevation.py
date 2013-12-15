def degree_elevation(control_points):
        n = len(control_points)
        #El primer y último punto de control coinciden con el primer y ultimo punto de control de la nueva curva
        control_points.append(control_points[-1])
        print control_points
        #El resto de puntos son calculados
        for i in xrange(1, n):
                control_points[i][0]=(float(i)/float(n+1))*control_points[i-1][0]+(1-(float(i)/float(n+1)))*control_points[i][0]
                control_points[i][1]=(float(i)/float(n+1))*control_points[i-1][1]+(1-(float(i)/float(n+1)))*control_points[i][1]
                print control_points
        return control_points

test = [[0,0],[10,10],[24,69],[74,0],[58,58],[0,100]]
