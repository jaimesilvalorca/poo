from modelo.cargo import Cargo
from dao.dao_cargo import daoCargo

class CargoDTO:

    def agregarCargo(self, identificaCargo, descripcionCargo):
        daocargo = daoCargo()
        cargo = Cargo(identificaCargo=identificaCargo, descripcionCargo=descripcionCargo)      
        resultado = daocargo.agregarCargo(cargo)
        return resultado        

    def listarCargos(self):
        daocargo = daoCargo()
        resultado = daocargo.listarCargo()
        __listaCargos = [] 
        if resultado is not None:
            for c in resultado:          
                __listaCargos.append(Cargo(identificaCargo=c[0], descripcionCargo=c[1]))  
        return __listaCargos
    
    def buscarCargo(self, identificaCargo):
        daocargo = daoCargo()
        resultado = daocargo.buscarCargo(Cargo(identificaCargo=identificaCargo))
        return Cargo(resultado[0], resultado[1]) if resultado is not None else None
    
    def actualizarCargo(self,numeroCargo, descripcionCargo):
        daocargo = daoCargo()
        resultado = daocargo.actualizarCargo(numeroCargo,Cargo(identificaCargo=0, descripcionCargo=descripcionCargo))
        return resultado
    
    def eliminarCargo(self,identificaCargo):
        daocargo = daoCargo()
        resultado = daocargo.eliminarCargo(Cargo(identificaCargo=identificaCargo))
        return resultado