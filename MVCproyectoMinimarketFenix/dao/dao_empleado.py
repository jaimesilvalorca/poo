from conex import conn
import traceback

class daoEmpleado:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "poo3")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    print(conn)

    def validarLogin(self,resultado):
        sql = "select CORREO,CLAVE from empleado where CORREO = %s and CLAVE = %s"
        c = self.getConex()
        #print(c)
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (resultado.getCorreoEmpleado(), resultado.getClaveEmpleado()))

            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado

    