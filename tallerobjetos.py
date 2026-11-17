class Libro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[{self.codigo}] {self.titulo} - {self.autor} ({estado})"

class Usuario:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.libros_prestados = []

    def __str__(self):
        return f"{self.nombre} (ID: {self.identificacion})"

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, usuario, libro):
        if libro.disponible:
            libro.disponible = False
            usuario.libros_prestados.append(libro)
            print("Libro prestado a", usuario.nombre)
        else:
            print("El libro no esta disponible")
        
    def devolver_libro(self, usuario, libro):
        if libro in usuario.libros_prestados:
            usuario.libros_prestados.remove(libro)
            libro.disponible = True
            print("Libro devuelto por", usuario.nombre)
        else:
            print("El usuario no tiene ese libro")

    def consultar_disponibles(self):
        print("Libros disponibles:")
        for libro in self.libros:
            if libro.disponible:
                print(libro)

biblio = Biblioteca()

libro1 = Libro("001", "Cien anos de soledad", "Gabriel Garcia Marquez")
libro2 = Libro("002", "El principito", "Antoine de Saint-Exupery")

usuario1 = Usuario("Laura", "1010")
usuario2 = Usuario("Carlos", "2020")

biblio.registrar_libro(libro1)
biblio.registrar_libro(libro2)
biblio.registrar_usuario(usuario1)
biblio.registrar_usuario(usuario2)

biblio.consultar_disponibles()

print("Prestamos:")
biblio.prestar_libro(usuario1, libro1)
biblio.prestar_libro(usuario2, libro1)  # no esta disponible

biblio.consultar_disponibles()

print("Devoluciones:")
biblio.devolver_libro(usuario1, libro1)
biblio.consultar_disponibles()