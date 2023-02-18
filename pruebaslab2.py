import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
im=2
f= 60
w= 2*np.pi*f
t = np.linspace(0, 4*(1/f) , 500, endpoint=False)
k=10
thetha= np.linspace(-2*np.pi, 2*np.pi, 500, endpoint=False)
fig = plt.figure()
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
limite=max(im*k*np.cos(thetha))
for i in range(len(t)):
    ax1.cla()
    ax2.cla()
    t2=t[i]
    b=im*k*np.cos(w*t2)*np.cos(thetha)
    ax1.plot(thetha,b)
    ax1.set_ylim(-limite,limite)
    x=k*np.cos(w*t2)*np.cos(0)
    y=k*np.cos(w*t2)*np.sin(0)
    ax2.quiver([0], [0], [x], [y], angles='xy', scale_units='xy', scale=1)
    ax2.set_xlim(-limite, limite)
    ax2.set_ylim(-limite,limite)
    plt.ion()
    plt.show()
    plt.pause(0.05)
    