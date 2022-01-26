import numpy as np
A = np.array([[3,8,4,0,8],[1,9,4,-5,-4],[3,4,-7,2,10],[4,3,0,-6,-4]])
print('A = \n',A)

#from numpy.linalg import det,inv
#print('det(A) = \n',det(A))
#print('inv(A) = \n',inv(A))

b = np.array([[8],[5],[-6]])

n = len(A)
I = np.identity(n)
A = np.hstack((A,I))

for i in range(0,n-1):
    d=A[i,i]
    A[i,:]=A[i,:]/A[i,i]
    print('R%d = R%d / %2.2f'%(i+1,i+1,d))
    print('A = \n',A)
    print()
    for j in range(i+1,n):
        lamb = -A[j,i]/A[i,i]
        A[j,:] = A[j,:] + lamb*A[i,:]
        print('R%d = R%d + %2.2f R%d'%(j+1,j+1,lamb,i+1))
        print('A = \n',A)
        print()

for i in range(n-1,-1,-1):
    d=A[i,i]
    A[i,:]=A[i,:]/A[i,i]
    print('R%d = R%d / %2.2f'%(i+1,i+1,d))
    print('A = \n',A)
    print()
    for j in range(i-1,-1,-1):
        lamb = -A[j,i]/A[i,i]
        A[j,:] = A[j,:] + lamb*A[i,:]
        print('R%d = R%d + %2.2f R%d'%(j+1,j+1,lamb,i+1))
        print('A = \n',A)
        print()

B = A[:,n:]
print('inv A = \n',B)
