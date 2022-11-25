from controlador.dto_user import UserDTO


def listAll():
    print("Listado de Usuarios")
    resultado = UserDTO().listarUsuarios()
    if len(resultado) > 0:
        for u in resultado:
            print(u)
    else:
        print("no hay resultados")

def validateFindUser():
    username = input("Ingrese el nombre de usuario a buscar : ")
    if username == "":
        print("Nombre de usuario incorrecto")
        return validateFindUser()
    else:
        resu = UserDTO().buscarUsuario(username)
        if resu is not None:
            print(f"Resultado : {resu}")
        else:
            print("Usuario No encontrado")
def validateUpdateUser():
    username = input("Ingrese el nombre de usuario a modificar : ")
    if len(username) == 0:
        print("Debe ingresar un nombre de usuario")
        return validateUpdateUser()
    resu = UserDTO().buscarUsuario(username)
    if resu is not None:
        print("Datos --> ", resu)
        email = input("Ingrese email : ") #crear función para validar email
        clave = input("Ingrese clave : ") #crear funci+on para valida clave
        print(UserDTO().actualizarUsuario(username, email,clave))

    else:
        print("Usuario No encontrado")
def validateAddUser():
    username = input("Ingrese nombre de usuario a incorporar: ")
    if len(username) == 0:
        print("Debe ingresar un nombre de usuario")
        return validateAddUser()
    resu = UserDTO().buscarUsuario(username)
    if resu is not None:
        print("Datos existentes--> ", resu)
    else:
        email = input("Ingrese email : ") #crear función para validar email
        clave = input("Ingrese clave : ") #crear funci+on para valida clave
        print(UserDTO().agregarUsuario(username, email,clave))

def validarLogin():
    username = input("Ingrese nombre de usuario : ")
    clave = input("Ingrese contraseña : ")
    resultado = UserDTO().validarLogin(username, clave)
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
            listAll()
        elif opc == 2:
            validateAddUser()
        elif opc == 3:
            #validaDelUser() 
            pass
        elif opc == 4:
            validateUpdateUser()
        elif opc == 5:
            validateFindUser()
        else:
            break

