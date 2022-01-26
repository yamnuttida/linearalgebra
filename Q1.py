from numpy import array
A = array([[8,2,1],[7,0,3]])
B = array([[2.9,0,5],[3,5.8,6]])
C = array([[-4,2,1],[8,5,7],[3,-2,4]])
D = array([[2,3,7],[-1,9,2],[4,-5,4]])
E = array([[9,0.4],[6,2],[0.3,5]])
F = array([[6],[7],[-2]])

# X1 = A+B
# print('A + B = \n',X1)
# print(X1[1][2])

# X2 = B-A
# print('B - A = \n',X2)
# print(X2[1][2])

# X3 = C+D
# print('C + D = \n',X3)
# print(X3[1][2])

# from numpy import dot
# X4 = dot(C,D)
# print('C * D = \n',X4)
# print(X4[1][2])

# X5 = dot(C,E)
# print('C * E = \n',X5)
# # print(X5[1][2])

# X6 = dot(D,E)
# print('D * E = \n',X6)
# # print(X6[1][2])

# X7 = dot(E,A)
# print('E * A = \n',X7)
# print(X7[1][2])

# X8 = 3*A + 5*B
# print('3A + 5B = \n',X8)
# print(X8[1][2])

from numpy.linalg import inv
A1 = array([[9,5],[3,-2]])
print(A1)
print('inv(A1) = \n',inv(A1))

A2 = array([[6,1,2],[5,3,-8],[1,6,5]])
print(A2)
print('inv(A2) = \n',inv(A2))

A3 = array([[8,5,2],[-5,1,3],[2,3,5]])
print(A3)
print('inv(A3) = \n',inv(A3))

















