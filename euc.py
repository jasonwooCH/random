import numpy

points = [(2, 10), (2, 5), (8, 4), (5, 8), (7, 5), (6, 4), (1, 2), (4, 9)]

coord = [];

for i in range (0, 7):
    coord.append(numpy.array(points[i]))
    
for j in range (0, 7):
    for k in range (j, 7):
        print (str(numpy.linalg.norm(coord[j]-coord[k])) + " ")
    print ("\n")
    
