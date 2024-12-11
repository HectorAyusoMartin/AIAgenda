#punto de entrada


from modules.gestor_tareas import GestorTareas

def main():
    print("Bienvenido a AI Agenda")

    gestor_tareas = GestorTareas()

    while True:
        print("\nOpciones:")
        print("1. Añadir tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

        
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            tarea = input("Escribe la nueva tarea: ").strip()
            gestor_tareas.agregar_tarea(tarea)
            print("Tarea añadida.")

        elif opcion == "2":
            tareas = gestor_tareas.listar_tareas()
            if tareas:
                print("Tus tareas:")
                for i, tarea in enumerate(tareas, 1):  # Enumerar desde 1
                    print(f"{i}. {tarea}")
            else:
                print("No tienes tareas.")

        elif opcion == "3":
            tareas = gestor_tareas.listar_tareas()
            if not tareas:
                print("No hay tareas para eliminar.")
                continue

            try:
                indice = int(input("Elige el número de la tarea a eliminar: ").strip())
                gestor_tareas.eliminar_tarea(indice - 1)  # Restar 1 porque enumeramos desde 1
                print("Tarea eliminada.")
            except (ValueError, IndexError):
                print("Por favor, introduce un número válido dentro del rango.")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Por favor, elige una opción válida (1-4).")

if __name__ == "__main__":
    main()
