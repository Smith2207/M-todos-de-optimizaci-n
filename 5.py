
#Durante el entrenamiento de un modelo de machine learning, el batch size x afecta el tiempo de
#entrenamiento T(x) = 1000/x + 0,1x. El tamaño del lote debe estar entre 16 y 128. Encuentra el
#batch size que minimiza el tiempo de entrenamiento
import numpy as np
import matplotlib.pyplot as plt

def T(x):
    return 1000 / x + 0.1 * x

# rango de batch sizes segun enunciado
batch_sizes = np.arange(16, 129)  
# Calculamos los tiempos de entrenamiento para cada batch size
tiempos = T(batch_sizes)

# encontramos el batch que minimiza el tiempo
batch_size_optimo = batch_sizes[np.argmin(tiempos)] #arming encunetra el índice del valor mínimo
tiempo_optimo = T(batch_size_optimo)

print("El batch size óptimo es:", batch_size_optimo)
print("El tiempo de entrenamiento mínimo es:", tiempo_optimo)
 
plt.plot(batch_sizes, tiempos, label='Tiempo de Entrenamiento T(x)', color='green', linewidth=2)
plt.axvline(x=batch_size_optimo, color='orange', linestyle='--', label='Batch Size Óptimo', linewidth=2)
plt.xlabel('Batch Size')
plt.ylabel('Tiempo de Entrenamiento')
plt.title('Minimización del Tiempo de Entrenamiento')
plt.grid(True)
plt.legend()
plt.show()
