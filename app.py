# app.py
from funciones import mostrar_libros, agregar_libro, actualizar_libro, eliminar_libro

def menu():
    while True:
        print("\n--- Biblioteca Personal --- ")
        print("1. Mostrar libros")
        print("2. Agregar libro")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            mostrar_libros()
        elif opcion == "2":
            agregar_libro()
        elif opcion == "3":
            actualizar_libro()
        elif opcion == "4":
            eliminar_libro()
        elif opcion == "5":
            print("Saliendo del programa....")
            break
        else:
            print("Opción invalida, intentá de nuevo")

# ejecutamos el menu
if __name__ == "__main__":
    menu()
