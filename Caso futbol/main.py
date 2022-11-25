from partido import Partido
from arbitro import Arbitro
from jugador import Jugador

def validaInt(cadena):
    try:
        numero = int(input(f'Ingresar {cadena} (solo numeros): '))
        if numero > 0:
            return numero
        else:
            print('Debe ingresar un numero valido.')
            return validaInt(cadena)
    except:
        print('Debe ingresar un numero valido.')
        return validaInt(cadena)

def validaStr(cadena):
    string = input(f'Igresar {cadena}: ')
    if len(string) > 0:
        return string
    else:
        print('El campo no puede estar vacio.')
        return validaStr(cadena)

def volver():
    input('Presione enter para volver al menu...\n')
def salir():
    input('Presione enter para salir del menu....\n ')

def menuPrincipal():
    print('''   Menu Principal
   ---- ---------
1. Registrar partido
2. Asignar arbitro
3. Agregar jugador
4. Eliminar jugador
5. Listar jugadores por equipo
6. Salir
''')

    try:
        op2 = int(input('Ingrese opcion: '))
        if op2 >= 1 and op2 <= 6:
            return op2
        else:
            print('Debe ingresar una opcion de acuerdo al rango del menu.\n')
            volver()
            return menuPrincipal()
    except:
        print('Error: Debe ingresar un valor numerico dentro de las opciones.\n')
        volver()
        return menuPrincipal()  
#Instanciar la clase Partido         
parti = Partido('','','')

while True:
    op = menuPrincipal()
    if op == 1:
        parti = Partido((validaStr('numero partido')),(validaStr('estadio')),'NN')
        volver()
    elif op == 2:
        parti.asignarReferi(Arbitro(validaStr('rut: '),validaStr('nombre: '),validaInt('antiguedad: ')))
        volver()
    elif op == 3:
        print(parti.addJugador(Jugador(validaStr('rut'),validaStr('nombre'),validaStr('equipo (nombre)'),validaInt('Numero camiseta'))))
        volver()
    elif op == 4:
        print(parti.delJugador(validaStr('rut'),validaStr('equipo')))
        volver()
    elif op == 5:
        parti.desplegarJugadoresPartido()
        volver()
    else:
        salir()
        print('Saliendo...')
        break