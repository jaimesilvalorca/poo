from controlador.dto_empleado import EmpleadoDTO

def validarLogin():
    correoEmpleado = input("Ingrese su correo: ")
    claveEmpleado = input("Ingrese contraseña: ")
    resultado = EmpleadoDTO().validarLogin(correoEmpleado, claveEmpleado)
    return resultado


def menu():
    print("1. Listar Usuarios")
    print("2. Agregar Usuario")
    print("3. Eliminar Usuario")
    print("4. Actualizar Usuario")
    print("5. Buscar Usuario")
    print("6. Salir")
    opc = int( input("Ingrese una opción : "))
    return opc

### para llegar al menu primero hay que loguearse

def inicial():

    while True:
        opc = menu()
        if opc == 1:
            pass
        elif opc == 2:
            pass
        elif opc == 3:
            pass
        elif opc == 4:
            pass
        elif opc == 5:
            pass
        else:
            break

