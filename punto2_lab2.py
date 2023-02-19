import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
im=2
f= 60
w= 2*np.pi*f
t = np.linspace(0, 4*(1/f) , 500, endpoint=False)
k=10
thetha= np.linspace(-2*np.pi, 2*np.pi, 500, endpoint=False)
theta1 = np.linspace(0,2*np.pi, 500)
fig = plt.figure()
ax1 = plt.subplot(121)
ax2 = plt.subplot(122, projection='polar')
for i in range(len(t)):
    ax1.cla()
    ax2.cla()
    t2=t[i]
    b=k*np.cos(w*t2)*np.cos(thetha)
    ax1.plot(thetha,b)
    ax1.set_ylim(-10,10)
    if k*np.cos(w*t2)<0:
        x=np.pi
    else :
        x=0
    ax2.arrow([x,0],[abs(k*np.cos(w*t2)), 0])
    ax2.set_ylim(0,15)
    plt.ion()
    plt.show()
    plt.pause(0.05)
    