
class GestorTareas:
    def __init__(self):
        #vamos a inicializar una lista de tareas..
        
        self.lista_tareas = []
        
        
    def agregar_tarea(self, descripcion, prioridad):
        
        tarea = {'descripcion': descripcion , 'prioridad' : prioridad}
        
        self.lista_tareas.append(tarea)
        
        #ordenando la lista por oden de prioridad
        
        self.lista_tareas.sort(key=lambda t: {"Alta": 1, "Media": 2, "Baja": 3}[t["prioridad"]])

        
        
    def listar_tareas(self):
        
        return self.lista_tareas
    
    
    
    
    def eliminar_tarea(self, indice):
        
        if 0 <= indice < len(self.lista_tareas):
            self.lista_tareas.pop(indice)
            
        else:
            raise IndexError("Indice de la tarea no valido")
        
        