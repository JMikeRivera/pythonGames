# José Miguel Rivera Garza
# A00836995
# ITC
# Proyecto: memorama de profesiones



import random,os

from colorama import init, Fore, Back, Style

colores = [Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.LIGHTWHITE_EX]
 
fondo = [Back.BLACK, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTWHITE_EX]

def pares():
    pars = """teacher
\U0001f468\u200D\U0001f3eb
student
\U0001f468\u200D\U0001f393
farmer
\U0001f468\u200D\U0001f33e
chef
\U0001f468\u200D\U0001f373
mechanic
\U0001f468\u200D\U0001f527
worker
\U0001f468\u200D\U0001f3ed
businessman
\U0001f468\u200D\U0001f4bc
scientist
\U0001f468\u200D\U0001f52c
programmer
\U0001f468\u200D\U0001f4bb
singer
\U0001f468\u200D\U0001f3a4
artist
\U0001f468\u200D\U0001f3a8
astronaut
\U0001f468\u200D\U0001f680
firefighter
\U0001f468\u200D\U0001f692
policeman
\U0001f46e
detective
\U0001f575\uFE0F
guard
\U0001f482
gymnast
\U0001f938
surfer
\U0001f3c4"""


    # convertimos pars en un string
    lista = pars.split("\n")
    return lista


def limpia():
    # funcion que limpia la pantalla sin importar el sistema operativo que este corriendo el programa
    if os.name == "nt": # windows
        os.system("cls")
    else: # "posix"
        os.system("clear") # mac/linux
    
    
def llena_tablero():
    # llenamos el tablero con las cartas volteadas
    matriz = []
    for r in range(6):
        renglon = []
        for c in range(6):
            # agregamos el emoji de la carta joker con el unicode \U0001f0cf
            renglon.append("\U0001f0cf")
        matriz.append(renglon)
    return matriz


def llena_escondidas(lista):
    # llenamos una matriz de emojis y palabras para que el niño pueda aprender ingles
    matriz = []
    # llamar a la funcion pares()
    # random.shuffle(lista)
    for r in range(6):
        renglon = []
        for c in range(6):
            # agregar cada elemento a la lista
            renglon.append(lista.pop(0))
        matriz.append(renglon)
    return matriz
    
    
def despliega_matriz(matriz, r1 = None, c1 = None, r2 = None, c2 = None):
    # desplegamos a pantalla la matriz que recibe en forma de tabla desplegando una cuadricula
    renglones = len(matriz)
    columnas = len(matriz[0])
    print("========1=============2============3=============4============5============6========")
    for r in range(renglones):
        print(r + 1,"|", end = "")
        # desplegamos el renglon r de la matriz
        for c in range(columnas):
            # las condiciones que se deben poner para pintar una carta
            if r1 != None and r1 == r and c1 == c:
                print(Back.LIGHTBLACK_EX + f"{matriz[r][c]}".center(12) + Back.RESET, end = "")
            elif r2 != None and r2 == r and c2 == c:
                print(Back.LIGHTBLACK_EX + f"{matriz[r][c]}".center(12) + Back.RESET, end = "")
            else:
                print(f"{matriz[r][c]}".center(12) + Back.RESET, end = "")
            print("|" + Back.RESET, end = "")
        print("\n"+"==============" * renglones)
    
    
def validar_carta(tablero, r1, c1, r2 = None, c2 = None):
    # verificamos que carta va a validar
    if r2 is None and c2 is None:
        # validamos la carta 1, volvemos a leer r1 y c1 si no se cumplen las condiciones
        while r1 < 1 or r1 > 6 or c1 < 1 or c1 > 6 or tablero[r1 - 1][c1 - 1] != "\U0001f0cf":
            r1 = int(input("Error, ingresa de nuevo la posicion de la carta 1\nRenglón: "))
            c1 = int(input("Columna: "))
        # regresamos el valor de manera correcta, si ingreso 1,1 si ingreso 0,0
        return r1 - 1, c1 - 1
    while r2 < 1 or r2 > 6 or c2 < 1 or c2 > 6 or tablero[r2 - 1][c2 - 1] != "\U0001f0cf" or (r2 - 1 == r1 and c2 - 1 == c1):
        r2 = int(input("Error, ingresa de nuevo la posicion de la carta 2\nRenglón: "))
        c2 = int(input("Columna: "))
    # regresamos el valor de manera correcta, si ingreso 1,1 si ingreso 0,0
    return r2 - 1, c2 - 1
    
    
def validar_carta_computadora(tablero,r1,c1, r2 = None, c2 = None):
    # verificamos que carta va a validar
    if r2 is None and c2 is None:
        # validamos la carta 1 (volvemos a generar un valor random r1, y c1)
        while tablero[r1 -1][c1 - 1] != "\U0001f0cf":
            r1 = random.randint(1,6)
            c1 = random.randint(1,6)
        # retornamos el valor definitivo de la carta 1 de la computadora 1,1 o 0,0
        return r1 - 1, c1 - 1
    else: # validar la carta 2
        while tablero[r2 -1][c2 - 1] != "\U0001f0cf" or r2 - 1 == r1 or c2 - 1 == c1:
            r2 = random.randint(1,6)
            c2 = random.randint(1,6)
        return r2 - 1, c2 - 1
     
     
