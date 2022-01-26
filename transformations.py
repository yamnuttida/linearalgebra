
import numpy as np
import matplotlib.pyplot as plt

def transform(pt,A):
    newpt = []
    for w in pt:
        newpt.append(A@w)
    return np.array(newpt)

'''
#---------------2miti---------------
xy = np.loadtxt("data1.csv", delimiter = ",")
print(xy.shape)

#---------------tranform---------------
#สะท้อนแกน x
A = np.array([[-1,0],[0,1]])
newxy = transform(xy,A)
plt.plot(xy[:,0],xy[:,1],'k')
plt.plot(newxy[:,0],newxy[:,1],'r')
plt.show

#สะท้อนแกน y
A = np.array([[1,0],[0,-1]])
newxy = transform(xy,A)
plt.plot(xy[:,0],xy[:,1],'k')
plt.plot(newxy[:,0],newxy[:,1],'b')
plt.show

#ขยาย 2 เท่า 
A = np.array([[2,0],[0,2]])
newxy = transform(xy,A)
plt.plot(xy[:,0],xy[:,1],'k')
plt.plot(newxy[:,0],newxy[:,1],'g')
plt.show

#หด 0.5 เท่า 
A = np.array([[0.5,0],[0,0.5]])
newxy = transform(xy,A)
plt.plot(xy[:,0],xy[:,1],'k')
plt.plot(newxy[:,0],newxy[:,1],'y')
plt.show

#---------------rotation---------------
for k in range(12):
    theta = k*np.pi/6
    A = np.array([[np.cos(theta),-np.sin(theta)],
                  [np.sin(theta),np.cos(theta)]])
    newxy = transform(xy,A)
    plt.plot(newxy[:,0],newxy[:,1],'m')
plt.plot(xy[:,0],xy[:,1],'k')
plt.show
'''

#---------------3miti---------------
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
xy = np.loadtxt("helix.csv", delimiter = ",")
print(xy.shape)

fig = plt.figure()
ax = fig.gca(projection = '3d')
for k in range(12):
    theta = k*np.pi/6
    A = np.array([[np.cos(theta),-np.sin(theta),0],
                  [np.sin(theta),np.cos(theta),0],
                  [0,0,1]])
    newxy = transform(xy,A)
    if k%2==0: 
        ax.plot(newxy[:,0],newxy[:,1],newxy[:,2],'k')
    if k%2==1:
        ax.plot(newxy[:,0],newxy[:,1],newxy[:,2],'y')
    '''
    if k%5==0: 
        ax.plot(newxy[:,0],newxy[:,1],newxy[:,2],'g')
    if k%5==1:
        ax.plot(newxy[:,0],newxy[:,1],newxy[:,2],'r')
    if k%5==2:
        ax.plot(newxy[:,0],newxy[:,1],newxy[:,2],'c')
    if k%5==3:
        ax.plot(newxy[:,0],newxy[:,1],newxy[:,2],'b')
    if k%5==4:
        ax.plot(newxy[:,0],newxy[:,1],newxy[:,2],'m')
    '''
ax.plot(xy[:,0],xy[:,1],xy[:,2],'k')
plt.show

