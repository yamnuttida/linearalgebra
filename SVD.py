import numpy as np
from numpy.linalg import svd
np.set_printoptions(precision = 2, suppress = True)
'''
#matrix n*n
A = np.array([[3,4],[6,8]])
U,s,V = svd(A)
print('U =\n' ,U)
print('V^T = \n' ,V)
print('Singular Values = ',s)
S = np.diag(s)
print('Matrix of singular values = \n',S)
print('USV^T = \n',U@S@V,'= \n',A)

'''
#matrix n*m
A = np.array([[1,2,0],[1,1,-1]])
print(A.shape)
U,s,V = svd(A)
print('U =\n' ,U)
print('V^T = \n' ,V)
print('Singular Values = ',s)
n,m = A.shape
S = np.zeros([n,m])
for i in range(0,len(s)):
    S[i,i] = s[i]
print('Matrix of singular values = \n',S)
print('USV^T = \n',U@S@V,'= \n',A)
'''
#############
print('##1')
A = np.array([[4,4],[-3,3]])
U,s,V = svd(A)
print('U =\n' ,U)
print('V^T = \n' ,V)
print('Singular Values = ',s)
n,m = A.shape
S = np.zeros([n,m])
for i in range(0,n):
    S[i,i] = s[i]
print('Matrix of singular values = \n',S)
print('USV^T = \n',U@S@V,'= \n',A)

#############
print('##2')
A = np.array([[2,2],[-1,1]])
U,s,V = svd(A)
print('U =\n' ,U)
print('V^T = \n' ,V)
print('Singular Values = ',s)
n,m = A.shape
S = np.zeros([n,m])
for i in range(0,m):
    S[i,i] = s[i]
print('Matrix of singular values = \n',S)
print('USV^T = \n',U@S@V,'= \n',A)
'''
#############
print('##3')
A = np.array([[1,-1],[0,1],[1,0]])
print(A.shape)
U,s,V = svd(A)
print('U =\n' ,U)
print('V^T = \n' ,V)
print('Singular Values = ',s)
n,m = A.shape
S = np.zeros([n,m])
for i in range(0,len(s)):
    S[i,i] = s[i]
print('Matrix of singular values = \n',S)
print('USV^T = \n',U@S@V,'= \n',A)
