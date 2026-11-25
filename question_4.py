class Semaforo:

    def __init__(self, color_inicial = "rojo"):
        self._color = color_inicial

    def siguiente_estado(self):
        if self._color == "rojo":
            self._color = "verde"
        elif self._color == "verde":
            self._color = "amarillo"
        elif self._color == "amarillo":
            self._color = "rojo"

    def puede_avanzar(self):
        return self._color == "verde"


semaforo = Semaforo()

semaforo.siguiente_estado()
print(semaforo.puede_avanzar())   # True

semaforo.siguiente_estado()
print(semaforo.puede_avanzar())   # False