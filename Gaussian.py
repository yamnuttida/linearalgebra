import numpy as np
A = np.array([[2,4,-4,0],[1,5,-5,-3],[2,3,1,3],[1,4,-2,2]])
b = np.array([[12],[18],[8],[8.0]])

np.set_printoptions(precision=2,suppress=True)
n = len(A)
B = A
A = np.hstack((A,b))
print('A =\n',A)

#Gaussian elimination
#สามเหลี่ยมบน
for i in range(0,n-1):
    for j in range(i+1,n):
        lamb = -A[j,i]/A[i,i]
        A[j,:] = A[j,:] + lamb*A[i,:]
b = A[:,n]
A = A[:,0:n]
#แทนค่าย้อนกลับ
n = n-1
x = np.zeros([n+1,1]) #สร้างเมทริกซ์ xgป็น0
x[n] = b[n] / A[n,n]
for k in range(n-1,-1,-1):
    x[k] = (b[k]-sum(A[k,k+1:]@x[k+1:])) / A[k,k]
print('ผลเฉลยที่ต้องการ คือ \n',x)
