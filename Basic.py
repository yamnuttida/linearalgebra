#for i in range(1,5):
#    print(2*i)

#a=2;b=3;c=4
#print('A = %d B = %d C = %d\n' %(a,b,c))    

# create matrix
from numpy import array
A = array([[1,0,2],[3,4,5]])
#print(A)

# size matrix
print(A.shape)

# find by position 
print(A[1][2])

# create identity matrix
from numpy import identity
I = identity(4)
print(I)

# transpose matrix
print(A.T)

B = array([[4,2,1,5],[3,1,4,2],[8,2,4,1],[6,5,3,8]])
print(B)
print(B.T)

C = array([[4],[5],[7],[2]])
print(C)
print(C.T) 

# Element Operation +,- "+,- dimention of matrix must same"
A = array([[1,0,2],[3,4,5]])
print('Matrix A = \n',A)
D = array([[-8,5,4],[-7,5,3]])
print('Matrix D = \n',D)
print('Matrix A+D = \n',A+D)
print('Matrix A-D = \n',A-D)

# Element Operation * "* dimention of row as dimention of column"
A = array([[1,-1,0],[2,3,1]])
print('Matrix A = \n',A)
B = array([[-2,1],[0,1],[1,-1]])
print('Matrix B = \n',B)
print('Matrix A*B = \n', A@B)  # sol 1
print('Matrix A*B = \n', A.dot(B)) # sol 2
from numpy import dot
print('Matrix A*B = \n', dot(A,B)) # sol 3 by import dot

A = array([[1,2,3],[-2,0,1],[1,1,2]])
print('Matrix A = \n',A)
B = array([[-3],[1],[2]])
print('Matrix B = \n',B)
print('Matrix A*B = \n', A@B)  # sol 1
print('Matrix A*B = \n', A.dot(B)) # sol 2
print('Matrix A*B = \n', dot(A,B)) # sol 3 by import dot

# constant * matrix
from numpy import array
A = array([[1,0,2],[3,4,5]])
print(2*A)
# * element oparation
C = 5*A
D = 0.25*B
print(A*B.T)
print(A/B.T)

# invest matrix
from numpy.linalg import inv
A= array([[2,5],[0,4]])
B = inv(A)
print('inv A = \n',B)
print('A*B = \n',A@B)

A = array([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]])
print(A)
# create diagonal matrix
from numpy import diag
d = diag(A)
print(d)
D = diag(d)
print(D)

from numpy import triu, tril
print('Upper triangular matrix :\n',triu(A))
print('Lower triangular matrix :\n',tril(A))




























