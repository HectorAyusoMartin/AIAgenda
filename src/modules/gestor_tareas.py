import json
import os

class GestorTareas:
    def __init__(self, archivo="tareas.json"):
        """Inicializa la lista de tareas y carga desde un archivo."""
        self.archivo = os.path.join(os.path.dirname(__file__), archivo)
        self.lista_tareas = []
        self.tareas_completadas = []
        self.cargar_tareas()

    def agregar_tarea(self, descripcion, prioridad):
        """Añade una nueva tarea con prioridad."""
        tarea = {"descripcion": descripcion, "prioridad": prioridad}
        self.lista_tareas.append(tarea)
        self.lista_tareas.sort(key=lambda t: {"Alta": 1, "Media": 2, "Baja": 3}[t["prioridad"]])
        self.guardar_tareas()

    def listar_tareas(self):
        """Devuelve la lista de tareas activas."""
        return self.lista_tareas

    def listar_completadas(self):
        """Devuelve la lista de tareas completadas."""
        return self.tareas_completadas

    def eliminar_tarea(self, indice):
        """Elimina una tarea activa basada en su índice."""
        if 0 <= indice < len(self.lista_tareas):
            self.lista_tareas.pop(indice)
            self.guardar_tareas()
        else:
            raise IndexError("Índice de tarea inválido.")

    def editar_tarea(self, indice, nueva_descripcion=None, nueva_prioridad=None):
        """Edita una tarea existente."""
        if 0 <= indice < len(self.lista_tareas):
            if nueva_descripcion:
                self.lista_tareas[indice]["descripcion"] = nueva_descripcion
            if nueva_prioridad:
                self.lista_tareas[indice]["prioridad"] = nueva_prioridad
            self.lista_tareas.sort(key=lambda t: {"Alta": 1, "Media": 2, "Baja": 3}[t["prioridad"]])
            self.guardar_tareas()
        else:
            raise IndexError("Índice de tarea inválido.")

    def marcar_completada(self, indice):
        """Marca una tarea activa como completada."""
        if 0 <= indice < len(self.lista_tareas):
            tarea_completada = self.lista_tareas.pop(indice)
            self.tareas_completadas.append(tarea_completada)
            self.guardar_tareas()
        else:
            raise IndexError("Índice de tarea inválido.")

    def guardar_tareas(self):
        """Guarda las tareas activas y completadas en un archivo JSON."""
        try:
            with open(self.archivo, "w") as f:
                json.dump(
                    {"tareas_activas": self.lista_tareas, "tareas_completadas": self.tareas_completadas}, 
                    f, 
                    indent=4
                )
        except Exception as e:
            print(f"Error al guardar tareas: {e}")

    def cargar_tareas(self):
        """Carga las tareas desde un archivo JSON."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r") as f:
                    data = json.load(f)
                    # Si el archivo contiene una lista, migrar al nuevo formato
                    if isinstance(data, list):
                        self.lista_tareas = data
                        self.tareas_completadas = []
                        self.guardar_tareas()  # Actualizar al nuevo formato
                    else:
                        self.lista_tareas = data.get("tareas_activas", [])
                        self.tareas_completadas = data.get("tareas_completadas", [])
            except json.JSONDecodeError:
                print(f"Error al leer el archivo {self.archivo}, inicializando lista vacía.")
                self.lista_tareas = []
                self.tareas_completadas = []
        else:
            print(f"No se encontró {self.archivo}, inicializando lista vacía.")
            self.lista_tareas = []
            self.tareas_completadas = []
            
    def buscar_tareas(self, palabra_clave):
        """Devuelve una lista de tareas activas que contienen la palabra clave en su descripción."""
        return [tarea for tarea in self.lista_tareas if palabra_clave.lower() in tarea["descripcion"].lower()]
