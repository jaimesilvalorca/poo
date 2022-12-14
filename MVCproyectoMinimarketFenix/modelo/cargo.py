class Cargo():

    __listaCargos = []

    def __init__(self,identificaCargo=0, descripcionCargo=''):
        self.__identificaCargo = identificaCargo
        self.__descripcionCargo = descripcionCargo

    def __str__(self):
        return f'Cargos:{self.__listaCargos} \nIdentificador Cargo: {self.__identificaCargo} \nDescripcion Cargo: {self.__descripcionCargo}'

    def setListaCargos(self, listaCargos):
        self.__listaCargos = listaCargos

    def setIdentificaCargos(self, identificaCargo):
        self.__identificaCargo = identificaCargo

    def setDescripcionCargo(self, descripcionCargo):
        self.__descripcionCargo = descripcionCargo

    def getListaCargos(self):
        return self.__listaCargos

    def getIdentificaCargos(self):
        return self.__identificaCargo

    def getDescripcionCargo(self):
        return self.__descripcionCargo

    def addCargo(self, cargo):
        self.__listaCargos.append(cargo)