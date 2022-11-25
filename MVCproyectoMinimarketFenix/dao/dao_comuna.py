from conex import conn
import traceback

class daoComuna:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "mydb")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn
