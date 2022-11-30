from modelo.empleado import Empleado
from utils.encoder import Encoder
from dao.dao_empleado import daoEmpleado

class EmpleadoDTO:

    def validarLogin(self, correoEmpleado, claveEmpleado):
        daoempleado = daoEmpleado()
        resultado = daoempleado.validarLogin(Empleado(correoEmpleado=correoEmpleado, claveEmpleado=Encoder().encode(claveEmpleado)))
        return Empleado(resultado[0],resultado[1]) if resultado is not None else None
        