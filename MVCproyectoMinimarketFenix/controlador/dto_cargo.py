from modelo.cargo import Cargo
from dao.dao_cargo import daoCargo

class CargoDTO:

    def agregarCargo(self, identificaCargo, descripcionCargo, cargo):
        daocargo = daoCargo()       
        cargo.addCargo(Cargo(identificaCargo=identificaCargo, descripcionCargo=descripcionCargo))
        """ resultado = daocargo.agregarCargo(Cargo(identificaCargo=identificaCargo, descripcionCargo=descripcionCargo)) """

        return "resultado"