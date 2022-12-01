from modelo.comuna import Comuna
from dao.dao_comuna import daoComuna

class ComunaDTO:

    def addComuna(self, identificaComuna, descripcionComuna):
        daocomuna = daoComuna()
        ciudad = Comuna(identificaComuna=identificaComuna, descripcionComuna=descripcionComuna)      
        resultado = daocomuna.addComuna(ciudad)
        return resultado
        
    def findAllComunas(self):
        daocomuna = daoComuna()
        resultado = daocomuna.findAllComuna()
        __listaComunas = [] 
        if resultado is not None:
            for c in resultado:          
                __listaComunas.append(Comuna(identificaComuna=c[0], descripcionComuna=c[1]))  
        return __listaComunas
    
    def findComuna(self, identificaComuna):
        daocomuna = daoComuna()
        resultado = daocomuna.findComuna(Comuna(identificaComuna=identificaComuna))
        return Comuna(resultado[0], resultado[1]) if resultado is not None else None
    
    def updateComuna(self,numeroComuna, descripcionComuna):
        daocomuna = daoComuna()
        resultado = daocomuna.updateComuna(numeroComuna,Comuna(identificaComuna=0, descripcionComuna=descripcionComuna))
        return resultado
    
    def delComuna(self,identificaComuna):
        daocomuna = daoComuna()
        resultado = daocomuna.delComuna(Comuna(identificaComuna=identificaComuna))
        return resultado


        
