from administrador import Administrador
from persona import Persona
from empleado import Empleado


def validaRut(): 
    rut = input("Ingrese rut (sin puntos, ni guión):")
    if rut[0:len(rut)-1].isnumeric() and rut[-1] in "0123456789kK":
        if len(rut)!=9: 
            print("Largo del Rut, debe ser de 9 digitos") 
            return validaRut() 
        else: 
            return rut
    else:
        print("Dato no cumple con formato solicitado") 
        return validaRut()

def validaClave():
    clave = input("Ingrese contraseña:")
    if clave != "":
        return clave
    else:
        print("Debe ingresar una contraseña")
        return validaClave()

def validaNombre():
    nombre = input("Ingrese nombre:")
    if nombre != "":
        return nombre
    else:
        print("Debe ingresar un nombre válido")
        return validaNombre()

def validaCargo():
    cargo = input("Ingrese cargo:")
    if cargo != "":
        return cargo
    else:
        print("Debe ingresar un cargo válido")
        return validaCargo()

def validaDepto():
    depto = input("Ingrese departamento:")
    if depto != "":
        return depto
    else:
        print("Debe ingresar un departamento válido")
        return validaDepto()

administrador = Administrador("11111111", "1234","Daniel", "Administrador", "15B16K")
e = Empleado()
def ingresoOpcion(cant):
    try:
        op = int(input("Digite opción:"))
        if op >=1 and op<=cant:
            return op
        else:
            print("Debe ingresar una opción valida")
            ingresoOpcion(cant)
    except Exception:
        print("Error en el ingreso")
        ingresoOpcion(cant)

def login():
    acceso1 = input("Ingrese su rut: ")
    clave1 = input("Ingrese clave empleado: ")
    clave2 = input("Ingrese clave administrador: ")
    lista = []
    lista.append(acceso1)
    lista.append(clave1)
    lista.append(clave2)
    return lista    

def menu():
    print("Menú principal")
    print("1. Administrador")
    print("2. Empleado")
    print("3. Ayuda")
    print("4. Salir") 

def menuEmpleado():
    print("1. Ingresar Empleado")
    print("2. Eliminar Empleado")
    print("3. Modificar Empleado")
    print("4. Buscar Empleado")
    print("5. Mostrar Empleados")
    print("6. Volver al menu principal")

def subMenu():
    print("1. Modifica clave")
    print("2. Modifica nombre")
    print("3. Modifica cargo")
    print("4. Volver al menú anterior")


while True:
    menu()
    op = ingresoOpcion(4)
    if op == 4:
        break;
    elif op == 1:
        datosAcceso = login()         

        if administrador.getAcceso(datosAcceso[0], datosAcceso[1], datosAcceso[2]):
            print("-----------------------------------")
            print("Sesion iniciada como administrador")
            print("-----------------------------------")
            while True:
                menuEmpleado()
                op = ingresoOpcion(6)
                if op ==6:
                    break;
                elif op == 1:
                    e.addEmpleado(validaRut(),validaClave(),validaNombre(),validaCargo(),validaDepto())
                    tecla = input("Digite enter para continuar")

                elif op == 2:
                    e.subEmpleado(validaRut())
                    tecla = input("Digite enter para continuar")
                    print()
                elif op == 3:
                    while True:
                        subMenu()
                        op = ingresoOpcion(4)
                        
                        if op == 4:
                            break
                        elif op == 1:
                            e.modificarEmpleado(validaRut(),validaClave(),op)
                            tecla = input("Digite enter para continuar")

                        elif op == 2:
                            e.modificarEmpleado(validaRut(),validaNombre(),op)
                            tecla = input("Digite enter para continuar")
                        elif op == 3:
                            e.modificarEmpleado(validaRut(),validaCargo(),op)
                            tecla = input("Digite enter para continuar")

                elif op == 4:
                    emp = e.buscarEmpleado(validaRut())
                    if emp is not None:
                        print(f"RUT: {emp.getRut()} CLAVE:{emp.getClave()} NOMBRE: {emp.getNombre()} CARGO: {emp.getCargo()} DEPTO: {emp.getDepto()}")
                        
                    else:
                        print("No se encontró ningun empleado")

                    tecla = input("Digite enter para continuar")                                 
                
                elif op == 5:
                    e.mostrarTodos() #error#
                    tecla = input("Digite enter para continuar")
        else:
             print("--------------------------------------------")
             print("Los datos de ingreso no son de administrador")
             print("Intente nuevamente")
             print("--------------------------------------------")
                    
    elif op == 2:
        pass
    elif op == 3:
        pass