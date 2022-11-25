from persona import Persona

class Administrador(Persona):

    def __init__(self, rut="", clave="", nombre="", cargo="", claveAdministrador=""):
        super().__init__(rut, clave, nombre, cargo)
        self.__claveAdministrador = claveAdministrador
    
    def getClaveAdministrador(self):
        return self.__claveAdministrador

   
    def getAcceso(self, rut, clave, claveAdministrador ):
        return (self.getRut() == rut and self.getClave() == clave and self.getClaveAdministrador() == claveAdministrador)
          