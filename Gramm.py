from numpy.linalg import norm
import math
import numpy as np
np.set_printoptions(precision = 2, suppress =True)

def gramm_schmidt(v):
    u = np.zeros(v.shape)
    w = np.zeros(v.shape)
    u[0] = v[0]
    for k in range(1,len(v)):
        C = np.zeros(u[0].shape)
        for j in range(0,k):
            C = C + v[k]@u[j]/norm(u[j])**2 * u[j]
        u[k] = v[k] - C
        w[k] = u[k]/norm(u[k]) #orthonormal vector
    w[0] = u[0]/norm(u[0])
    print('ฐานเชิงตั้งฉาก คือ \n',u)
    print('ฐานเชิงตั้งฉากปกติ คือ \n',w)
    return u,w

#v = np.array([[1,2],[3,4]])
v = np.array([[1,1,0],[2,0,1],[2,2,1]])
#2.1
v = np.array([[3,2,4],[1,3,0],[0,5,5]])
#2.2
v = np.array([[8,2],[7,0]])
#2.3
v = np.array([[math.sqrt(2),0,1],[1,math.sqrt(2),math.sqrt(2)],[1,0,2]])
#2.4
v = np.array([[-4,2,1],[8,5,7],[3,-2,4]])
#2.5
v = np.array([[2,3,7],[-1,9,2],[4,-5,4]])
#2.6
v = np.array([[9,math.sqrt(2),2],[1,6,2],[3,5,math.pi]])


v = np.array([[1,math.sqrt(3),1/2],[1/math.sqrt(3),5,1],[-2,math.pi,5]])
print('v = \n',v)
gramm_schmidt(v)

