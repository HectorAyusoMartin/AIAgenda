from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

class ClasificadorPrioridades:
    def __init__(self):
       
        self.data = [
            
            ("Completar informe de ventas urgente", "Alta"),
            ("Resolver problemas críticos del servidor", "Alta"),
            ("Preparar presentación para la junta directiva", "Alta"),
            ("Terminar el proyecto antes de la fecha límite", "Alta"),
            ("Responder a correos urgentes del cliente", "Alta"),
            ("Gestionar crisis en la producción", "Alta"),
            ("Planificar estrategia para el lanzamiento del producto", "Alta"),
            ("Atender llamada importante con el proveedor", "Alta"),
            ("Analizar reportes financieros trimestrales", "Alta"),
            ("Coordinar equipo para la reunión de emergencia", "Alta"),

          
            ("Revisar los correos pendientes del día", "Media"),
            ("Actualizar la lista de contactos del equipo", "Media"),
            ("Planificar actividades para la próxima semana", "Media"),
            ("Organizar la reunión semanal del equipo", "Media"),
            ("Responder correos de seguimiento de clientes", "Media"),
            ("Actualizar software de las estaciones de trabajo", "Media"),
            ("Revisar informes de desempeño mensual", "Media"),
            ("Preparar reportes para la próxima reunión", "Media"),
            ("Llamar a clientes para confirmar pedidos", "Media"),
            ("Revisar documentación interna para actualizaciones", "Media"),

            
            ("Organizar documentos antiguos", "Baja"),
            ("Limpiar el escritorio y la oficina", "Baja"),
            ("Hacer copias de seguridad regulares", "Baja"),
            ("Archivar contratos vencidos", "Baja"),
            ("Ordenar carpetas en el sistema de archivos", "Baja"),
            ("Pedir material de oficina para el próximo mes", "Baja"),
            ("Eliminar correos electrónicos innecesarios", "Baja"),
            ("Revisar la lista de tareas pendientes", "Baja"),
            ("Actualizar plantillas de correos corporativos", "Baja"),
            ("Planificar limpieza general de la oficina", "Baja"),

            
            ("Solucionar problemas con proveedores importantes", "Alta"),
            ("Enviar actualizaciones a los clientes principales", "Media"),
            ("Actualizar manuales de procedimientos internos", "Baja"),
            ("Realizar encuestas de satisfacción de clientes", "Media"),
            ("Configurar nuevas estaciones de trabajo", "Alta"),
            ("Revisar y actualizar políticas internas", "Media"),
            ("Preparar el presupuesto para el siguiente trimestre", "Alta"),
            ("Enviar recordatorios para la reunión semanal", "Media"),
            ("Hacer mantenimiento del equipo de oficina", "Baja"),
            ("Organizar actividades del día del empleado", "Baja"),
            ("Reparar la fuga de agua en el baño", "Alta"),
            ("Resolver el problema eléctrico en la cocina", "Alta"),
            ("Limpiar la casa antes de la llegada de invitados", "Alta"),
            ("Preparar comida para la cena familiar", "Alta"),
            ("Comprar medicinas urgentes en la farmacia", "Alta"),
            ("Descongelar el congelador para evitar daños", "Alta"),
            ("Lavar y planchar ropa para un evento importante", "Alta"),
            ("Acomodar el cuarto de los niños antes de la inspección", "Alta"),
            ("Comprar ingredientes frescos para la comida", "Alta"),
            ("Aspirar alfombras que llevan meses sin limpiar", "Alta"),

           
            ("Ordenar los armarios de la cocina", "Media"),
            ("Planificar el menú de la semana", "Media"),
            ("Revisar los pagos pendientes de servicios", "Media"),
            ("Llamar al técnico para el mantenimiento del aire acondicionado", "Media"),
            ("Poner gasolina al coche para la semana", "Media"),
            ("Cambiar las sábanas y fundas de las camas", "Media"),
            ("Revisar las fechas de vencimiento en la despensa", "Media"),
            ("Sacar a pasear al perro durante el día", "Media"),
            ("Revisar las luces fundidas de la casa", "Media"),
            ("Regar las plantas del jardín", "Media"),

          
            ("Limpiar los espejos del baño", "Baja"),
            ("Ordenar los libros en la estantería", "Baja"),
            ("Sacar la basura de reciclaje", "Baja"),
            ("Lavar el coche en casa", "Baja"),
            ("Doblar la ropa limpia del armario", "Baja"),
            ("Organizar las fotos antiguas en álbumes", "Baja"),
            ("Limpiar los electrodomésticos pequeños", "Baja"),
            ("Vaciar el buzón de correos", "Baja"),
            ("Lavar los juguetes del perro", "Baja"),
            ("Arreglar cajones que no cierran bien", "Baja"),
        ]
        self.modelo = None
        self.vectorizador = CountVectorizer()

    def entrenar_modelo(self):
       
        textos, etiquetas = zip(*self.data)

        
        X = self.vectorizador.fit_transform(textos)
        
        self.modelo = MultinomialNB()
        self.modelo.fit(X, etiquetas)

        with open("clasificador_model.pkl", "wb") as f:
            pickle.dump((self.vectorizador, self.modelo), f)

    def predecir_prioridad(self, descripcion):
        
        if not self.modelo:
            with open("clasificador_model.pkl", "rb") as f:
                self.vectorizador, self.modelo = pickle.load(f)
        
        
        X = self.vectorizador.transform([descripcion])
        return self.modelo.predict(X)[0]
