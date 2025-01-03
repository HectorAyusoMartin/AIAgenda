from modules.gestor_tareas import GestorTareas
from modules.clasificador_prioridades import ClasificadorPrioridades
from modules.sugeridor_prioridad import SugeridorDePrioridad




from colorama import Fore, Style, init







init(autoreset=True)

def main():
    print(Fore.BLUE + "Bienvenido a AI Agenda\n")

    gestor_tareas = GestorTareas()
    
    clasificador = ClasificadorPrioridades()
    clasificador.entrenar_modelo()
    sugeridor = SugeridorDePrioridad()
    
    
    

    while True:
        print(Style.BRIGHT + Fore.CYAN + "\nOpciones:")
        print(Fore.YELLOW + "1. Agregar tarea")
        print(Fore.YELLOW + "2. Ver tareas activas")
        print(Fore.YELLOW + "3. Ver tareas completadas")
        print(Fore.YELLOW + "4. Eliminar tarea")
        print(Fore.YELLOW + "5. Filtrar tareas por prioridad")
        print(Fore.YELLOW + "6. Editar una tarea")
        print(Fore.YELLOW + "7. Marcar una tarea como completada")
        print(Fore.YELLOW + "8. Salir")
        print(Fore.YELLOW + "9. Predecir prioridad de una tarea")
        print(Fore.YELLOW + "10. Busqueda de Tarea por palabra clave")
        

            

        opcion = input(Fore.CYAN + "Elige una opción: ").strip()
        
        if opcion == "1":
            descripcion = input(Fore.GREEN + "Escribe la nueva tarea: ").strip()
            prioridad_sugerida = sugeridor.sugerir_prioridad(descripcion)
            print(Fore.YELLOW + f"Prioridad sugerida: {prioridad_sugerida}")
            prioridad = input(Fore.GREEN + "Escribe la prioridad (Alta, Media, Baja) o presiona Enter para usar la sugerida: ").strip().capitalize()
            if not prioridad:
                prioridad = prioridad_sugerida
            if prioridad not in ["Alta", "Media", "Baja"]:
                print(Fore.RED + "Prioridad inválida. Usa 'Alta', 'Media' o 'Baja'.")
                continue
            gestor_tareas.agregar_tarea(descripcion, prioridad)
            print(Fore.GREEN + "Tarea añadida correctamente.")
            print(Fore.GREEN + "Tarea añadida correctamente.")

            print("Función de sugerencia de prioridad añadida correctamente al agregar tarea.")
        
    

        elif opcion == "2":
            tareas = gestor_tareas.listar_tareas()
            print(Style.BRIGHT + Fore.BLUE + "\nTareas activas:")
            if tareas:
                for i, tarea in enumerate(tareas, 1):
                    print(f"{Fore.YELLOW}{i}. {Fore.WHITE}{tarea['descripcion']} ({tarea['prioridad']})")
            else:
                print(Fore.RED + "No tienes tareas activas.")

        elif opcion == "3":
            completadas = gestor_tareas.listar_completadas()
            print(Style.BRIGHT + Fore.BLUE + "\nTareas completadas:")
            if completadas:
                for i, tarea in enumerate(completadas, 1):
                    print(f"{Fore.YELLOW}{i}. {Fore.WHITE}{tarea['descripcion']} ({tarea['prioridad']})")
            else:
                print(Fore.RED + "No tienes tareas completadas.")

        elif opcion == "4":
            tareas = gestor_tareas.listar_tareas()
            if not tareas:
                print(Fore.RED + "No hay tareas para eliminar.")
                continue

            print(Style.BRIGHT + Fore.BLUE + "\nTareas disponibles:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{Fore.YELLOW}{i}. {Fore.WHITE}{tarea['descripcion']} ({tarea['prioridad']})")

            try:
                indice = int(input(Fore.CYAN + "Elige el número de la tarea a eliminar: ").strip())
                gestor_tareas.eliminar_tarea(indice - 1)
                print(Fore.GREEN + "Tarea eliminada correctamente.")
            except (ValueError, IndexError):
                print(Fore.RED + "Por favor, introduce un número válido dentro del rango.")

        elif opcion == "5":
            prioridad = input(Fore.GREEN + "Escribe la prioridad a filtrar (Alta, Media, Baja): ").strip().capitalize()
            if prioridad not in ["Alta", "Media", "Baja"]:
                print(Fore.RED + "Prioridad inválida. Usa 'Alta', 'Media' o 'Baja'.")
                continue

            tareas_filtradas = [t for t in gestor_tareas.listar_tareas() if t["prioridad"] == prioridad]
            print(Style.BRIGHT + Fore.BLUE + f"\nTareas con prioridad {prioridad}:")
            if tareas_filtradas:
                for i, tarea in enumerate(tareas_filtradas, 1):
                    print(f"{Fore.YELLOW}{i}. {Fore.WHITE}{tarea['descripcion']} ({tarea['prioridad']})")
            else:
                print(Fore.RED + f"No hay tareas con prioridad {prioridad}.")

        elif opcion == "6":
            tareas = gestor_tareas.listar_tareas()
            if not tareas:
                print(Fore.RED + "No hay tareas para editar.")
                continue

            print(Style.BRIGHT + Fore.BLUE + "\nTareas disponibles:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{Fore.YELLOW}{i}. {Fore.WHITE}{tarea['descripcion']} ({tarea['prioridad']})")

            try:
                indice = int(input(Fore.CYAN + "Elige el número de la tarea a editar: ").strip())
                if not (1 <= indice <= len(tareas)):
                    print(Fore.RED + "Número fuera de rango.")
                    continue

                nueva_descripcion = input(Fore.GREEN + "Escribe la nueva descripción (o presiona Enter para no cambiar): ").strip()
                nueva_prioridad = input(Fore.GREEN + "Escribe la nueva prioridad (Alta, Media, Baja) o presiona Enter para no cambiar: ").strip().capitalize()

                if nueva_prioridad and nueva_prioridad not in ["Alta", "Media", "Baja"]:
                    print(Fore.RED + "Prioridad inválida. Usa 'Alta', 'Media' o 'Baja'.")
                    continue

                gestor_tareas.editar_tarea(indice - 1, nueva_descripcion, nueva_prioridad)
                print(Fore.GREEN + "Tarea editada correctamente.")
            except ValueError:
                print(Fore.RED + "Entrada inválida. Introduce un número.")

        elif opcion == "7":
            tareas = gestor_tareas.listar_tareas()
            if not tareas:
                print(Fore.RED + "No hay tareas para completar.")
                continue

            print(Style.BRIGHT + Fore.BLUE + "\nTareas disponibles:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{Fore.YELLOW}{i}. {Fore.WHITE}{tarea['descripcion']} ({tarea['prioridad']})")

            try:
                indice = int(input(Fore.CYAN + "Elige el número de la tarea a completar: ").strip())
                gestor_tareas.marcar_completada(indice - 1)
                print(Fore.GREEN + "Tarea marcada como completada.")
            except (ValueError, IndexError):
                print(Fore.RED + "Entrada inválida o índice fuera de rango.")

        elif opcion == "8":
            print(Fore.GREEN + "¡Hasta luego!")
            break
        
        elif opcion == "9":
            
            descripcion = input(Fore.GREEN + "Escribe la descripción de la tarea: ").strip()
            prioridad = clasificador.predecir_prioridad(descripcion)
            print(Fore.MAGENTA + f"La prioridad sugerida es: {prioridad}")
        
        elif opcion == '10':
            
            palabra_clave = input(Fore.GREEN + "Introduce una palabra clave para buscar: ").strip()
            resultados = gestor_tareas.buscar_tareas(palabra_clave)
                
            if resultados:
                    
                print(Fore.BLUE + f"Tareas que coinciden con '{palabra_clave}':")
                
                
                for i, tarea in enumerate(resultados, 1):
                    print(f"{Fore.YELLOW}{i}. {Fore.WHITE}{tarea['descripcion']} ({tarea['prioridad']})")
                    
            else:
                print(Fore.RED + f"No se encontraron tareas que contengan '{palabra_clave}'.")
        


        else:
            print(Fore.RED + "Por favor, elige una opción válida (1-10).")

if __name__ == "__main__":
    main()
