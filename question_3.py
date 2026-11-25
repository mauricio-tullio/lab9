class Libro:

    def __init__(self, titulo, autor, paginas, leidas = 0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self._progreso = leidas

    def leer(self, cantidad):
        if cantidad > 0 and self._progreso + cantidad <= self.paginas:
            self._progreso += cantidad
        else:
            print("Cantidad inválida")

    def progreso(self):
        return round(self._progreso / self.paginas * 100)

    def resumen(self):
        return f"{self.titulo} - {self.autor} ({self.progreso()}%): {self._progreso} páginas leídas de {self.paginas}"


l1 = Libro("Pachinko", "Min Jin Lee", 496, 193)
l2 = Libro("El Conde de Monte Cristo", "Alexander Dumas", 1276)

l1.leer(200)
print(l1._progreso)    # 393

print(l1.progreso())   # 79

print(l1.resumen())    # Pachinko - Min Jin Lee (79%): 393 páginas leídas de 496
print(l2.resumen())    # El Conde de Monte Cristo - Alexander Dumas (0%): 0 páginas leídas de 1276