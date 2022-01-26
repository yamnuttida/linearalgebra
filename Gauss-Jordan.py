import numpy as np
'''#1
A = np.array([[-1.0,3,2],[1,2,-3],[2,1,-2]])
b = np.array([[8],[5],[-6]]) #b =Ax
'''
'''#2
A = np.array([[4,8,4,0],[1,5,4,-3],[1,4,7,2],[1,3,0,-2]])
b = np.array([[8],[-4],[10],[-4.0]]) 
'''
#3
A = np.array([[2,4,-4,0],[1,5,-5,-3],[2,3,1,3],[1,4,-2,2]])
b = np.array([[12],[18],[8],[8.0]])

np.set_printoptions(precision=2,suppress=True)
n = len(A)
B = A
A = np.hstack((A,b))
print('A =\n',A)

''' #Gauss-Jordan elimination
#สามเหลี่ยมบน
for i in range(0,n-1):
    A[i,:] = A[i,:]/A[i,i]
    for j in range(i+1,n):
        lamb = -A[j,i]/A[i,i]
        A[j,:] = A[j,:] + lamb*A[i,:]
#สามเหลี่ยมล่าง
for i in range(n-1,-1,-1):
    A[i,:] = A[i,:]/A[i,i]
    for j in range(i-1,-1,-1):
        lamb = -A[j,i]/A[i,i]
        A[j,:] = A[j,:] + lamb*A[i,:]    
print('A =\n',A)
print('Ax=b คือ \n',A[:,n])

print('Ax =\n',B@A[:,n]) '''

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
