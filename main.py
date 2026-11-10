from modelo import Biblioteca, Libro, Usuario, VERDE, ROJO

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n=======================================")
        print("    SISTEMA DE GESTIÓN DE BIBLIOTECA   ")
        print("=======================================")
        print("1. Registrar libro")
        print("2. Registrar usuario")
        print("3. Consultar libros")
        print("4. Realizar préstamo")
        print("5. Registrar devolución")
        print("6. Consultar estado de un libro")
        print("7. Salir")
        
        opcion = input("\nSeleccione una opción (1-7): ")

        if opcion == "1":
            codigo = input("Ingrese el código del libro: ")
            titulo = input("Ingrese el título: ")
            autor = input("Ingrese el autor: ")
            biblioteca.registrar_libro(Libro(codigo, titulo, autor))
            
        elif opcion == "2":
            identificacion = input("Ingrese la identificación del usuario: ")
            nombre = input("Ingrese el nombre completo: ")
            correo = input("Ingrese el correo electrónico: ")
            biblioteca.registrar_usuario(Usuario(identificacion, nombre, correo))
            
        elif opcion == "3":
            biblioteca.consultar_libros()
            
        elif opcion == "4":
            codigo = input("Ingrese el código del libro a prestar: ")
            id_usu = input("Ingrese la identificación del usuario: ")
            biblioteca.realizar_prestamo(codigo, id_usu)
            
        elif opcion == "5":
            codigo = input("Ingrese el código del libro a devolver: ")
            biblioteca.registrar_devolucion(codigo)
            
        elif opcion == "6":
            codigo = input("Ingrese el código del libro a consultar: ")
            biblioteca.consultar_estado_libro(codigo)
            
        elif opcion == "7":
            print(f"\n{VERDE}¡Gracias por utilizar el sistema de la biblioteca! Saliendo...{RESET}")
            break
        else:
            print(f"\n{ROJO}Opción inválida. Por favor, ingrese un número del 1 al 7.{RESET}")

if __name__ == "__main__":
    menu()