""" 
from administrador import Administrador
from persona import Persona """
from empleado import Empleado
"""
empleado = Empleado()
empleado.addEmpleado("16878151", 1234,"juanito", "vago", "informatica")
empleado.addEmpleado("16878151", 1234,"pedrito", "vago", "informatica")
empleado.mostrarTodos()
administrador = Administrador("16878151", 1234,"juanito", "vago", 4321)

##str(administrador)
print(administrador.getAcceso("16878151", 1234,43212))"""

empleado = Empleado()
empleado.addEmpleado("16878151", 1234,"juanito", "info", "informatica")
empleado.addEmpleado("77247", 1234,"pedrito", "info", "informatica")
empleado.mostrarTodos()
empleado.subEmpleado("16878151")
print("-----")
empleado.mostrarTodos()


