import numpy as np
A = np.array([[-1,3,2],[1,2,-3],[2,1,-2]])
np.set_printoptions(precision=2,suppress=True)
print('A = \n',A)

n = len(A)
I = np.identity(n)
A = np.hstack((A,I)) # A|I

#สามเหลี่ยมบน
for i in range(0,n-1):
    d = A[i,i]
    A[i,:] = A[i,:]/A[i,i]
    print('R%d = R%d%2.2f'%(i+1,i+1,d))
    print('A = \n',A)
    print()
    for j in range(i+1,n):
        lamp = -A[j,i]/A[i,i]
        A[j,:] = A[j,:] + lamp*A[i,:]
        print('R%d = R%d + %2.2f R%d'%(j+1,j+1,lamp,i+1))
        print('A = \n',A)
        print()

#สามเหลี่ยมล่าง        
for i in range(n-1,-1,-1):
    A[i,:] = A[i,:]/A[i,i]
    print('R%d = R%d%2.2f'%(i+1,i+1,d))
    print('A\n',A)
    print()
    for j in range(i-1,-1,-1):
        lamp = -A[j,i]/A[i,i]
        A[j,:] = A[j,:] + lamp*A[i,:]
        print('R%d = R%d + %2.2f R%d'%(j+1,j+1,lamp,i+1))
        print('A = \n',A)
        print()
'''
#แนวทแยงมุมหลักเป็น 1                  
for i in range(0,n):
    A[i,:] = A[i,:]/A[i,i] 
print('A = \n',A)                                                                                                                                                                                                                                                      
'''
B = A[:,n:]
print('inv A = \n',B)
