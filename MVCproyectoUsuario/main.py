from controlador.validations import inicial, validarLogin


##### login
intentos = 1
print("Sistema POO")
while intentos <= 3:
    try:
        resu = validarLogin()
        if resu is not None:
            print(f"Bienvenido(a) Sr(a). : {resu.username}")
            inicial()
            break
        else:
            print("usuario o contraseña incorrecta")
            intentos += 1
    except:
        print("intentar nuevamengte")
if intentos == 4:
    print("contraseña boqueada")