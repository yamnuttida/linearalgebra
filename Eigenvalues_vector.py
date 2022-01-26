import numpy as np
from numpy.linalg import eig , norm
np.set_printoptions(precision = 2, suppress = True)
'''
A = np.array([[3,0],[8,-1]])
values,vectors = eig(A)
print('ค่าลักษณะเฉพาะ (Eigenvalues) คือ \n',values)
print('เวกเตอร์ลักษณะเฉพาะ (Eigenvectors) คือ \n',vectors)
print('ขนาดของเวกเตอร์ลักษณะเฉพาะ คือ')
print(norm(vectors[:,0])) #ของ[0,1]
print(norm(vectors[:,1])) #ของ[0.45,0.89]

A = np.array([[0,0,-2],[1,2,1],[1,0,3]])
values,vectors = eig(A)
print('ค่าลักษณะเฉพาะ (Eigenvalues) คือ \n',values)
print('เวกเตอร์ลักษณะเฉพาะ (Eigenvectors) คือ \n',vectors)
print('ขนาดของเวกเตอร์ลักษณะเฉพาะ คือ')
print(norm(vectors[:,0])) #ของ[0,1,0] ต้องมีค่าเป็น1
print(norm(vectors[:,1])) #ของ[-0.82,0.41,0.41] ต้องมีค่าเป็น1
print(norm(vectors[:,2])) #ของ[0.71,0,-0.71] ต้องมีค่าเป็น1

A = np.array([[4,0,1],[-2,1,0],[-2,0,1]])
values,vectors = eig(A)
print('ค่าลักษณะเฉพาะ (Eigenvalues) คือ \n',values)
print('เวกเตอร์ลักษณะเฉพาะ (Eigenvectors) คือ \n',vectors)
print('ขนาดของเวกเตอร์ลักษณะเฉพาะ คือ')
print(norm(vectors[:,0])) #ของ[0,1,0] ต้องมีค่าเป็น1
print(norm(vectors[:,1])) #ของ[-0.82,0.41,0.41] ต้องมีค่าเป็น1
print(norm(vectors[:,2])) #ของ[0.71,0,-0.71] ต้องมีค่าเป็น1
'''
A1 = A = np.array([[6,2],[2,3]])
values,vectors = eig(A)
print('ค่าลักษณะเฉพาะ (Eigenvalues) คือ \n',values)
print('เวกเตอร์ลักษณะเฉพาะ (Eigenvectors) คือ \n',vectors)
print('ขนาดของเวกเตอร์ลักษณะเฉพาะ คือ')
print(norm(vectors[:,0])) ;print(norm(vectors[:,1]))
'''
A2 = A = np.array([[2,3],[4,3]])
values,vectors = eig(A)
print('ค่าลักษณะเฉพาะ (Eigenvalues) คือ \n',values)
print('เวกเตอร์ลักษณะเฉพาะ (Eigenvectors) คือ \n',vectors)
print('ขนาดของเวกเตอร์ลักษณะเฉพาะ คือ')
print(norm(vectors[:,0])) ;print(norm(vectors[:,1]))

A3 = A = np.array([[1,2,9],[12,11,2],[0,0,4]])
values,vectors = eig(A)
print('ค่าลักษณะเฉพาะ (Eigenvalues) คือ \n',values)
print('เวกเตอร์ลักษณะเฉพาะ (Eigenvectors) คือ \n',vectors)
print('ขนาดของเวกเตอร์ลักษณะเฉพาะ คือ')
print(norm(vectors[:,0])) ;print(norm(vectors[:,1]))

A4 = A = np.array([[2,1,3],[1,-2,1],[0,5,8]])
values,vectors = eig(A)
print('ค่าลักษณะเฉพาะ (Eigenvalues) คือ \n',values)
print('เวกเตอร์ลักษณะเฉพาะ (Eigenvectors) คือ \n',vectors)
print('ขนาดของเวกเตอร์ลักษณะเฉพาะ คือ')
print(norm(vectors[:,0])) ;print(norm(vectors[:,1]));print(norm(vectors[:,2]))

B4 = B = np.array([[2,0,6],[-2,3,-2],[0,0,-4]])
values,vectors = eig(B)
print('ค่าลักษณะเฉพาะ (Eigenvalues) คือ \n',values)
print('เวกเตอร์ลักษณะเฉพาะ (Eigenvectors) คือ \n',vectors)
print('ขนาดของเวกเตอร์ลักษณะเฉพาะ คือ')
print(norm(vectors[:,0])) ;print(norm(vectors[:,1]));print(norm(vectors[:,2]))

'''