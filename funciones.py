# Lista para almacenar los libros
biblioteca = []

#mostrar todos los libros
def mostrar_libros():
    if not biblioteca:
        print("No hay libros guardados.")
    else:
        print("Libros en la biblioteca: ")
        for idx, libro in enumerate(biblioteca, start=1): #enumera los libros guardados para cceder mas facil a ellos
            print(f"{idx}. Título: {libro['titulo']}, Autor: {libro['autor']}, Estrellas: {libro['estrellas']}, "
                  f"Descripción: {libro['descripcion']}")

# agregar un libro
def agregar_libro():
    while True: #se ejecuta siempre
        titulo = input("Ingresa el título del libro: ")
        autor = input("Ingresa el autor del libro: ")
        estrellas = input("Cuántas estrellas le das? del 1 al 5: ")
        descripcion = input("Ingresa una reseña: ")

        libro = {
            "titulo": titulo,
            "autor": autor,
            "estrellas": estrellas,
            "descripcion": descripcion
        }
        
        biblioteca.append(libro)
        print("Libro agregado!")

        # Pregunta si desea agregar otro libro
        agregar_otro = input("¿Queres agregar otro libro? (s/n): ").strip().lower() #compruebo y formateo a lower 
        if agregar_otro != 's':
            break

#actualizar un libro
def actualizar_libro():
    mostrar_libros()
    index = int(input("Ingresa el número del libro a actualizar: ")) - 1
    if 0 <= index < len(biblioteca):
        titulo = input("Ingresa el nuevo titulo o dejalo en blanco para mantener el actual : ")
        autor = input("Ingresa el nuevo autor : ")
        estrellas = input("Actualiza la cantidad de estrellas ")
        descripcion = input("Ingresa una nueva reseña: ")

        # Actualiza los campos solo si hay datos nuevos
        if titulo:
            biblioteca[index]['titulo'] = titulo
        if autor:
            biblioteca[index]['autor'] = autor
        if estrellas:
            biblioteca[index]['estrellas'] = estrellas
        if descripcion:
            biblioteca[index]['descripcion'] = descripcion

        print("Libro actualizado exitosamente.")
    else:
        print("Número de libro inválido.")

# eliminar un libro
def eliminar_libro():
    mostrar_libros()
    index = int(input("Ingresa el número del libro a eliminar: ")) - 1
    if 0 <= index < len(biblioteca):
        biblioteca.pop(index)
        print("Libro eliminado.")
    else:
        print("Número de libro no existe.")
