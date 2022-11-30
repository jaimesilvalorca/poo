from conex import conn
import traceback

class daoCargo:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "poo3")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    def agregarCargo(self,cargo):
        sql = "insert into cargo (NUMEROCARGO, NOMBRECARGO) values (%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo.getIdentificaCargos(),cargo.getDescripcionCargo()))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos agregados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje
