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

def validateAddComuna():
    numeroComuna = input("Ingrese numero de comuna : ")
    if len(numeroComuna) == 0:
        print("Debe ingresar un numero de Comuna")
        return validateAddComuna()
    resu = ComunaDTO().findComuna(numeroComuna)
    if resu is not None:
        print("Usuario encontrado")
        print("-------------------")
        print("Datos existentes--> ", resu)
    else:
        print("Usuario no encontrado, listo para ingresar")        
        descripcionComuna = input("Ingrese nombre de la comuna: ") 
        print(ComunaDTO().addComuna(numeroComuna, descripcionComuna))

def validateAddCargo():
    numeroCargo = input("Ingrese numero de cargo : ")
    if len(numeroCargo) == 0:
        print("Debe ingresar un numero de Cargo")
        return validateAddCargo()
    resu = CargoDTO().findCargo(numeroCargo)
    if resu is not None:
        print("Usuario encontrado")
        print("-------------------")
        print("Datos existentes--> ", resu)
    else:
        print("Usuario no encontrado, listo para ingresar")
        descripcionCargo = input("Ingrese descripcion del cargo: ") 
        print(CargoDTO().addCargo(numeroCargo, descripcionCargo))
    
def listAllComunas():
    print("\n")
    print("Listado de Comunas")
    resultado = ComunaDTO().findAllComunas()
    if len(resultado) > 0:
        for u in resultado:
            print(u)
    else:
        print("no hay resultados")

def listAllCargos():
    print("\n")
    print("Listado de Cargos")
    resultado = CargoDTO().findAllCargos()
    if len(resultado) > 0:
        for u in resultado:
            print(u)
    else:
        print("no hay resultados")

def validateFindComuna():
    numeroComuna = input("Ingrese el numero de comuna a buscar: ")
    if numeroComuna == "":
        print("Numero de comuna incorreto")
        return validateFindComuna()
    else:
        resu = ComunaDTO().findComuna(numeroComuna)
        if resu is not None:
            print(f"Resultado : {resu}")
        else:
            print("Usuario No encontrado")

def validateFindCargo():
    numeroCargo = input("Ingrese el numero de Cargo a buscar: ")
    if numeroCargo == "":
        print("Numero de Cargo incorreto")
        return validateFindCargo()
    else:
        resu = CargoDTO().findCargo(numeroCargo)
        if resu is not None:
            print(f"Resultado : {resu}")
        else:
            print("Usuario No encontrado")

def validateUpdateComuna():
    numeroComuna = input("Ingrese el numero de comuna para modificar : ")
    if len(numeroComuna) == 0:
        print("Debe ingresar una comuna valida")
        return validateUpdateComuna() 
    resu = ComunaDTO().findComuna(numeroComuna)
    if resu is not None:
        print("Comuna: ", resu)
        nuevoNombre = input("Ingrese el nuevo nombre:  ")
        print(ComunaDTO().updateComuna(numeroComuna,nuevoNombre))

def validateUpdateCargo():
    numeroCargo = input("Ingrese el numero de Cargo para modificar : ")
    if len(numeroCargo) == 0:
        print("Debe ingresar un numero de cargo valido")
        return validateUpdateCargo() 
    resu = CargoDTO().findCargo(numeroCargo)
    if resu is not None:
        print("Cargo: ", resu)
        nuevoNombre = input("Ingrese el nuevo nombre:  ")
        print(CargoDTO().updateCargo(numeroCargo,nuevoNombre))

def validateDeleteComuna():
    numeroComuna = input("Ingrese el numero de la comuna que va eliminar: ")
    if len(numeroComuna) == 0:
        print("Debe ingresar una comuna valida")
        return validateDeleteComuna() 
    resu = ComunaDTO().findComuna(numeroComuna)
    if resu is not None:
        print("comuna: ", resu)
        print(ComunaDTO().delComuna(numeroComuna))

def validateDeleteCargo():
    numeroCargo = input("Ingrese el numero de la Cargo que va eliminar: ")
    if len(numeroCargo) == 0:
        print("Debe ingresar una Cargo valido")
        return validateDeleteCargo() 
    resu = CargoDTO().findCargo(numeroCargo)
    if resu is not None:
        print("Cargo: ", resu)
        print(CargoDTO().delCargo(numeroCargo))

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



def inicial():

    while True:
        opc = menu()
        if opc == 1:
            pass
        elif opc == 2:
            while True:
                opc = crudCargos()
                if opc == 1:
                    validateAddCargo()
                elif opc == 2:
                    validateUpdateCargo()
                elif opc == 3:
                    validateDeleteCargo()   
                elif opc == 4:
                    listAllCargos()
                elif opc == 5:
                    break 
                elif opc == 6:
                    break;
        elif opc == 3:
            while True:
                opc = crudComunas()
                if opc == 1:
                    validateAddComuna()
                elif opc == 2:
                    validateUpdateComuna()
                elif opc == 3:
                    validateDeleteComuna()   
                elif opc == 4:
                    listAllComunas()
                elif opc == 5:
                    break
                elif opc == 6:
                    break;
        elif opc == 4:
            break

