from controlador.dto_empleado import EmpleadoDTO
from controlador.dto_comuna import ComunaDTO
from controlador.dto_cargo import CargoDTO
from modelo.comuna import Comuna
from modelo.cargo import Cargo

comuna = Comuna()
cargo = Cargo()

def validarLogin():
    correoEmpleado = input("Ingrese su correo: ")
    claveEmpleado = input("Ingrese contraseña: ")
    resultado = EmpleadoDTO().validarLogin(correoEmpleado, claveEmpleado)
    return resultado

def validateAddComuna(comuna):
    """numeroComuna = input("Ingrese numero de comuna : ")
    if len(numeroComuna) == 0:
        print("Debe ingresar un nombre de usuario")
        return validateAddUser()
    resu = ComunaDTO().buscarUsuario(numeroComuna)
    if resu is not None:
        print("Datos existentes--> ", resu)
    else:"""
    numeroComuna = input("Ingrese numero de comuna: ") #crear función para validar email
    descripcionComuna = input("Ingrese comuna: ") 
    print(ComunaDTO().agregarComuna(numeroComuna, descripcionComuna, comuna))

def validateAddCargo(cargo=0):
    """numeroCargo = input("Ingrese numero de cargo : ")
    if len(numeroCargo) == 0:
        print("Debe ingresar un nombre de usuario")
        return validateAddUser()
    resu = CargoDTO().buscarUsuario(numeroCargo)
    if resu is not None:
        print("Datos existentes--> ", resu)
    else:"""
    numeroCargo = input("Ingrese numero de cargo: ") #crear función para validar email
    descripcionCargo = input("Ingrese cargo: ") 
    print(CargoDTO().agregarCargo(numeroCargo, descripcionCargo, cargo))
    
def listAll():
    print("\n")
    print("Listado de Comunas")
    resultado = ComunaDTO().listarComunas()
    if len(resultado) > 0:
        for u in resultado:
            print(u)
    else:
        print("no hay resultados")

def validateFindComuna():
    numeroComuna = input("Ingrese el nombre de usuario a buscar : ")
    if numeroComuna == "":
        print("Nombre de usuario incorrecto")
        return validateFindComuna()
    else:
        resu = ComunaDTO().buscarComuna(numeroComuna)
        if resu is not None:
            print(f"Resultado : {resu}")
        else:
            print("Usuario No encontrado")

def validateUpdateComuna():
    numeroComuna = input("Ingrese el nombre de usuario a modificar : ")
    if len(numeroComuna) == 0:
        print("Debe ingresar un nombre de usuario")
        return validateUpdateComuna() 
    resu = ComunaDTO().buscarComuna(numeroComuna)
    if resu is not None:
        print("Datos --> ", resu)
        nuevoNombre = input("Ingrese clave : ") #crear funci+on para valida clave
        print(ComunaDTO().actualizarComuna(numeroComuna,nuevoNombre))

def validateDeleteComuna():
    numeroComuna = input("Ingrese el nombre de usuario a modificar : ")
    if len(numeroComuna) == 0:
        print("Debe ingresar un nombre de usuario")
        return validateDeleteComuna() 
    resu = ComunaDTO().buscarComuna(numeroComuna)
    if resu is not None:
        print("Datos --> ", resu)
        print(ComunaDTO().eliminarComuna(numeroComuna))


def menu():
    
    print("1. CRUD Empleados")
    print("2. CRUD Cargos")
    print("3. CRUD Comunas")
    print("4. Salir")
    opc = int( input("Ingrese una opción : "))
    return opc

def crudCargos():
    print("1. Ingresar Cargo")
    print("2. Modificar Cargo")
    print("3. Eliminar Cargo")
    print("4. Mostrar todos los Cargos")
    print("5. Volver al menú principal")
    print("6. Salir")
    opc = int( input("Ingrese una opción : "))
    return opc

def crudComunas():
    print("1. Ingresar Comuna")
    print("2. Modificar Comuna")
    print("3. Eliminar Comuna")
    print("4. Mostrar todos los Comunas")
    print("5. Volver al menú principal")
    print("6. Salir")
    opc = int( input("Ingrese una opción : "))
    return opc


### para llegar al menu primero hay que loguearse

def inicial(comuna=0, cargo=0):

    while True:
        opc = menu()
        if opc == 1:
            pass
        elif opc == 2:
            while True:
                opc = crudCargos()
                if opc == 1:
                    validateAddCargo(cargo)
                elif opc == 2:
                    pass
                elif opc == 3:
                    pass   
                elif opc == 4:
                    pass 
                elif opc == 5:
                    menu() 
                elif opc == 6:
                    break
        elif opc == 3:
            while True:
                opc = crudComunas()
                if opc == 1:
                    validateAddComuna(comuna)
                elif opc == 2:
                    validateUpdateComuna()
                elif opc == 3:
                    validateDeleteComuna()   
                elif opc == 4:
                    listAll()
                elif opc == 5:
                    menu() 
                elif opc == 6:
                    break
        elif opc == 4:
            break

