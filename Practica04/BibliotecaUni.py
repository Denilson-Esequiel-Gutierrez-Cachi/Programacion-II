# =========================
# CLASE PARTE - PAGINA (COMPOSICIÓN)
# =========================
class Pagina:
    def __init__(self, num, cont):
        self.numeroPagina = num
        self.contenido = cont

    def mostrarPagina(self):
        print(f"Pagina {self.numeroPagina}: {self.contenido}")

# =========================
# CLASE LIBRO (COMPOSICIÓN CON PAGINA)
# =========================
class Libro:
    def __init__(self, titulo, isbn, contenidoPaginas):
        self.titulo = titulo
        self.isbn = isbn
        # COMPOSICIÓN: Las páginas se crean dentro del libro
        self.paginas = [Pagina(i + 1, cont) for i, cont in enumerate(contenidoPaginas)]

    def leer(self):
        print(f"\nLeyendo libro: {self.titulo}")
        for p in self.paginas:
            p.mostrarPagina()

    def __str__(self):
        return f"Libro [titulo='{self.titulo}', isbn='{self.isbn}']"

# =========================
# CLASES (AUTOR Y ESTUDIANTE)
# =========================
class Autor:
    def __init__(self, nom, nac):
        self.nombre = nom
        self.nacionalidad = nac

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"

class Estudiante:
    def __init__(self, cod, nom):
        self.codigo = cod
        self.nombre = nom

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

# =========================
# CLASE PRESTAMO (ASOCIACIÓN)
# =========================
class Prestamo:
    def __init__(self, fechaP, fechaD, estudiante, libro):
        self.fechaPrestamo = fechaP
        self.fechaDevolucion = fechaD
        self.estudiante = estudiante
        self.libro = libro

    def mostrarInfo(self):
        print(f"Prestamo -> Libro: {self.libro.titulo} | Estudiante: {self.estudiante.nombre} | Fecha: {self.fechaPrestamo} al {self.fechaDevolucion}")

# =========================
# CLASE HORARIO Y BIBLIOTECA
# =========================
class Horario:
    def __init__(self, dias, apertura, cierre):
        self.diasApertura = dias
        self.horaApertura = apertura
        self.horaCierre = cierre

    def mostrarHorario(self):
        print(f"Horario: {self.diasApertura} | {self.horaApertura} - {self.horaCierre}")

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  # AGREGACIÓN
        self.autores = [] # AGREGACIÓN
        self.prestamos = [] # COMPOSICIÓN
        self.horario = Horario("Lunes a Viernes", "08:00", "20:00")

    def agregarLibro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro.titulo}")

    def agregarAutor(self, autor):
        self.autores.append(autor)
        print(f"Autor registrado: {autor}")

    def prestarLibro(self, estudiante, libro):
        p = Prestamo("10/05/2026", "17/05/2026", estudiante, libro)
        self.prestamos.append(p)
        print("Prestamo realizado correctamente.")

    def mostrarEstado(self):
        print(f"\n========== {self.nombre.upper()} ==========")
        self.horario.mostrarHorario()
        print("\n--- LIBROS ---")
        for l in self.libros: print(l)
        print("\n--- AUTORES ---")
        for a in self.autores: print(a)
        print("\n--- PRESTAMOS ---")
        for p in self.prestamos: p.mostrarInfo()

    def cerrarBiblioteca(self):
        print(f"\nCerrando biblioteca {self.nombre}")
        self.prestamos.clear()
        print("Todos los prestamos dejaron de existir.")

# =========================
# EJECUCIÓN (MAIN)
# =========================
autor1 = Autor("Gabriel Garcia Marquez", "Colombiano")
autor2 = Autor("Mario Vargas Llosa", "Peruano")

libro1 = Libro("Cien Anos de Soledad", "ISBN-111", ["Inicio", "Nudo", "Desenlace"])
libro2 = Libro("Programacion Python", "ISBN-222", ["Variables", "POO", "Listas"])

est1 = Estudiante("2024001", "Denilson")
est2 = Estudiante("2024002", "Maria")

biblio = Biblioteca("Biblioteca UMSA")
biblio.agregarLibro(libro1)
biblio.agregarLibro(libro2)
biblio.agregarAutor(autor1)
biblio.agregarAutor(autor2)

biblio.prestarLibro(est1, libro1)
biblio.prestarLibro(est2, libro2)

biblio.mostrarEstado()
libro1.leer()
biblio.cerrarBiblioteca()