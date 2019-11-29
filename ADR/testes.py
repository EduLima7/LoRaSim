import numpy as np

# def count(mat, val):
# 	cnt = 0
# 	for i in range(mat.shape[0]):
# 		for j in range(mat.shape[1]):
# 			if mat[i,j]> val:
# 				cnt += 1
# 	return cnt

points = np.matrix([[1, -4, 22, 9, 2], [7, 8, 9, 3, 11],[7, 8, 9, -120, 1]])
arrayone = np.ones((5,4))*12

# print points.shape[0]
# print points.shape[1]

# print "Max value" + str(np.argwhere(points==np.argmax(points))[0][1]) +": "  + str(np.max(points))

# for i in range(points.shape[0]):
# 		for j in range(points.shape[1]):
# 			print "Coordenadas[" + str(i) + "," + str(j) + "]: " + str(points[i,j])
# print points[2,3]

# for i in range(0, len(points)):
# x = count(points,5)
# print x
# print len(points)
z = np.argwhere(points==-120)
print z[0][0]