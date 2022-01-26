import numpy as np
from numpy.linalg import eig , norm
np.set_printoptions(precision = 2, suppress = True)
import numpy as np
from numpy.linalg import svd
np.set_printoptions(precision = 2, suppress = True)

#1
A = np.array([[4,6],[-1,-3]])
values,vectors = eig(A)
print('ค่าลักษณะเฉพาะ (Eigenvalues) คือ \n',values)
print('เวกเตอร์ลักษณะเฉพาะ (Eigenvectors) คือ \n',vectors)


#2
B = np.array([[5,-2,3],[1,4,9],[7,9,2]])
values,vectors = eig(B)
print('ค่าลักษณะเฉพาะ (Eigenvalues) คือ \n',values)
print('เวกเตอร์ลักษณะเฉพาะ (Eigenvectors) คือ \n',vectors)


#3
C = np.array([[2,1,3],[1,-2,1],[0,5,8]])
print(C.shape)
U,s,V = svd(C)
print('U =\n' ,U)
print('V^T = \n' ,V)
print('Singular Values = ',s)
n,m = C.shape
S = np.zeros([n,m])
for i in range(0,len(s)):
    S[i,i] = s[i]
print('Matrix of singular values = \n',S)
print('USV^T = \n',U@S@V,'= \n',C)
