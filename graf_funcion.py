import numpy as np
import matplotlib.pyplot as plt

funcion = input("Ingrese función f(x): ")
min = float(input("min intervalo: "))
max = float(input("max intervalo: "))
x = np.linspace(min, max, 1000)
y = eval(funcion)
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-')
plt.title(f'Gráfica de la función {funcion}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.ylim(np.min(y), np.max(y))
plt.show()
