from datetime import datetime

# Códigos ANSI para colores en consola
ROJO = "\033[91m"
AMARILLO = "\033[93m"
VERDE = "\033[92m"
RESET = "\033[0m"

class Libro:
    def __init__(self, codigo, titulo, autor):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True

    # Getters y Setters (Encapsulamiento)
    def get_codigo(self):
        return self.__codigo

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def is_disponible(self):
        return self.__disponible

    def set_disponible(self, disponible):
        self.__disponible = disponible

    def __str__(self):
        estado = f"{VERDE}Disponible{RESET}" if self.__disponible else f"{AMARILLO}Prestado{RESET}"
        return f"Código: {self.__codigo} | Título: {self.__titulo} | Autor: {self.__autor} | Estado: {estado}"


class Usuario:
    def __init__(self, identificacion, nombre, correo):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo = correo

    # Getters
    def get_identificacion(self):
        return self.__identificacion

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def __str__(self):
        return f"ID: {self.__identificacion} | Nombre: {self.__nombre} | Correo: {self.__correo}"


class Prestamo:
    def __init__(self, libro, usuario):
        self.__libro = libro
        self.__usuario = usuario
        self.__fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fecha (Color Rojo)
        self.__estado = "Activo"  # Estado (Color Amarillo)

    def get_libro(self):
        return self.__libro

    def get_usuario(self):
        return self.__usuario

    def get_fecha(self):
        return self.__fecha

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def __str__(self):
        fecha_str = f"{ROJO}{self.__fecha}{RESET}"
        estado_str = f"{AMARILLO}{self.__estado}{RESET}" if self.__estado == "Activo" else f"{VERDE}{self.__estado}{RESET}"
        return f"Libro: {self.__libro.get_titulo()} | Usuario: {self.__usuario.get_nombre()} | Fecha: {fecha_str} | Estado: {estado_str}"


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro):
        self.libros.append(libro)
        print(f"\n{VERDE}¡Libro registrado exitosamente!{RESET}")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"\n{VERDE}¡Usuario registrado exitosamente!{RESET}")

    def consultar_libros(self):
        if not self.libros:
            print(f"\n{AMARILLO}No hay libros registrados en el sistema.{RESET}")
            return
        print("\n--- LISTA DE LIBROS REGISTRADOS ---")
        for libro in self.libros:
            print(libro)

    def buscar_libro(self, codigo):
        for libro in self.libros:
            if libro.get_codigo() == codigo:
                return libro
        return None

    def buscar_usuario(self, identificacion):
        for usuario in self.usuarios:
            if usuario.get_identificacion() == identificacion:
                return usuario
        return None

    def realizar_prestamo(self, codigo_libro, id_usuario):
        libro = self.buscar_libro(codigo_libro)
        usuario = self.buscar_usuario(id_usuario)

        if not libro:
            print(f"\n{ROJO}Error: El libro con código '{codigo_libro}' no existe.{RESET}")
            return
        if not usuario:
            print(f"\n{ROJO}Error: El usuario con identificación '{id_usuario}' no existe.{RESET}")
            return
        if not libro.is_disponible():
            print(f"\n{AMARILLO}Aviso: El libro '{libro.get_titulo()}' ya se encuentra prestado.{RESET}")
            return

        libro.set_disponible(False)
        prestamo = Prestamo(libro, usuario)
        self.prestamos.append(prestamo)
        print(f"\n{VERDE}¡Préstamo registrado con éxito!{RESET}")

    def registrar_devolucion(self, codigo_libro):
        libro = self.buscar_libro(codigo_libro)
        if not libro:
            print(f"\n{ROJO}Error: El libro no existe.{RESET}")
            return
        if libro.is_disponible():
            print(f"\n{AMARILLO}Aviso: El libro ya se encontraba disponible.{RESET}")
            return

        for prestamo in self.prestamos:
            if prestamo.get_libro().get_codigo() == codigo_libro and prestamo.get_estado() == "Activo":
                prestamo.set_estado("Finalizado")
                libro.set_disponible(True)
                print(f"\n{VERDE}¡Devolución registrada correctamente!{RESET}")
                return

        print(f"\n{ROJO}No se encontró un préstamo activo para este libro.{RESET}")

    def consultar_estado_libro(self, codigo_libro):
        libro = self.buscar_libro(codigo_libro)
        if not libro:
            print(f"\n{ROJO}Error: El libro no existe.{RESET}")
            return
        print(f"\n--- ESTADO DEL LIBRO ---")
        print(libro)