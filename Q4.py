import numpy as np
import matplotlib.pyplot as plt

def transform(pt,A):
    newpt = []
    for w in pt:
        newpt.append(A@w)
    return np.array(newpt)

xy = np.array([[0,0],[-2,4],[-2.9,3.5],[-3,2],[0,0]])
'''
A = np.array([[-1,0],[0,1]])
newxy = transform(xy,A)
plt.plot(xy[:,0],xy[:,1],'k')
plt.plot(newxy[:,0],newxy[:,1],'--')
plt.show


A = np.array([[1,0],[0,-1]])
newxy = transform(xy,A)
plt.plot(xy[:,0],xy[:,1],'k')
plt.plot(newxy[:,0],newxy[:,1],'--')
plt.show


A = np.array([[1,0],[0,0.5]])
newxy = transform(xy,A)
plt.plot(xy[:,0],xy[:,1],'k')
plt.plot(newxy[:,0],newxy[:,1],'--')
plt.show

A = np.array([[2,0],[0,0.5]])
newxy = transform(xy,A)
plt.plot(xy[:,0],xy[:,1],'k')
plt.plot(newxy[:,0],newxy[:,1],'--')
plt.show


theta = np.pi
A = np.array([[np.cos(theta),-np.sin(theta)],
                  [np.sin(theta),np.cos(theta)]])
newxy = transform(xy,A)
plt.plot(newxy[:,0],newxy[:,1],'m')
plt.plot(xy[:,0],xy[:,1],'k')
plt.show

'''

theta = 7*np.pi/4
A = np.array([[np.cos(theta),-np.sin(theta)],
                  [np.sin(theta),np.cos(theta)]])
newxy = transform(xy,A)
plt.plot(newxy[:,0],newxy[:,1],'o--')
plt.plot(xy[:,0],xy[:,1],'ok-')
plt.show
    