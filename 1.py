#Un algoritmo necesita procesar datos en lotes. Cada lote requiere x MB de memoria, pero la
#capacidad total de memoria disponible es de 1024 MB. El algoritmo puede procesar un máximo
#de 8 lotes. El objetivo es maximizar la cantidad de datos procesados, pero cada lote más allá del
#quinto reduce su eficiencia en un 20 %

import numpy as np
import matplotlib.pyplot as plt

max_memoria = 1024  # MB
max_lotes = 8    # máximo de lotes

lotes = []
dat_procesados = []

for n in range(1, max_lotes + 1):
    x = max_memoria / n  
    if n <= 5:
        P = n * x  # eficiencia total
    else:
        P = 5 * x + (n - 5) * x * 0.8  # eficiencia reducida
    lotes.append(n)
    dat_procesados.append(P)

plt.figure(figsize=(10, 6))
plt.plot(lotes, dat_procesados, marker='o')
plt.title('Datos procesados en función del número de lotes')
plt.xlabel('Número de Lotes')
plt.ylabel('Datos Procesados (MB)')
plt.xticks(lotes)
plt.grid(True)
plt.axhline(y=max_memoria, color='r', linestyle='--', label='Memoria Total (1024 MB)')
plt.legend()
plt.show()

