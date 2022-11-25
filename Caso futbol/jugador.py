from persona import Persona

class Jugador(Persona):
    def __init__(self, rut, nombre, equipo, numeroCamiseta):
        super().__init__(rut, nombre)
        self.__equipo = equipo
        self.__numeroCamiseta = numeroCamiseta
    
    def __str__(self) -> str:
        return f'{super().__str__()} \nEquipo: {self.__equipo} \nNumero camiseta: {self.__numeroCamiseta}'
    
    def setEquipo(self, equipo):
        self.__equipo = equipo
    def setNumeroCamiseta(self, numeroCamiseta):
        self.__numeroCamiseta = numeroCamiseta
    
    def getEquipo(self):
        return self.__equipo
    def getNumeroCamiseta(self):
        return self.__numeroCamiseta
    
    
