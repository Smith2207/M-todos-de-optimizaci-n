
#El entrenamiento de un modelo de deep learning en una GPU consume x unidades de energía por
#lote. El objetivo es maximizar el tamaño del lote x, pero el consumo de energía total no puede
#exceder las 200 unidades por segundo, y cada lote adicional más allá del 10 reduce el rendimiento en un 10 %.
import numpy as np
import matplotlib.pyplot as plt

def energia_consumida(x):
    # Si el tamaño del lote es mayor que 10, reduce el rendimiento en un 10% por lote adicional
    if x <= 10:
        return x  
    else:
        return x * (1 - 0.1 * (x - 10))  

def consumo_total(x):
    return x * energia_consumida(x)

x_values = np.linspace(1, 20, 100)
consumo = np.array([consumo_total(x) for x in x_values])

x_max = np.max(x_values[consumo <= 200])

plt.figure(figsize=(10, 6))
plt.plot(x_values, consumo, label='Consumo total de energía', color='b')
plt.axhline(y=200, color='r', linestyle='--', label='Restricción de 200 unidades de energía')
plt.axvline(x=x_max, color='g', linestyle='--', label=f'Máximo en x={x_max:.2f}')
plt.plot(x_max, consumo_total(x_max), 'go', label=f'Tamaño de lote máximo: {x_max:.2f}')
plt.axvline(x=10, color='purple', linestyle='--', label='Límite de rendimiento óptimo')
plt.plot(10, consumo_total(10), 'mo', label='Consumo total en tamaño de lote 10') 
plt.title('Consumo total de energía vs Tamaño de lote')
plt.xlabel('Tamaño de lote (x)')
plt.ylabel('Consumo total de energía (unidades)')
plt.grid(True)
plt.legend()

plt.show()

print(f"El tamaño de lote máximo que satisface la restricción de 200 unidades de energía es aproximadamente: {x_max:.2f}.")
print(f"Consumo total de energía para el tamaño de lote máximo ({x_max:.2f}): {consumo_total(x_max):.2f} unidades.")
