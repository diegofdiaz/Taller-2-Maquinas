import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
#Permitir la entrada de simbolos de latex
#plt.rcParams['text.usetex'] = True 
#Index
im=float(input("Digite Im: "))
f= float(input("Digite de la frecuencia electrica: "))
w= 2*np.pi*f
t = np.linspace(0, 4*(1/f) , 500, endpoint=False)
k= float(input("Digite de la constante K: "))
thetha= np.linspace(-2*np.pi, 2*np.pi, 500, endpoint=False)
#Definición del la grafica
fig = plt.figure() #constrained_layout=True
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
#Fijación de los limites de la grafica
limite=max(im*k*np.cos(thetha))+1
#Definición de la animación
for i in range(len(t)):
    ax1.cla()
    ax2.cla()
    t2=t[i]
    b=im*k*np.cos(w*t2)*np.cos(thetha)
    ax1.plot(thetha,b)
    ax1.set_title(" Densidad de campo|B| ")
    ax1.set_ylim(-limite,limite)
    x=im*k*np.cos(w*t2)*np.cos(0)
    y=im*k*np.cos(w*t2)*np.sin(0)
    ax2.quiver([0], [0], [x], [y], angles='xy', scale_units='xy', scale=1)
    ax2.set_title("Fasor espacial")
    ax2.set_xlim(-limite, limite)
    ax2.set_ylim(-limite,limite)
    plt.ion()
    ax1.grid()
    ax2.grid()
    plt.show()
    plt.pause(0.05)
    