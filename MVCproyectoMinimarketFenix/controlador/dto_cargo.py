from model.empleado import Empleado
from model.cargo import Cargo
from model.comuna import Comuna
from dao.dao_cargo import daoCargo

class CargoDTO:

    def listarUsuarios(self):
        daocargo= daoCargo()
        resultado = daocargo.listarUsuarios()
        lista = []
        if resultado is not None:
            for u in resultado:
                cargo = Cargo(listaCargos=u[0], identificaCargo=u[1], descripcionCargo=u[2])
                lista.append(cargo)
        return lista
