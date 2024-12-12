import streamlit as st
import matplotlib.pyplot as plt
from modules.gestor_tareas import GestorTareas
from modules.sugeridor_prioridad import SugeridorDePrioridad


gestor = GestorTareas()
sugeridor = SugeridorDePrioridad()


st.set_page_config(page_title="AI Agenda", layout="wide")



st.sidebar.markdown("---")
st.sidebar.markdown("Autor: Héctor Ayuso Martín")
st.sidebar.markdown("[Repositorio](https://github.com/HectorAyusoMartin/AIAgenda.git)")
st.sidebar.markdown("[Linkedin](https://www.linkedin.com/in/hector-ayuso-martin)")


menu = st.sidebar.radio("Menú", ["Inicio", "Tareas activas", "Tareas completadas", "Estadísticas", "Búsqueda de tareas", "Editar tarea", "Marcar como completada", "Eliminar tarea"])

if menu == "Inicio":
    st.header("Agregar nueva tarea")

    
    with st.form("form_agregar_tarea"):
        descripcion = st.text_input("Descripción de la tarea", "")
        if descripcion:
            prioridad_sugerida = sugeridor.sugerir_prioridad(descripcion)
            st.markdown(f"**Prioridad sugerida:** {prioridad_sugerida}")

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
            st.markdown(f"**{idx}.** {tarea['descripcion']} - Prioridad: {tarea['prioridad']}")
    else:
        st.warning("No hay tareas activas")

elif menu == "Tareas completadas":
    st.header("Tareas completadas")
    completadas = gestor.listar_completadas()
    if completadas:
        for idx, tarea in enumerate(completadas, 1):
            st.markdown(f"**{idx}.** {tarea['descripcion']} - Prioridad: {tarea['prioridad']}")
    else:
        st.info("No hay tareas completadas")

elif menu == "Estadísticas":
    st.header("Estadísticas de tareas")

    
    total_tareas = len(gestor.listar_tareas()) + len(gestor.listar_completadas())
    completadas = len(gestor.listar_completadas())
    activas = len(gestor.listar_tareas())

    if total_tareas > 0:
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total de tareas", total_tareas)
        col2.metric("Tareas completadas", completadas, delta=completadas - activas)
        col3.metric("Tareas activas", activas)

        
        prioridades = [t["prioridad"] for t in gestor.listar_tareas()]
        prioridades_counts = {"Alta": prioridades.count("Alta"), "Media": prioridades.count("Media"), "Baja": prioridades.count("Baja")}

        fig, ax = plt.subplots()
        ax.bar(prioridades_counts.keys(), prioridades_counts.values(), color=["red", "orange", "green"])
        ax.set_title("Distribución de Prioridades")
        ax.set_ylabel("Cantidad de Tareas")
        st.pyplot(fig)

        
        fig2, ax2 = plt.subplots()
        ax2.pie([completadas, activas], labels=["Completadas", "Activas"], autopct="%1.1f%%")
        ax2.set_title("Tareas Completadas vs Activas")
        st.pyplot(fig2)
    else:
        st.write("No hay tareas registradas todavía")

elif menu == "Búsqueda de tareas":
    st.header("Búsqueda de tareas")
    palabra_clave = st.text_input("Escribe una palabra clave para buscar tareas")
    if st.button("Buscar"):
        resultados = gestor.buscar_tareas(palabra_clave)
        if resultados:
            for idx, tarea in enumerate(resultados, 1):
                st.markdown(f"**{idx}.** {tarea['descripcion']} - Prioridad: {tarea['prioridad']}")
        else:
            st.error("No se encontraron tareas que coincidan con la palabra clave")

elif menu == "Editar tarea":
    st.header("Editar tarea")
    tareas = gestor.listar_tareas()
    if tareas:
        tarea_idx = st.selectbox("Selecciona una tarea para editar", options=range(len(tareas)), format_func=lambda x: tareas[x]['descripcion'])
        nueva_descripcion = st.text_input("Nueva descripción", tareas[tarea_idx]['descripcion'])
        nueva_prioridad = st.selectbox("Nueva prioridad", options=["Alta", "Media", "Baja"], index=["Alta", "Media", "Baja"].index(tareas[tarea_idx]['prioridad']))
        if st.button("Guardar cambios"):
            gestor.editar_tarea(tarea_idx, nueva_descripcion, nueva_prioridad)
            st.success("Tarea editada correctamente")
    else:
        st.warning("No hay tareas para editar")

elif menu == "Marcar como completada":
    st.header("Marcar tarea como completada")
    tareas = gestor.listar_tareas()
    if tareas:
        tarea_idx = st.selectbox("Selecciona una tarea para completar", options=range(len(tareas)), format_func=lambda x: tareas[x]['descripcion'])
        if st.button("Marcar como completada"):
            gestor.marcar_completada(tarea_idx)
            st.success("Tarea marcada como completada")
    else:
        st.info("No hay tareas para completar")

elif menu == "Eliminar tarea":
    st.header("Eliminar tarea")
    tareas = gestor.listar_tareas()
    if tareas:
        tarea_idx = st.selectbox("Selecciona una tarea para eliminar", options=range(len(tareas)), format_func=lambda x: tareas[x]['descripcion'])
        if st.button("Eliminar tarea"):
            gestor.eliminar_tarea(tarea_idx)
            st.success("Tarea eliminada correctamente")
    else:
        st.warning("No hay tareas para eliminar")
