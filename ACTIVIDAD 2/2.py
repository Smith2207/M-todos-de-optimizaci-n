#Un sistema distribuido tiene 20 nodos. Cada nodo puede procesar x peticiones por segundo. El
#sistema en su conjunto no puede procesar más de 400 peticiones por segundo debido a limitaciones
#de red. Maximiza el número de peticiones procesadas sin exceder la capacidad de la red.
import matplotlib.pyplot as plt
import numpy as np

nodos_t = 20
cap_red = 400

capacidades_nodo = np.linspace(1, 50, 50)  
peticiones_totales = []

for cap_nodo in capacidades_nodo:
    peticiones_total = min(nodos_t * cap_nodo, cap_red)
    peticiones_totales.append(peticiones_total)

plt.plot(capacidades_nodo, peticiones_totales)
plt.xlabel("Capacidad por nodo (peticiones/segundo)")
plt.ylabel("Capacidad total de la red (peticiones/segundo)")
plt.title("Capacidad de la red en función de la capacidad por nodo")
plt.grid(True)
plt.show()