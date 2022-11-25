class Persona:
    def __init__(self, rut="", clave="", nombre="", cargo=""):
        self.__rut = rut
        self.__clave = clave
        self.__nombre = nombre
        self.__cargo = cargo

    def __str__(self):
        return f"RUT : {self.__rut} Nombre: {self.__nombre} Cargo: {self.__cargo}"
    
    def getRut(self):
        return self.__rut
    
    def getClave(self):
        return self.__clave
