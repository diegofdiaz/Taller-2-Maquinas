import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
t = np.linspace(-2*np.pi, 2*np.pi, 500, endpoint=False)
x=15
desfase=180/x
desfaseactual=0
wtotal=np.zeros(len(t))
while (desfaseactual+1)<180:
  w=signal.square((t)-(((180+desfaseactual)*np.pi)/180))
  wtotal=wtotal+w
  desfaseactual=desfaseactual+desfase
plt.plot(t, wtotal)
plt.show()