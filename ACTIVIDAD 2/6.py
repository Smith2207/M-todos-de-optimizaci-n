#Un sistema de transmisión de datos tiene un ancho de banda total de 1000 Mbps. Cada archivo
#que se transmite utiliza x Mbps. El sistema puede transmitir un máximo de 50 archivos a la vez,
#y cada archivo adicional más allá de 30 reduce el ancho de banda disponible en un 5 %. Maximiza
#el número de archivos transmitidos.

import numpy as np
import matplotlib.pyplot as plt

# Parámetros
ab_total = 1000  # Mbps
x = 20  # AB x archivo
max_archivos = 50  

def ab_disponible(n):
    return ab_total if n <= 30 else ab_total * (1 - 0.05 * (n - 30))

ab_usado = np.arange(1, max_archivos + 1) * x
ab_disponible_lista = np.array([ab_disponible(n) for n in range(1, max_archivos + 1)])

archivos_maximos = np.max(np.where(ab_usado <= ab_disponible_lista)[0]) + 1   #np.where para las condiciones dentro del array

# Graficar
plt.plot(ab_usado, label='Ancho de Banda Usado', color='blue', linewidth=2)
plt.plot(ab_disponible_lista, label='Ancho de Banda Disponible', color='red', linestyle='--', linewidth=2)
plt.axvline(x=archivos_maximos, color='green', linestyle='--', label=f'Máx Archivos: {archivos_maximos}', linewidth=2)

plt.xlabel('Número de Archivos Transmitidos')
plt.ylabel('Ancho de Banda (Mbps)')
plt.title('Maximización del Número de Archivos Transmitidos')
plt.grid(True)
plt.legend()
plt.show()

print(f"El número máximo de archivos que se pueden transmitir es: {archivos_maximos}")
