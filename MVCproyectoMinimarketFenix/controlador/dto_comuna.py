from model.empleado import Empleado
from model.cargo import Cargo
from model.comuna import Comuna
from dao.dao_comuna import daoComuna



class ComunaDTO:

    def listarUsuarios(self):
        daocomuna= daoComuna()
        resultado = daocomuna.listarUsuarios()
        lista = []
        if resultado is not None:
            for u in resultado:
                comuna = Comuna(listaComunas=u[0], identificaComuna=u[1], descripcionComuna=u[2])
                lista.append(comuna)
        return lista
