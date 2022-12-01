from modelo.cargo import Cargo
from dao.dao_cargo import daoCargo

class CargoDTO:

    def addCargo(self, identificaCargo, descripcionCargo):
        daocargo = daoCargo()
        cargo = Cargo(identificaCargo=identificaCargo, descripcionCargo=descripcionCargo)      
        resultado = daocargo.addCargo(cargo)
        return resultado        

    def findAllCargos(self):
        daocargo = daoCargo()
        resultado = daocargo.findAllCargo()
        __listaCargos = [] 
        if resultado is not None:
            for c in resultado:          
                __listaCargos.append(Cargo(identificaCargo=c[0], descripcionCargo=c[1]))  
        return __listaCargos
    
    def findCargo(self, identificaCargo):
        daocargo = daoCargo()
        resultado = daocargo.findCargo(Cargo(identificaCargo=identificaCargo))
        return Cargo(resultado[0], resultado[1]) if resultado is not None else None
    
    def updateCargo(self,numeroCargo, descripcionCargo):
        daocargo = daoCargo()
        resultado = daocargo.updateCargo(numeroCargo,Cargo(identificaCargo=0, descripcionCargo=descripcionCargo))
        return resultado
    
    def delCargo(self,identificaCargo):
        daocargo = daoCargo()
        resultado = daocargo.delCargo(Cargo(identificaCargo=identificaCargo))
        return resultado