from modelo.comuna import Comuna
from dao.dao_comuna import daoComuna



class ComunaDTO:

    def agregarUsuario(self, identificaComuna, descripcionComuna):
        daocomuna = daoComuna()
        resultado = daocomuna.agregarUsuario(Comuna(identificaComuna=identificaComuna, descripcionComuna=descripcionComuna))
        return resultado
