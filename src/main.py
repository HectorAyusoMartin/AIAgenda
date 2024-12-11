from modules.gestor_tareas import GestorTareas
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

def main():
    print(Fore.BLUE + "Bienvenido a AI Agenda\n")

    gestor_tareas = GestorTareas()

    while True:
        print(Style.BRIGHT + Fore.CYAN + "\nOpciones:")
        print(Fore.YELLOW + "1. Agregar tarea")
        print(Fore.YELLOW + "2. Ver tareas")
        print(Fore.YELLOW + "3. Eliminar tarea")
        print(Fore.YELLOW + "4. Salir")

        opcion = input(Fore.CYAN + "Elige una opción: ").strip()

        if opcion == "1":
            tarea = input(Fore.GREEN + "Escribe la nueva tarea: ").strip()
            gestor_tareas.agregar_tarea(tarea)
            print(Fore.GREEN + "Tarea añadida correctamente.")

        elif opcion == "2":
            tareas = gestor_tareas.listar_tareas()
            print(Style.BRIGHT + Fore.BLUE + "\nTus tareas:")
            if tareas:
                for i, tarea in enumerate(tareas, 1):
                    print(f"{Fore.YELLOW}{i}. {Fore.WHITE}{tarea}")
            else:
                print(Fore.RED + "No tienes tareas registradas.")

        elif opcion == "3":
            tareas = gestor_tareas.listar_tareas()
            if not tareas:
                print(Fore.RED + "No hay tareas para eliminar.")
                continue

            print(Style.BRIGHT + Fore.BLUE + "\nTareas disponibles:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{Fore.YELLOW}{i}. {Fore.WHITE}{tarea}")

            try:
                indice = int(input(Fore.CYAN + "Elige el número de la tarea a eliminar: ").strip())
                gestor_tareas.eliminar_tarea(indice - 1)  # Restar 1 porque enumeramos desde 1
                print(Fore.GREEN + "Tarea eliminada correctamente.")
            except (ValueError, IndexError):
                print(Fore.RED + "Por favor, introduce un número válido dentro del rango.")

        elif opcion == "4":
            print(Fore.GREEN + "¡Hasta luego!")
            break

        else:
            print(Fore.RED + "Por favor, elige una opción válida (1-4).")

if __name__ == "__main__":
    main()
