
#Un sistema de colas procesa x trabajos por segundo. La función del tiempo de respuesta T(x) =
#100/x + 2x. Minimiza el tiempo de respuesta del sistema, considerando que el sistema debe procesar
#al menos 5 trabajos por segundo.
import numpy as np
import matplotlib.pyplot as plt

def T(x):
    return 100 / x + 2 * x

x_values = np.linspace(5, 15, 100) 
T_values = T(x_values)

min_x = 7.07
min_T = T(min_x)

print(f"El valor de x que minimiza T(x) es: {min_x:.2f}")
print(f"El tiempo de respuesta mínimo correspondiente es: {min_T:.2f}")

plt.figure(figsize=(10, 6))
plt.plot(x_values, T_values, label='T(x)', color='blue')
plt.scatter(min_x, min_T, color='red', label='Mínimo (x=7.07)', zorder=5)
plt.title('Tiempo de Respuesta T(x)')
plt.xlabel('Trabajos por segundo (x)')
plt.ylabel('Tiempo de Respuesta T(x)')
plt.axhline(min_T, color='gray', linestyle='--', label=f'Tiempo Mínimo: {min_T:.2f}')
plt.axvline(min_x, color='gray', linestyle='--')
plt.legend()
plt.grid()
plt.xlim(5, 15)
plt.ylim(0, 40)
plt.show()
