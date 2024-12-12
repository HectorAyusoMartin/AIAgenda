import streamlit as st
import matplotlib.pyplot as plt
from modules.gestor_tareas import GestorTareas
from modules.sugeridor_prioridad import SugeridorDePrioridad

# Inicializar gestor de tareas y sugeridor de prioridades
gestor = GestorTareas()
sugeridor = SugeridorDePrioridad()

# Configuración de la página
st.set_page_config(page_title="AI Agenda", layout="centered")
st.title("📋 AI Agenda")

# Menú principal
st.sidebar.header("Menú")
menu = st.sidebar.radio("Navegación", ["Inicio", "Tareas activas", "Tareas completadas", "Estadísticas"])

if menu == "Inicio":
    st.header("Agregar nueva tarea")

    # Formulario para agregar tareas
    with st.form("form_agregar_tarea"):
        descripcion = st.text_input("Descripción de la tarea", "")
        if descripcion:
            prioridad_sugerida = sugeridor.sugerir_prioridad(descripcion)
            st.write(f"**Prioridad sugerida:** {prioridad_sugerida}")

        prioridad = st.selectbox(
            "Prioridad",
            options=["Alta", "Media", "Baja"],
            index=["Alta", "Media", "Baja"].index(prioridad_sugerida) if descripcion else 1,
        )
        submitted = st.form_submit_button("Agregar tarea")

        if submitted:
            gestor.agregar_tarea(descripcion, prioridad)
            st.success("Tarea agregada exitosamente")

elif menu == "Tareas activas":
    st.header("Tareas activas")
    tareas = gestor.listar_tareas()
    if tareas:
        for idx, tarea in enumerate(tareas, 1):
            st.write(f"{idx}. {tarea['descripcion']} - Prioridad: {tarea['prioridad']}")
    else:
        st.write("No hay tareas activas")

elif menu == "Tareas completadas":
    st.header("Tareas completadas")
    completadas = gestor.listar_completadas()
    if completadas:
        for idx, tarea in enumerate(completadas, 1):
            st.write(f"{idx}. {tarea['descripcion']} - Prioridad: {tarea['prioridad']}")
    else:
        st.write("No hay tareas completadas")

elif menu == "Estadísticas":
    st.header("📊 Estadísticas de tareas")

    # Cálculo de estadísticas
    total_tareas = len(gestor.listar_tareas()) + len(gestor.listar_completadas())
    completadas = len(gestor.listar_completadas())
    activas = len(gestor.listar_tareas())

    if total_tareas > 0:
        # Mostrar métricas
        st.metric("Total de tareas", total_tareas)
        st.metric("Tareas completadas", completadas)
        st.metric("Tareas activas", activas)

        # Gráfico de barras para prioridades
        prioridades = [t["prioridad"] for t in gestor.listar_tareas()]
        prioridades_counts = {"Alta": prioridades.count("Alta"), "Media": prioridades.count("Media"), "Baja": prioridades.count("Baja")}

        fig, ax = plt.subplots()
        ax.bar(prioridades_counts.keys(), prioridades_counts.values(), color=["red", "orange", "green"])
        ax.set_title("Distribución de Prioridades")
        ax.set_ylabel("Cantidad de Tareas")
        st.pyplot(fig)

        # Gráfico de pastel para tareas completadas vs activas
        fig2, ax2 = plt.subplots()
        ax2.pie([completadas, activas], labels=["Completadas", "Activas"], autopct="%1.1f%%", colors=["blue", "gray"])
        ax2.set_title("Tareas Completadas vs Activas")
        st.pyplot(fig2)
    else:
        st.write("No hay tareas registradas todavía")
