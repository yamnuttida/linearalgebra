import numpy as np
#2. จงหาฐานของ RS(A), CS(A)เเละ NS(A) 
A = np.array([[-1,8,4,-3],[2,1,4,-3],[-2,4,1,2],[3,-1,-5,1]])
n = len(A)

#2.1
A = np.array([[3,5,1,6],[1,3,4,1],[0,6,3,1]])
#2.2
A = np.array([[2,-4,1],[8,1,3],[1,1,-4]])
#2.3
A = np.array([[2,-3,1,7,5],[-8,1,2,-3,7],[0,1,-4,1,3],[2,4,1,7,-5]])

n = len(A)
#ใช้ Gauss-Jordan elimination ทำขั้นบันได 
#หา RS(A)
#สามเหลี่ยมบน
for i in range(0,n-1):
    if A[i,i] !=0 :
        A[i,:] = A[i,:]/A[i,i]
        for j in range(i+1,n):
            lamb = -A[j,i]/A[i,i]
            A[j,:] = A[j,:] + lamb*A[i,:]
if A[n-1,n-1] !=0:
    A[n-1,:] = A[n-1,:]/A[n-1,n-1]
print('B =\n',A)

#หาผลเฉลย Ax=0
b = np.zeros([n,1])
A = np.hstack((A,b))
#สามเหลี่ยมล่าง
for i in range(n-1,-1,-1):
    for j in range(i-1,-1,-1):
        if A[i,i] !=0 :
            lamb = -A[j,i]/A[i,i]
            A[j,:] = A[j,:] + lamb*A[i,:]    
print('A =\n',A)