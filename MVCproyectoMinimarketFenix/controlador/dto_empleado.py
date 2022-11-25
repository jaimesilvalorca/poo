from model.empleado import Empleado
from model.cargo import Cargo
from model.comuna import Comuna
from utils.encoder import Encoder
from dao.dao_empleado import daoEmpleado

class EmpleadoDTO:

    def listarUsuarios(self):
        daoempleado= daoEmpleado()
        resultado = daoempleado.listarUsuarios()
        lista = []
        if resultado is not None:
            for u in resultado:
                empleado = Empleado(runEmplado=u[0], nombreEmpleado=u[1], apellidoEmpleado=u[2], direccionEmpleado=u[3],claveEmpleado=u[4],correoEmpleado=u[5],)
                lista.append(empleado)
        return lista

    def buscarUsuario(self, runEmpleado):
        daoempleado = daoEmpleado()
        resultado = daoempleado.buscarUsuario(Empleado(runEmpleado=runEmpleado))
        return Empleado(resultado[0], resultado[1], resultado[2]) if resultado is not None else None

    def validarLogin(self, correoEmpleado, clave):
        daoempleado = daoEmpleado()
        resultado = daoempleado.validarLogin(Empleado(correoEmpleado=correoEmpleado, claveEmpleado=Encoder().encode(clave)))
        return Empleado(resultado[0]) if resultado is not None else None

    def actualizarUsuario(self, runEmpleado, nombreEmpleado, apellidoEmpleado, direccionEmpleado, claveEmpleado, correoEmpleado):
        daoempleado = daoEmpleado()
        resultado = daoempleado.actualizarUsuario(Empleado(runEmpleado=runEmpleado, nombreEmpleado=nombreEmpleado, apellidoEmpleado=apellidoEmpleado, direccionEmpleado=direccionEmpleado, correoEmpleado=correoEmpleado,claveEmpleado=Encoder().encode(claveEmpleado)))
        return resultado

    def agregarUsuario(self, runEmpleado, nombreEmpleado, apellidoEmpleado,direccionEmpleado, claveEmpleado, correoEmpleado):
        daoempleado = daoEmpleado()
        resultado = daoempleado.agregarUsuario(Empleado(runEmpleado=runEmpleado, nombreEmpleado=nombreEmpleado, apellidoEmpleado=apellidoEmpleado, direccionEmpleado=direccionEmpleado, correoEmpleado=correoEmpleado,claveEmpleado=Encoder().encode(claveEmpleado)))
        return resultado
