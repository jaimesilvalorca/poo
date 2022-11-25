from persona import Persona

class Empleado(Persona):
    __listaEmpleado = []
    
    
    def __init__(self, rut="", clave="", nombre="", cargo="", depto = ""):
        super().__init__(rut, clave, nombre, cargo)
        self._depto = depto

    def __str__(self):
        return f"RUT: {self.__rut} CLAVE:{self.__clave} NOMBRE: {self.__nombre} CARGO: {self.__cargo} DEPTO: {self.__depto}"

    def getRut(self):
        return self.__rut

    def getClave(self):
        return self.__clave

    def getNombre(self):
        return self.__nombre

    def getCargo(self):
        return self.cargodepto

    def getDepto(self):
        return self.__depto 

    def setRut(self,rut):
        self.__rut = rut

    def setClave(self, clave):
        self.__clave = clave

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setCargo(self, cargo):
        self.cargodepto = cargo

    def setDepto(self, depto):
        self.__depto = depto   

    def buscarEmpleado(self, rut):
        for e in self.__listaEmpleado:
            if rut == e.getRut():
                return e
        return None

     

    def addEmpleado(self, rut="", clave="", nombre="", cargo="", depto = ""):
        if self.buscarEmpleado(rut) is None:
            empleado = Empleado()
            empleado.setRut(rut)
            empleado.setClave(clave)
            empleado.setNombre(nombre)
            empleado.setCargo(cargo)
            empleado.setDepto(depto)
            self.__listaEmpleado.append(empleado)
            return True
            
        return False

    def subEmpleado(self, rut):
        if self.buscarEmpleado(rut) is not None:
            self.__listaEmpleado.remove(self.buscarEmpleado(rut))

    def mostrarTodos(self):
        if len(self.__listaEmpleado) == 0:
            return print("no hay empleados")       
        
        for a in self.__listaEmpleado:
            print(f"RUT: {a.getRut()} CLAVE:{a.getClave()} NOMBRE: {a.getNombre()} CARGO: {a.getCargo()} DEPTO: {a.getDepto()}")

    def getListaEmpleado(self):
        return   self.__listaEmpleado

    def modificarEmpleado(self, rut, dato, opcion):
        if self.buscarEmpleado(rut) is not None:
            e = self.buscarEmpleado(rut)
            if opcion == 1:
                 e.setClave(dato)
            elif  opcion == 2:
                 e.setNombre(dato)

            elif  opcion == 3:
                 e.setCargo(dato)
                  
            self.__listaEmpleado.remove(self.buscarEmpleado(rut))   
            self.__listaEmpleado.append(e)   