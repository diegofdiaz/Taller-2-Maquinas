import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy import constants as c
t = np.linspace(-2*np.pi, 2*np.pi, 5000, endpoint=False)
g=float(input("Por favor digite el valor de g: "))
N=int(input("Por favor digite el valor de N: "))
I=float(input("Por favor digite el valor de I: "))
X=int(input("Por favor digite el valor de X: "))
while (X>15) or (1>X):
  X=int(input('Por favor digite el valor de X, recuerde que debe estar entre 1 y 15: '))
desfase=180/X
desfaseactual=0
wtotal=np.zeros(len(t))
while (desfaseactual+1)<180:
  w=(c.mu_0*N*I/(2*g))*(signal.square((t)-(((186+desfaseactual)*np.pi)/180)))
  wtotal=wtotal+w
  desfaseactual=desfaseactual+desfase
plt.plot(t*(180/np.pi), wtotal)
plt.ylabel("B[T]")
plt.xlabel("Grados (°)")
plt.title("Densidad de campo magnetico vs θ")
plt.grid()
plt.show()