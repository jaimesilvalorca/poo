from conex import conn
import traceback

class daoCargo:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "mydb")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn
