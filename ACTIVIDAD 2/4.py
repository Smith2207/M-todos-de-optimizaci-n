#Un servidor web procesa x peticiones por segundo, y el uso de CPU sigue la fórmula 2x^2 + 10x.
#La CPU no puede exceder el 80 % de uso. Minimiza el uso de CPU sin caer por debajo del umbral
#de procesamiento de 10 peticiones por segundo


import numpy as np
import matplotlib.pyplot as plt

capacidad_cpu = 100  # Capacidad total de CPU 
limite_cpu = 0.8 * capacidad_cpu  # CPU al 80%
min_peticiones = 10  # Mínimo de peticiones
# uso de CPU
def uso_cpu(x):
    return 2 * x**2 + 10 * x

# Generación de valores de peticiones
peticiones = np.arange(min_peticiones, 30, 0.1)
usos_cpu = uso_cpu(peticiones)

indices_optimos = np.where(usos_cpu <= limite_cpu)[0]

if len(indices_optimos) > 0:
    indice_optimo = indices_optimos[-1] 
    peticiones_optimas = peticiones[indice_optimo]
else:
    peticiones_optimas = min_peticiones  

plt.plot(peticiones, usos_cpu, label='Uso de CPU', color='blue', linewidth=2)
plt.axhline(y=limite_cpu, color='red', linestyle='--', label='Límite de CPU (80%)', linewidth=2)
plt.axvline(x=peticiones_optimas, color='green', linestyle='--', label='Peticiones óptimas', linewidth=2)
plt.xlabel('Peticiones por segundo')
plt.ylabel('Uso de CPU (%)')
plt.title('Minimización del uso de CPU')
plt.grid(True)
plt.legend()

# ver todo el uso de CPU 
plt.ylim(0, max(usos_cpu) + 10)  
plt.show()
print("El número óptimo de peticiones por segundo es:", peticiones_optimas)