def son_pares(tablero, escondidas, lista_pares, lista_impares, r1, r2, c1, c2):
    # pares 1 = pares1 + verifica_cambio(r1,c1,r2,c2,tablero,escondidas)
    # ponemos visible la carta 1 y la carta 2 (volteamos visibles las partes escondidas)
    tablero[r1][c1] = escondidas[r1][c1]
    tablero[r2][c2] = escondidas[r2][c2]
    
    # desplegamos el tablero (ver lo que destapamos, elegimos)
    limpia()
    despliega_matriz(escondidas)
    despliega_matriz(tablero, r1, c1 ,r2 ,c2)
    input("Oprime cualquier tecla para continuar")
    gano = 0
    
    # verificar si son pares
    # buscamos donde esta la carta 1
    if escondidas[r1][c1] in lista_pares:
        # ¿en que posicion esta?
        posicion = lista_pares.index(escondidas[r1][c1])
        # verificamos si lo que esta en la lista impares es igual a la carta 2
        if escondidas[r2][c2] == lista_impares[posicion]:
            print("¡Felicidades, es par! \U0001f389")
            gano = 1
        else:
            print("¡No es par! \U0001f614")
            # escondemos de nuevo las cartas que no fueron par
            tablero[r1][c1] = "\U0001f0cf"
            tablero[r2][c2] = "\U0001f0cf"
            gano = 0
    elif escondidas[r1][c1] in lista_impares:
        # ¿en que posicion esta?
        posicion = lista_impares.index(escondidas[r1][c1])
        # verificamos si lo que esta en la lista pares es igual a la carta 2
        if escondidas[r2][c2] == lista_pares[posicion]:
            print("¡Felicidades, es par! \U0001f389")
            gano = 1
        else:
            print("¡No es par! \U0001f614")
            # escondemos de nuevo las cartas que no fueron par
            tablero[r1][c1] = "\U0001f0cf"
            tablero[r2][c2] = "\U0001f0cf"
            gano = 0
    return gano 
            
    
def main():
    # llamamos la funcion que llena las matrices
    # llamamos la funcion pares() = retorna una lista de 36 elementos
    lista = pares()
    
    # separar los pares/impares
    lista_pares = lista[0: :2]
    lista_impares = lista[1: :2]
    
    # creamos el tablero
    tablero = llena_tablero()
    escondidas = llena_escondidas(lista)
    
    # contador de pares del jugador y la computadora antes del ciclo
    pares1 = 0
    pares2 = 0
    
    # se ejecuta mientras alguno de los jugadores no gane
    while pares1 + pares2 < 18:
        limpia()
        despliega_matriz(escondidas)
        despliega_matriz(tablero)
        print("Escribe la posicion de la carta que quieres destapar")
        
        # crear una funcion que valide que las cartas 1.- sean diferentes, 2.- no esten destapadas, 3.- esten dentro del rango
        # seleccionamos la primera carta
        r1 = int(input('Ingresa la posicion de la carta1\nRenglón: '))
        c1 = int(input('Columna: '))
        r1, c1 = validar_carta(tablero,r1,c1)
        # seleccionamos la segunda carta
        r2 = int(input('Ingresa la posicion de la carta2\nRenglón: '))
        c2 = int(input('Columna: '))
        r2,c2 = validar_carta(tablero, r1, c1, r2, c2)
    
        # actualizar el contador del jugador 1
        pares1 += son_pares(tablero, escondidas, lista_pares, lista_impares, r1, r2, c1, c2)
        print("Pares del jugador = ", pares1)
        print("Pares de la computadora = ", pares2)
        
        
    
        # ***** TURNO DE LA COMPUTADORA *****
        
        if pares1 + pares2 < 18:
            # generamos la carta 1 de la computadora
            r1 = random.randint(1,6)
            c1 = random.randint(1,6)
            r1,c1 = validar_carta_computadora(tablero,r1,c1)
    
            # generamos la carta 2 de la computadora
            r2 = random.randint(1,6)
            c2 = random.randint(1,6)
            r2,c2 = validar_carta_computadora(tablero,r2,c2)
    
            # desplegamos al jugador el tiro elegido por la computadora
            print("La computadora eligio la carta1: [",r1 + 1,"]","[",c1 + 1,"]")
            print("La computadora eligio la carta2: [",r2 + 1,"]","[",c2 + 1,"]")
            # creamos una pausa
            input("Enter para continuar")
    
            # actualizamos el contador de la computadora
            pares2 += son_pares(tablero, escondidas, lista_pares, lista_impares, r1, r2, c1, c2)
            print("Pares del jugador = ", pares1)
            print("Pares de la computadora = ", pares2)
    
            # creamos una pausa
            input("Enter para continuar")
    
    # se acaba el ciclo verifica resultado
    # se destaparon todas las cartas
    if pares1 + pares2 >= 18:
        limpia()
        despliega_matriz(tablero)
        if pares1 == pares2:
            salida = Back.LIGHTBLACK_EX + f"¡Empate!" + Back.RESET
            print(salida.center(50,"*"))
        elif pares1 > pares2:
            salida = Back.LIGHTBLACK_EX + f"¡Ganaste, felicidades!" + Back.RESET
            print(salida.center(80,"*"))
        else:
            salida = Back.LIGHTBLACK_EX + f"¡Te gane, intenta de nuevo cuando seas bueno en esto!" + Back.RESET
            print(salida.center(80,"*"))
            
            
main()