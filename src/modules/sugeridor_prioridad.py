from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import os

# Crear el modelo de sugerencia
class SugeridorDePrioridad:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.modelo = MultinomialNB()
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
        ]
        prioridades = ["Media", "Baja", "Alta", "Alta", "Alta", "Media", "Alta", "Baja"]

        X = self.vectorizer.fit_transform(tareas)
        self.modelo.fit(X, prioridades)

    def sugerir_prioridad(self, descripcion):
        X = self.vectorizer.transform([descripcion])
        return self.modelo.predict(X)[0]
    
    
sugeridor = SugeridorDePrioridad()