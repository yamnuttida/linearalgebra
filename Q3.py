import numpy as np
A = np.array([[1,1/3,0,1/3,1],[1,0,2,1,-2],[1,1/3,-1,0,4],[1,-3,4,-4,2]])
n = len(A)
print('A =\n',A)
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
print('Ax =\n',A)