from jugador import Jugador
from arbitro import Arbitro

class Partido:
    def __init__(self, numPartido, estadio, referi):
        self.__numPartido = numPartido
        self.__estadio = estadio
        self.__referi = referi
        self.__listEquipo1 = []
        self.__listEquipo2 = []
    
    def __str__(self):
        return f'Numero partido:{self.__numPartido} \nEstadio: {self.__estadio} \nReferi: {self.__referi}'
    
    def setNumPartido(self, numPartido):
        self.__numPartido = numPartido
    def setEstadio(self, estadio):
        self.__estadio = estadio
    def setReferi(self, referi = Arbitro('', '', '')):
        self.__referi = referi
    
    def getNumPartido(self):
        return self.__numPartido
    def getEstadio(self):
        return self.__estadio
    def getReferi(self):
        return self.__referi
    def getListaEquipo1(self):
        return self.__listEquipo1
    def getListaEquipo2(self):
        return self.__listEquipo2
    
    def asignarReferi(self,referi):
        self.__referi = referi 
    
    def addJugador(self, ju):
        if ju.getEquipo().upper() =="COLO COLO":
            if len(self.getListaEquipo1()) < 11:
                if ju not in self.getListaEquipo1():
                    self.getListaEquipo1().append(ju)
                    return 'Jugador agregado de manera exitosa'
                else:
                    return 'El jugador ya existe'
            else:
                return 'El equipo alcanzo la capacidad maxima de 11 personas'
        elif ju.getEquipo().upper()== "WANDERERS":
            if len(self.getListaEquipo2()) < 11:          
                if ju not in self.getListaEquipo2():
                    self.getListaEquipo2().append(ju)
                    return 'Jugador agregado de manera exitosa'
                else:
                    return 'El jugador ya existe'
            else:
                return 'El equipo alcanzo la capacidad maxima de 11 personas'

    def delJugador(self, rut, equipo):
        if equipo.upper() == "COLO COLO":
            if len(self.getListaEquipo1()) != 0:
                for ju in self.getListaEquipo1():
                    if ju.getRut() == rut:
                        self.getListaEquipo1().remove(ju)
                        return 'Jugador eliminado'
                return 'Jugador no se encuentra entre los titulares'
            else:
                return 'Aun no hay jugadores ingresados en este equipo'
        elif equipo.upper() == "WANDERERS":
            if len(self.getListaEquipo2()) != 0:
                for ju in self.getListaEquipo2():
                    if ju.getRut() == rut:
                        self.getListaEquipo2().remove(ju)
                        return 'Jugador eliminado'
                    else:
                        return 'Jugador no se encuentra entre los titulares'
            else:
                return 'Aun no hay jugadores ingresados en este equipo'
        else:
            return "Equipo ingresado es incorrecto"

    def desplegarJugadoresPartido(self):
        print(self)
        if len(self.getListaEquipo1()) > 0:
            for ju in self.getListaEquipo1():
                print('Jugadores de Colo colo:')
                print(ju)
        else:
            print('No hay jugadores ingresados en Colo colo')
        if len(self.getListaEquipo2()) > 0:
            for ju in self.getListaEquipo2():
                print('Jugadores de Wanderers:')
                print(ju)  
        else:
            print('No hay jugadores ingresados en Wanderers')