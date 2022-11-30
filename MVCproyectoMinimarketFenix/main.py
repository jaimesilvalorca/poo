from controlador.validations import inicial, validarLogin
from modelo.comuna import Comuna
from modelo.cargo import Cargo

""" comuna = Comuna()
cargo = Cargo() """
""" comuna.addComuna(Comuna(10, "san bk"))

for e in comuna.getListaComunas():
    print(e.getIdentificaComunas(),e.getDescripcionComuna()) """

##### login
intentos = 1
print("Sistema POO")
while intentos <= 3:
    try:
        """ resu = validarLogin() """
        resu = True
        if resu is not None:
            print(f"Bienvenido al CRUD Minimarket Fenix")
            inicial()
            break
        else:
            print("usuario o contraseña incorrecta")
            intentos += 1
    except:
        print("intentar nuevamente")
if intentos == 4:
    print("contraseña boqueada")