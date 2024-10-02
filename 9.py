#Una empresa almacena datos en la nube. El costo de almacenamiento por TB es de 50+5x dólares,
#donde x es la cantidad de TB de almacenamiento utilizado. La empresa tiene un presupuesto de
#500 dólares. Maximiza la cantidad de datos almacenados sin exceder el presupuesto.

import numpy as np
import matplotlib.pyplot as plt

def costo(x):
    return 50 + 5 * x
  
presupuesto = 500

max_x = (presupuesto - 50) / 5

x_values = np.linspace(0, 100, 100)
costo_values = costo(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, costo_values, label='Costo de almacenamiento', color='blue')
plt.axhline(presupuesto, color='red', linestyle='--', label='Presupuesto ($500)')
plt.axvline(max_x, color='green', linestyle='--', label='Máximo almacenamiento (90 TB)')

plt.title('Costo de Almacenamiento vs. Almacenamiento (TB)')
plt.xlabel('Almacenamiento (TB)')
plt.ylabel('Costo ($)')
plt.xlim(0, 100)
plt.ylim(0, 600)
plt.grid()
plt.legend()
plt.show()

print(f"La cantidad máxima de datos alamacenados sin exceder el presupuesto es: {max_x:.2f} TB")
