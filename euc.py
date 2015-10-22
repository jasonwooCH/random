import numpy

points = [(2, 10), (2, 5), (8, 4), (5, 8), (7, 5), (6, 4), (1, 2), (4, 9)]

coord = [];

for i in range (0, 8):
    coord.append(numpy.array(points[i]))

#for j in range (0, 8):
 #   for k in range (j, 8):
  #      print (str(numpy.linalg.norm(coord[j]-coord[k])) + " ")
   # print ("\n")

k1 = numpy.array((11/3, 9)) #(3,9.5) (2,10)
k2 = numpy.array((7,13/3))  # (6.5,5.25) (6,6)
k3 = numpy.array((1.5,3)) # (1.5,3) (1.5,3)

for i in range (0, 8):
    print (numpy.linalg.norm(k1-coord[i]))
    print (numpy.linalg.norm(k2-coord[i]))
    print (numpy.linalg.norm(k3-coord[i]))
    print ("\n")
