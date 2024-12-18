import streamlit as st
from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, lpSum
import matplotlib.pyplot as plt
import numpy as np

st.title("Resolución de Problemas de Programación Lineal Entera (ILP)")
st.markdown("---")
st.write("Selecciona uno de los problemas predefinidos para resolver de forma interactiva.")

enunciados = {
    "Problema 1: Maximización de Ganancias": "Una empresa produce dos productos, A y B. Cada unidad de A genera una ganancia de $3 y cada unidad de B genera una ganancia de $5. Las restricciones son: no se pueden producir más de 4 unidades de A, se pueden producir hasta 12 unidades de B, y el tiempo total de producción no puede superar las 18 horas, donde A consume 3 horas y B consume 2 horas por unidad. Maximiza las ganancias.",
    "Problema 2: Minimización de Costos": "Una compañía quiere minimizar los costos de transporte entre dos almacenes. El costo por enviar una unidad de producto desde el almacén 1 es $2 y desde el almacén 2 es $3. La demanda total es de 5 unidades y se puede enviar un máximo de 6 unidades desde el almacén 1. Minimiza el costo total.",
    "Problema 3: Producción Óptima": "Una fábrica produce dos tipos de productos, X y Y. Cada unidad de X genera un beneficio de $50 y cada unidad de Y genera $40. Las restricciones son: no se pueden usar más de 40 horas en la máquina 1 y no más de 60 horas en la máquina 2. X consume 1 hora en la máquina 1 y 3 horas en la máquina 2, mientras que Y consume 2 horas en la máquina 1 y 1 hora en la máquina 2. Maximiza los beneficios.",
    "Problema 4: Asignación de Recursos": "Una empresa debe asignar recursos a tres proyectos para minimizar costos. Los costos asociados son $4, $6 y $9 por unidad asignada a los proyectos 1, 2 y 3, respectivamente. La disponibilidad de recursos es de 8 unidades para los proyectos 1 y 2 juntos, y 5 unidades para los proyectos 2 y 3 juntos. Minimiza el costo total."
}

problemas = {
    "Problema 1: Maximización de Ganancias": {
        "tipo": LpMaximize,
        "objetivo": [3, 5],
        "restricciones": [
            {"coef": [1, 0], "rhs": 4},
            {"coef": [0, 2], "rhs": 12},
            {"coef": [3, 2], "rhs": 18}
        ]
    },
    "Problema 2: Minimización de Costos": {
        "tipo": LpMinimize,
        "objetivo": [2, 3],
        "restricciones": [
            {"coef": [1, 1], "rhs": 5},
            {"coef": [2, 1], "rhs": 6}
        ]
    },
    "Problema 3: Producción Óptima": {
        "tipo": LpMaximize,
        "objetivo": [50, 40],
        "restricciones": [
            {"coef": [1, 2], "rhs": 40},
            {"coef": [3, 1], "rhs": 60}
        ]
    },
    "Problema 4: Asignación de Recursos": {
        "tipo": LpMinimize,
        "objetivo": [4, 6, 9],
        "restricciones": [
            {"coef": [1, 1, 0], "rhs": 8},
            {"coef": [0, 1, 1], "rhs": 5}
        ]
    }
}

# Selección del problema
st.header("Selecciona un problema")
seleccion = st.selectbox("Elige un problema para resolver:", list(problemas.keys()))
st.markdown("---")

st.subheader("Enunciado del Problema")
st.write(enunciados[seleccion])
st.markdown("---")

problema = problemas[seleccion]

modelo = LpProblem("ILP_Problem", problema["tipo"])

num_variables = len(problema["objetivo"])
variables = [LpVariable(f"x{i+1}", lowBound=0, cat="Continuous") for i in range(num_variables)]

modelo += lpSum(problema["objetivo"][i] * variables[i] for i in range(num_variables)), "Función Objetivo"

for i, restriccion in enumerate(problema["restricciones"]):
    modelo += lpSum(restriccion["coef"][j] * variables[j] for j in range(num_variables)) <= restriccion["rhs"], f"Restricción {i+1}"

if st.button("Resolver Problema"):
    estado = modelo.solve()

    st.subheader("Resultados")
    if estado == 1:
        st.write("Estado: Solución Óptima Encontrada")
        for var in variables:
            st.write(f"{var.name} = {var.varValue}")
        st.write(f"Valor de la Función Objetivo: {modelo.objective.value()}")

        if num_variables == 2:  
            x = np.linspace(0, 20, 400)
            fig, ax = plt.subplots()

            for restriccion in problema["restricciones"]:
                y = (restriccion["rhs"] - restriccion["coef"][0] * x) / restriccion["coef"][1]
                ax.plot(x, y, label=f"{restriccion["coef"]} <= {restriccion["rhs"]}")

            ax.fill_between(x, 0, 20, color="gray", alpha=0.2)

            ax.plot([var.varValue for var in variables][0], [var.varValue for var in variables][1], 'ro', label="Solución Óptima")

            ax.set_xlim(0, 20)
            ax.set_ylim(0, 20)
            ax.set_xlabel("x1")
            ax.set_ylabel("x2")
            ax.legend()
            st.pyplot(fig)

    else:
        st.write("No se encontró una solución óptima para este problema.")
st.markdown("---")
