from modelo.cargo import Cargo
from modelo.comuna import Comuna

class Empleado:
    def __init__(self, runEmpleado ='', nombreEmpleado='', apellidoEmpleado='', cargo='', direccionEmpleado='', claveEmpleado='', correoEmpleado='', comuna=''):

        self.__runEmpleado = runEmpleado
        self.__nombreEmpleado = nombreEmpleado
        self.__apellidoEmpleado = apellidoEmpleado
        self.__cargo = cargo
        self.__direccionEmpleado = direccionEmpleado
        self.__claveEmpleado = claveEmpleado
        self.__correoEmpleado = correoEmpleado
        self.__comuna = comuna
        
    def __str__(self):
        return f'Rut:{self.__runEmpleado} \nNombre: {self.__nombreEmpleado} \nApellido: {self.__apellidoEmpleado} \nCargo: {self.__cargo} \nDirección: {self.__direccionEmpleado} \nCorreo: {self.__correoEmpleado} \nComuna: {self.__comuna} \nclave:{self.__claveEmpleado} '

    def setRutEmpleado(self, runEmpleado):
        self.__runEmpleado = runEmpleado

    def setNombreEmpleado(self, nombreEmpleado):
        self.__nombreEmpleado = nombreEmpleado

    def setApellidoEmpleado(self, apellidoEmpleado):
        self.__apellidoEmpleado = apellidoEmpleado

    def setCargo(self, cargo = Cargo('','')):
        self.__cargo = cargo

    def setDireccionEmpleado(self, direccionEmpleado):
        self.__direccionEmpleado = direccionEmpleado

    def setClaveEmpleado(self, claveEmpleado):
        self.__claveEmpleado = claveEmpleado

    def setCorreoEmpleado(self, correoEmpleado):
        self.__correoEmpleado = correoEmpleado

    def setComuna(self, comuna = Comuna('','')):
        self.__comuna = comuna

    def getRutEmpleado(self):
        return self.__runEmpleado

    def getNombreEmpleado(self):
        return self.__nombreEmpleado

    def getApellidoEmpleado(self):
        return self.__apellidoEmpleado

    def getCargo(self):
        return self.__cargo

    def getDireccionEmpleado(self):
        return self.__direccionEmpleado

    def getClaveEmpleado(self):
        return self.__claveEmpleado

    def getCorreoEmpleado(self):
        return self.__correoEmpleado

    def getComuna(self):
        return self.__comuna