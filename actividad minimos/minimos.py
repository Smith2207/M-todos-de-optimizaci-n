import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Optimización No Lineal - Resolución Detallada")

# Menú de navegación
st.sidebar.title("Ejercicios") 
opcion = st.sidebar.radio(
    "Selecciona un ejercicio",
    (
        "Ejercicio 1: Minimizadores globales o locales",
        "Ejercicio 2: Función |x|",
        "Ejercicio 3: Teorema de Weierstrass",
        "Ejercicio 4: Mínimo global en 2D",
        "Ejercicio 5: Ejemplo de mínimo global no único"
    )
)

# Ejercicio 1
if opcion == "Ejercicio 1: Minimizadores globales o locales":
    st.header("Ejercicio 1: Verificar minimizadores globales o locales")
    st.markdown("""
    La función a evaluar es:
    """)
    st.latex(r"f(x) = x^2 - 4x + 5")
    st.markdown("""
    **Paso 1:** Reescribimos \( f(x) \) completando el cuadrado:
    """)
    st.latex(r"f(x) = (x - 2)^2 + 1")
    st.markdown("""
    - Este término alcanza su valor mínimo en \( x = 2 \).
    - Evaluamos en \( x = 2 \): \( f(2) = (2 - 2)^2 + 1 = 1 \).
    - En \( x = 0 \): \( f(0) = (0 - 2)^2 + 1 = 5 \).
    
    **Conclusión:** \( x = 2 \) es un **mínimo global**, mientras que \( x = 0 \) no es un mínimo.
    """)

    # Gráfico
    x = np.linspace(-2, 6, 100)
    f_x = x**2 - 4*x + 5

    fig, ax = plt.subplots()
    ax.plot(x, f_x, label=r"$f(x) = x^2 - 4x + 5$")
    ax.scatter([2], [1], color="red", label="Mínimo global (x=2)")
    ax.scatter([0], [5], color="blue", label="No es mínimo (x=0)")
    ax.set_title("Gráfico de f(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    st.pyplot(fig)

# Ejercicio 2
elif opcion == "Ejercicio 2: Función |x|":
    st.header("Ejercicio 2: Función |x|")
    st.markdown("""
    **Función a analizar:**  
    \( f(x) = |x| \)
    
    **Paso 1:** La función \( f(x) = |x| \) tiene forma de "V".  
    **Paso 2:** Evaluamos en \( x = 0 \):  
    \( f(0) = |0| = 0 \), que es el valor más pequeño que puede tomar la función.
    
    **Conclusión:** \( x = 0 \) es un **mínimo global**.
    """)

    # Gráfico
    x = np.linspace(-5, 5, 100)
    f_abs_x = np.abs(x)

    fig2, ax2 = plt.subplots()
    ax2.plot(x, f_abs_x, label=r"$f(x) = |x|$")
    ax2.scatter([0], [0], color="red", label="Mínimo global (x=0)")
    ax2.set_title("Gráfico de f(x) = |x|")
    ax2.set_xlabel("x")
    ax2.set_ylabel("f(x)")
    ax2.legend()
    st.pyplot(fig2)

# Ejercicio 3
elif opcion == "Ejercicio 3: Teorema de Weierstrass":
    st.header("Ejercicio 3: Teorema de Weierstrass")
    st.markdown("""
    **Función a analizar:**  
    \( f(x) = \sin(x) \) en el intervalo \([0, \pi]\).
    
    **Paso 1:** \( f(x) \) es continua en \([0, \pi]\), un intervalo cerrado y acotado.  
    **Paso 2:** Según el Teorema de Weierstrass, una función continua en un dominio cerrado tiene un mínimo global.  
    **Paso 3:** Evaluamos \( f(x) \) en el intervalo:  
    \( f(0) = \sin(0) = 0 \), que es el valor más bajo en \([0, \pi]\).
    
    **Conclusión:** \( x = 0 \) es el **mínimo global**.
    """)

    # Gráfico
    x = np.linspace(0, np.pi, 100)
    f_sin_x = np.sin(x)

    fig3, ax3 = plt.subplots()
    ax3.plot(x, f_sin_x, label=r"$f(x) = \sin(x)$")
    ax3.scatter([0], [0], color="red", label="Mínimo global (x=0)")
    ax3.set_title("Gráfico de f(x) = sin(x) en [0, π]")
    ax3.set_xlabel("x")
    ax3.set_ylabel("f(x)")
    ax3.legend()
    st.pyplot(fig3)

# Ejercicio 4
elif opcion == "Ejercicio 4: Mínimo global en 2D":
    st.header("Ejercicio 4: Mínimo global en 2D")
    st.markdown("""
    **Función a analizar:**  
    \( f(x, y) = x^2 + y^2 \) con \( x^2 + y^2 \leq 1 \).
    
    **Paso 1:** La función \( f(x, y) = x^2 + y^2 \) representa un paraboloide.  
    **Paso 2:** El dominio dado \( x^2 + y^2 \leq 1 \) es un disco de radio 1 centrado en el origen.  
    **Paso 3:** Evaluamos \( f(0, 0) = 0^2 + 0^2 = 0 \).
    
    **Conclusión:** El **mínimo global** está en \( (x, y) = (0, 0) \).
    """)

    # Gráfico 2D
    x = np.linspace(-1, 1, 100)
    y = np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2

    fig4, ax4 = plt.subplots()
    contour = ax4.contourf(X, Y, Z, levels=50, cmap="viridis")
    ax4.scatter([0], [0], color="red", label="Mínimo global (0, 0)")
    ax4.set_title("Gráfico de f(x, y) = x^2 + y^2")
    ax4.set_xlabel("x")
    ax4.set_ylabel("y")
    ax4.legend()
    st.pyplot(fig4)

# Ejercicio 5
elif opcion == "Ejercicio 5: Ejemplo de mínimo global no único":
    st.header("Ejercicio 5: Ejemplo de mínimo global no único")
    st.markdown("""
    **Función a analizar:**  
    \( f(x) = x^4 - 4x^2 + 4 \).
    
    **Paso 1:** Los puntos \( x = -1 \) y \( x = 1 \) cumplen \( f(-1) = f(1) = 0 \).  
    **Paso 2:** Estos puntos son mínimos globales, ya que \( f(x) \geq 0 \) para todo \( x \).
    
    **Conclusión:** Los mínimos globales no son únicos.
    """)

    # Gráfico
    x = np.linspace(-2, 2, 100)
    f_poly = x**4 - 4*x**2 + 4

    fig5, ax5 = plt.subplots()
    ax5.plot(x, f_poly, label=r"$f(x) = x^4 - 4x^2 + 4$")
    ax5.scatter([-1, 1], [0, 0], color="red", label="Mínimos globales (x=-1, x=1)")
    ax5.set_title("Gráfico de f(x) = x^4 - 4x^2 + 4")
    ax5.set_xlabel("x")
    ax5.set_ylabel("f(x)")
    ax5.legend()
    st.pyplot(fig5)

