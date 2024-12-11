import json
import os




class GestorTareas:
    def __init__(self, archivo ='tareas.json'):
             
        #iniciamos la lista de tareas de carga desde un archivo
        
        # Asegura que el archivo JSON esté en la misma carpeta que este script
        self.archivo = os.path.join(os.path.dirname(__file__), archivo)
        
        
        self.lista_tareas = []
        
        
        self.cargar_tareas()
        
        
        
    def agregar_tarea(self, descripcion, prioridad):
        
        tarea = {'descripcion': descripcion , 'prioridad' : prioridad}
        
        self.lista_tareas.append(tarea)
        
        #ordenando la lista por oden de prioridad
        
        self.lista_tareas.sort(key=lambda t: {"Alta": 1, "Media": 2, "Baja": 3}[t["prioridad"]])

        self.guardar_tareas()
        
    def listar_tareas(self):
        
        return self.lista_tareas
    
    
    
    
    def eliminar_tarea(self, indice):
        
        
        if 0 <= indice < len(self.lista_tareas):
            self.lista_tareas.pop(indice)
            self.guardar_tareas()
            
        else:
            raise IndexError("Indice de la tarea no valido")
        


    def cargar_tareas(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as f:
                    self.lista_tareas = json.load(f)
                    print(f'Tareas cargadas desde {self.archivo}')
            except FileNotFoundError:
                self.lista_tareas = [] #si no existe, inicia lista vacia
            except json.JSONDecodeError:
                print(f'Error al leer el archivo {self.archivo}, inicializando lista vacia')
                self.lista_tareas = []
        else:
            print(f'No se encontro {self.archivo},inicializando lista vacia')
            self.lista_tareas = []
                
            
            
            
    
    
    def guardar_tareas(self):
        
        try:
            
            with open(self.archivo, 'w') as f:
                json.dump(self.lista_tareas ,f, indent=4)
            print(f'Tareas guardadas en {self.archivo}')
        
        except Exception as e:
            print(f'Error al guardar las tareas: {e}')
        
    
