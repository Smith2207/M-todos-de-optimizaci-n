#Un sistema de mensajería tiene una latencia L(x) = 100−2x, donde x es el número de mensajes por
#segundo. La latencia no puede ser inferior a 20 ms debido a restricciones del protocolo. Maximiza
#el número de mensajes enviados sin que la latencia caiga por debajo de este límite.
import numpy as np
import matplotlib.pyplot as plt

def latencia(x):
    return 100 - 2 * x

def max_mensajes():
    lim_latencia = 20
    # Despejamos la inecuación: 100 - 2x >= 20
    max_x = (100 - lim_latencia) / 2
    return max_x

max_x = max_mensajes()

x_values = np.linspace(0, 60, 100)  
latencia_values = latencia(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, latencia_values, label='Latencia (ms)', color='blue')
plt.axhline(20, color='red', linestyle='--', label='Límite de latencia (20 ms)')
plt.axvline(max_x, color='green', linestyle='--', label='Máximo mensajes')
plt.scatter(max_x, latencia(max_x), color='green', s=100, zorder=5)

plt.title('Latencia vs. Número de Mensajes por Segundo')
plt.xlabel('Número de Mensajes por Segundo (x)')
plt.ylabel('Latencia (ms)')
plt.xlim(0, 60)
plt.ylim(0, 100)
plt.grid()
plt.legend()
plt.show()

print(f"La cantidad máxima de mensajes que se puede enviar sin que la latencia caiga por debajo de 20 ms es: {max_x:.2f} mensajes por segundo")
