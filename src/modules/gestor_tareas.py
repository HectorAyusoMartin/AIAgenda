
class GestorTareas:
    def __init__(self):
        #vamos a inicializar una lista de tareas..
        
        self.lista_tareas = []
        
        
    def agregar_tarea(self, tarea):
        
        self.lista_tareas.append(tarea)
        
        
    def listar_tareas(self):
        
        return self.lista_tareas
    
    def eliminar_tarea(self, indice):
        
        if 0 <= indice < len(self.lista_tareas):
            self.lista_tareas.pop(indice)
            
        else:
            raise IndexError("Indice de la tarea no valido")
        
        