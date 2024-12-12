from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Crear el modelo de sugerencia
class SugeridorDePrioridad:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.modelo = RandomForestClassifier()
        self.entrenar_modelo()

    def entrenar_modelo(self):
        tareas = [
            "Enviar un informe",
            "Revisar correos",
            "Pagar facturas",
            "Llamar al jefe",
            "Preparar presentación",
            "Limpiar la casa",
            "Estudiar para el examen",
            "Comprar alimentos",
            "Hacer ejercicio",
            "Visitar al médico",
            "Ordenar documentos",
            "Planificar vacaciones",
            "Cuidar a las mascotas",
            "Cocinar la cena",
        ]
        prioridades = [
            "Media", "Baja", "Alta", "Alta", "Alta", "Media", "Alta", "Baja", "Media",
            "Alta", "Media", "Baja", "Media", "Media"
        ]
        
        tareas = [
            "Enviar reporte urgente al jefe",
            "Comprar leche y pan para la cena",
            "Limpiar el baño y la cocina",
            "Estudiar teoría de programación",
            "Revisar presupuesto anual del equipo",
            "Planificar evento del próximo mes",
            "Hacer ejercicio físico en el gimnasio",
            "Cuidar al gato enfermo durante el día",
            "Actualizar el software del ordenador",
            "Reservar entradas para el cine",
            "Llamar al proveedor por contrato",
            "Leer el nuevo informe semanal",
            "Pagar la cuota del gimnasio mensual",
            "Revisar correos atrasados en la bandeja",
            "Actualizar perfil profesional en LinkedIn",
            "Comprar el regalo para el cumpleaños",
            "Escribir un artículo para el blog",
            "Organizar documentos de impuestos",
            "Terminar la presentación de ventas",
            "Preparar la reunión de equipo",
            "Ir al médico por chequeo anual",
            "Buscar ideas para vacaciones de verano",
            "Organizar la despensa de alimentos",
            "Hacer una lista de compras de supermercado",
            "Revisar contratos laborales pendientes",
            "Preparar las maletas para el viaje",
            "Responder mensajes importantes en WhatsApp",
            "Programar la limpieza del coche",
            "Hacer llamada de soporte técnico urgente",
            "Solicitar permiso de vacaciones",
            "Renovar la póliza del seguro de coche",
            "Limpiar las ventanas de la casa",
            "Investigar nuevos libros para leer",
            "Configurar la red de internet en casa",
            "Revisar tareas escolares de los niños",
            "Solicitar cotización de reparaciones",
            "Enviar felicitaciones a un colega",
            "Hacer pedido online de supermercado",
            "Visitar la casa de los abuelos",
            "Revisar pagos pendientes de facturas",
            "Revisar agenda semanal de trabajo",
            "Pedir cita para el dentista urgente",
            "Estudiar para el examen de fin de mes",
            "Reparar la fuga de agua en el baño",
            "Cargar el teléfono antes de salir",
            "Llamar a un amigo por su cumpleaños",
            "Solicitar renovación de pasaporte",
            "Guardar copia de seguridad de archivos",
            "Planificar un picnic familiar el domingo",
            "Enviar la propuesta al cliente antes del lunes",
            "Comprar repuestos para el coche",
            "Hacer revisión médica para los niños",
            "Pedir pizza para la cena de esta noche",
            "Revisar ofertas de trabajo en LinkedIn",
            "Preparar una lista de preguntas para la reunión",
            "Hacer mantenimiento a la bicicleta",
            "Comprar lámparas nuevas para la sala",
            "Hacer seguimiento al cliente importante",
            "Planificar presupuesto mensual personal",
            "Configurar el nuevo televisor en el salón",
            "Limpiar la nevera y el congelador",
            "Terminar de leer el libro de novela",
            "Preparar la ropa para la reunión formal",
            "Guardar fotos de las vacaciones en la nube",
            "Programar clases de yoga para la semana",
            "Hacer limpieza profunda en la cocina",
            "Configurar el móvil con nuevas aplicaciones",
            "Asistir a la boda de un amigo el sábado",
            "Recoger los resultados médicos del laboratorio",
            "Asegurarse de cerrar bien las puertas por la noche",
            "Revisar los reportes financieros trimestrales",
            "Asistir a la reunión de padres en el colegio",
            "Planificar el menú semanal para toda la familia",
            "Hacer una presentación para el nuevo proyecto",
            "Pedir cita para el oculista por molestias",
            "Leer un artículo interesante sobre tecnología",
            "Ir a la tienda por herramientas específicas",
            "Escribir el borrador para el proyecto del equipo",
            "Revisar actualizaciones de software importantes",
            "Confirmar asistencia al evento del domingo",
            "Registrar las compras en el presupuesto personal",
            "Actualizar la contraseña del correo electrónico",
            "Comprar juguetes nuevos para los niños",
            "Preparar el desayuno para el domingo temprano",
            "Enviar mensajes de agradecimiento a clientes",
            "Solicitar reunión con el supervisor esta semana",
            "Limpiar la terraza y ordenar los muebles",
            "Revisar el manual de instrucciones del coche",
            "Asistir a clases de inglés esta semana",
            "Llamar al electricista para arreglos pendientes",
            "Inscribirse en un curso de desarrollo web",
            "Hacer una lista de objetivos para el mes",
            "Enviar un correo electrónico a Recursos Humanos",
            "Hacer videollamada con la familia lejana",
            "Pintar la habitación de los niños de azul",
            "Buscar tutoriales de cocina en internet",
            "Enviar el informe final al cliente a tiempo",
            "Ir al supermercado por artículos de limpieza",
            "Buscar recetas nuevas para la cena",
            "Revisar pendientes de pagos de servicios",
            "Asistir al seminario online el miércoles",
            "Hacer una reunión de seguimiento con el equipo",
            "Realizar ejercicio diario durante 30 minutos",
            "Configurar nueva impresora en la oficina",
            "Llamar al banco por una consulta urgente",
            "Enviar una tarjeta de felicitación personalizada",
            "Asegurarse de revisar el buzón de correos",
            "Revisar si las plantas necesitan agua",
            "Cocinar una receta especial para la familia",
            "Terminar la edición del video promocional",
        ]

        prioridades = [
            "Alta", "Baja", "Media", "Alta", "Alta", "Media", "Alta", "Media", "Baja", "Baja",
            "Alta", "Alta", "Media", "Baja", "Baja", "Alta", "Media", "Alta", "Alta", "Alta",
            "Alta", "Media", "Baja", "Media", "Alta", "Media", "Baja", "Alta", "Alta", "Media",
            "Baja", "Media", "Media", "Alta", "Alta", "Media", "Media", "Alta", "Alta", "Alta",
            "Alta", "Alta", "Baja", "Media", "Media", "Media", "Media", "Alta", "Alta", "Baja",
            "Media", "Baja", "Media", "Baja", "Media", "Media", "Media", "Media", "Alta", "Alta",
            "Media", "Media", "Alta", "Alta", "Baja", "Media", "Baja", "Media", "Media", "Media",
            "Media", "Baja", "Alta", "Alta", "Media", "Baja", "Media", "Baja", "Alta", "Media",
            "Alta", "Alta", "Media", "Media", "Media", "Media", "Alta", "Media", "Alta", "Media",
            "Alta", "Alta", "Baja", "Media", "Baja", "Media", "Media", "Media", "Baja", "Media",
            "Baja", "Alta", "Baja", "Media", "Media", "Media", "Alta", "Alta", "Media", "Media",
            
        ]


        # Dividir el conjunto de datos para entrenamiento y prueba
        X = self.vectorizer.fit_transform(tareas)
        X_train, X_test, y_train, y_test = train_test_split(X, prioridades, test_size=0.2, random_state=42)

        # Entrenar el modelo
        self.modelo.fit(X_train, y_train)

        

    def sugerir_prioridad(self, descripcion):
        X = self.vectorizer.transform([descripcion])
        return self.modelo.predict(X)[0]

# Instanciar el sugeridor de prioridad
sugeridor = SugeridorDePrioridad()
