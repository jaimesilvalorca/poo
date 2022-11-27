
class Comuna():

    __listaComunas = []

    def __init__(self,identificaComuna=0,descripcionComuna=''):

        self.__identificaComuna = identificaComuna
        self.__descripcionComuna = descripcionComuna

    def __str__(self):
        return f'Comunas:{self.__listaComunas} \nIdentificador comuna: {self.__identificaComuna} \nDescripcion Comuna: {self.__descripcionComuna}'        

    def setListaComunas(self, listaComunas):
        self.__listaComunas = listaComunas

    def setIdentificaComunas(self, identificaComuna):
        self.__identificaComuna = identificaComuna

    def setDescripcionComuna(self, descripcionComuna):
        self.__descripcionComuna = descripcionComuna

    def getListaComunas(self):
        return self.__listaComunas

    def getIdentificaComunas(self):
        return self.__identificaComuna

    def getDescripcionComuna(self):
        return self.__descripcionComuna
