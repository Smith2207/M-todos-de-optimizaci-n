#Un script de Python tarda 5x+2 segundos en procesar x datos. Por cada dato adicional, el tiempo
#de ejecución crece linealmente. Sin embargo, el sistema tiene un límite de tiempo de ejecución de
#50 segundos. ¿Cuál es el número máximo de datos que puede procesar el script?
#
import numpy as np
import matplotlib.pyplot as plt

t_maximo = 50
x = np.arange(0, 12)  
t_ejecucion = 5 * x + 2
x_max = (t_maximo - 2) / 5
maximo_datos = int(x_max)

print(f"El número máximo de datos que puede procesar el script es: {maximo_datos}")
plt.figure(figsize=(10, 6))
plt.plot(x, t_ejecucion, label='Tiempo de Ejecución (5x + 2)', color='green')
plt.axhline(y=t_maximo, color='red', linestyle='--', label='Tiempo Máximo Permitido (50 s)')
plt.axvline(x=maximo_datos, color='orange', linestyle='--', label=f'Máximo Datos: {maximo_datos}')
plt.title('Relación entre el Número de Datos y el Tiempo de Ejecución')
plt.xlabel('Número de Datos (x)')
plt.ylabel('Tiempo de Ejecución (s)')
plt.xlim(0, 20)
plt.ylim(0, 60)
plt.grid()
plt.legend()
plt.show()
