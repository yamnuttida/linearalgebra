import numpy as np
#1. จงหาผลเฉลยของระบบสมการ
#1.1
'''
A = np.array([[2,-5,0,-1],[3,1,6,-9],[1,3,-5,2],[3,0,8,1]])
b = np.array([[-4],[1],[1],[12.0]])

#1.2
A = np.array([[-1,5,8,-3],[-2,1,-4,-1],[-1,2,0,2],[4,1,5,1]])
b = np.array([[15],[-16],[-1],[19.0]])
'''
#1.3
A = np.array([[-2,2,1,3],[2,1,0,1],[2,4,-3,1],[1,-2,1,3]])
b = np.array([[6],[5],[8],[1.0]])

np.set_printoptions(precision=4,suppress=True)
n = len(A)
B = A
A = np.hstack((A,b))
print('A =\n',A)

#checkค่าในเส้นทเเยงมุมว่ามีค่ามากกว่าใต้เส้นทแยงมุมหรือไหม ถ้ามีน้อยกว่าในสลับเเถว
#checkmaxDiagonal for ให้ได้คำตอบที่ถูกต้อง
for i in range(0,n-1):
    for j in range(i+1,n):
        if A[i,i] < A[j,i]:
            temp = np.array(A[i,:])
            A[i,:] = A[j,:]
            A[j,:] = temp
            print('A = \n',A)

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

#check คำตอบ
#A = np.array([[2,-5,0,-1],[3,1,6,-9],[1,3,-5,2],[3,0,8,1]])
#A = np.array([[-1,5,8,-3],[-2,1,-4,-1],[-1,2,0,2],[4,1,5,1]])
A = np.array([[-2,2,1,3],[2,1,0,1],[2,4,-3,1],[1,-2,1,3]])
print('Ax = \n',A@x) #จะได้A@x = b

