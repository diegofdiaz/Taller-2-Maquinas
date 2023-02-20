import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as c
#Permitir la entrada de simbolos de latex
def pol2rect(im,k,w,t2,desfase):
    x=c.mu_0*im*k*np.cos((w*t2)+desfase)*np.cos(desfase)
    y=c.mu_0*im*k*np.cos((w*t2)+desfase)*np.sin(desfase)
    return(x,y)
#plt.rcParams['text.usetex'] = True 
#Index data
im=float(input("Digite Im: "))
f= float(input("Digite de la frecuencia electrica en hz: "))
w= 2*np.pi*f
t = np.linspace(0, 4*(1/f) , 500, endpoint=False)
k= float(input("Digite de la constante K: "))
thetha= np.linspace(-2*np.pi, 2*np.pi, 500, endpoint=False)
#Definición del la grafica
fig = plt.figure() #constrained_layout=True
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
#Fijación de los limites de la grafica
limite=max(c.mu_0*im*k*np.cos(thetha))
#Definición de la animación
for i in range(len(t)):
    ax1.cla()
    ax2.cla()
    t2=t[i]
    fase_a=(c.mu_0)*im*k*np.cos(w*t2)*np.cos(thetha)
    ax1.plot(thetha,fase_a, color="r")
    fase_b=(c.mu_0)*im*k*np.cos((w*t2)-((2*np.pi)/3))*np.cos(thetha-((2*np.pi)/3))
    ax1.plot(thetha,fase_b,color="b")
    fase_c=(c.mu_0)*im*k*np.cos((w*t2)+((2*np.pi)/3))*np.cos(thetha+((2*np.pi)/3))
    ax1.plot(thetha,fase_c, color="y")
    ax1.set_title(" Densidad de campo|B| ")
    ax1.set_ylim(-limite,limite)
    ax1.legend(("Fase a", "Fase b", "Fase c"),prop = {'size': 10}, loc='upper right')
    ax1.grid()
    ax1.set_ylabel("B[T]")
    ax1.set_xlabel("Grados (°)")
    ax1.set_title(" Densidad de campo|B| ")
    x1,y1= pol2rect(im,k,w,t2,0)
    x2,y2= pol2rect(im,k,w,t2,-((2*np.pi)/3))
    x3,y3= pol2rect(im,k,w,t2,((2*np.pi)/3))
    xt=x1+x2+x3
    yt=y1+y2+y3
    ax2.quiver([0], [0], [x1], [y1], angles='xy', scale_units='xy', scale=1, color="r", label='Fase a')
    ax2.quiver([0], [0], [x2], [y2], angles='xy', scale_units='xy', scale=1, color="b", label='Fase b')
    ax2.quiver([0], [0], [x3], [y3], angles='xy', scale_units='xy', scale=1, color="y", label='Fase c')
    ax2.quiver([0], [0], [xt], [yt], angles='xy', scale_units='xy', scale=1, color="c", label='Campo total rotativo')
    ax2.set_title("Fasor espacial")
    ax2.legend(loc='lower right')
    ax2.grid()
    ax2.set_xlim(-(limite+limite/2), (limite+limite/2))
    ax2.set_ylim(-(limite+limite/2),(limite+limite/2))
    plt.ion()
    plt.show()
    plt.pause(0.005)