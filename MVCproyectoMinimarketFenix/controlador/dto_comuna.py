from modelo.comuna import Comuna
from dao.dao_comuna import daoComuna

class ComunaDTO:

    def agregarComuna(self, identificaComuna, descripcionComuna):
        daocomuna = daoComuna()
        ciudad = Comuna(identificaComuna=identificaComuna, descripcionComuna=descripcionComuna)      
        resultado = daocomuna.agregarComuna(ciudad)
        return resultado
        
    def listarComunas(self):
        daocomuna = daoComuna()
        resultado = daocomuna.listarComuna()
        __listaComunas = [] 
        if resultado is not None:
            for c in resultado:          
                __listaComunas.append(Comuna(identificaComuna=c[0], descripcionComuna=c[1]))  
        return __listaComunas
    
    def buscarComuna(self, identificaComuna):
        daocomuna = daoComuna()
        resultado = daocomuna.buscarComuna(Comuna(identificaComuna=identificaComuna))
        return Comuna(resultado[0], resultado[1]) if resultado is not None else None
    
    def actualizarComuna(self,numeroComuna, descripcionComuna):
        daocomuna = daoComuna()
        resultado = daocomuna.actualizarComuna(numeroComuna,Comuna(identificaComuna=0, descripcionComuna=descripcionComuna))
        return resultado
    
    def eliminarComuna(self,identificaComuna):
        daocomuna = daoComuna()
        resultado = daocomuna.eliminarComuna(Comuna(identificaComuna=identificaComuna))
        return resultado


        
