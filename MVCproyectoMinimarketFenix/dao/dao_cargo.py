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

    def addCargo(self,cargo):
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

    def findAllCargo(self):
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select NUMEROCARGO, NOMBRECARGO from cargo")
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return result
    
    def findCargo(self, cargo):
        sql = "select NUMEROCARGO, NOMBRECARGO from cargo where NUMEROCARGO = %s"
        resultado = None
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo.getIdentificaCargos(),))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado

    def updateCargo(self, numeroCargo,cargo):
        sql = "update cargo set NOMBRECARGO = %s where NUMEROCARGO = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo.getDescripcionCargo(),numeroCargo))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos modificados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def delCargo(self,cargo):
        sql = "delete from cargo where NUMEROCARGO=%s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo.getIdentificaCargos(),))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Cargo eliminado correctamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje