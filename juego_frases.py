#agregar menu para elegir la dificultar
# 3 difucultades q varian la cant de palabras permitidas en una frase

#agregar contador de partidas ganadas por cada jugador


##JUEGO
'''Un jugador escribe una frase y otro tiene que adivinarla con las palabras desordenadas'''

import random
from mi_paquete import imprimir
import time

#Constantes
INTENTOS = 3
RONDAS = 3

#formato
verde = "\33[32m"
amarillo = "\33[33m"
rojo = "\33[31m"
azul = "\33[34m"
morado = "\33[35m"
negrita = "\33[1m"
formato_reset = "\33[0m"

#variables Globales
variables_globales = {
    "jugador_1": "",
    "jugador_2": "",
    "puntos_j1": 0,
    "puntos_j2": 0,
}
nombre_1 = ""
nombre_2 = ""
rondas_completas = 0
max_palabras = 0

#Funciones

#definir dificultad
'''
def definir_dificultad():
    global max_palabras
    dificultad = 0
    print("Seleccione la dificultad (1, 2 o 3):")
    print("[1] Facil")
    print("[2] Medio")
    print("[3] Dificil")

    dificultad = input("Dificultad deseada: ")
    while dificultad != 1 and dificultad != 2 and dificultad != 3:
        print(rojo + "La opcion ingresada no es valida!" + formato_reset)
        dificultad = input("Dificultad deseada: ")

    if dificultad == 1:
        max_palabras = 4
    elif dificultad == 2:
        max_palabras = 6
    elif dificultad == 3:
        max_palabras = 8
'''
#enrocar
def enrocar(param1,param2):
    aux = variables_globales[param1]
    variables_globales[param1] = variables_globales[param2]
    variables_globales[param2] = aux

#explicacion del juego
def presention_juego():
    imprimir.limpiar_pantalla()
    print(negrita + "DESAFIO DE FRASES" + formato_reset)
    print("El juego consiste en que un jugador ingresa una frase secreta y el otro jugador tiene que adivinarla viendo las palabras desordenadas")
    print("El jugador que haya hecho mas puntos luego de 3 rondas gana.\n")
    time.sleep(6)

#volver a jugar o terminar
def repetir_o_finalizar():
    jugar_devuelta = input("Desean volver a Jugar? (Si/No) ")
    #contemplo errores
    while jugar_devuelta != "si" and jugar_devuelta != "SI" and jugar_devuelta != "Si" and jugar_devuelta != "sI" and jugar_devuelta != "no" and jugar_devuelta != "NO" and jugar_devuelta != "No" and jugar_devuelta != "nO":
        print(rojo + "Porfavor ingrese una respuesta valida." + formato_reset)
        jugar_devuelta = input("Desean volver a Jugar? (Si/No)")
    if jugar_devuelta == "si" or jugar_devuelta == "Si" or jugar_devuelta == "SI" or jugar_devuelta == "sI":
        enrocar("jugador_1", "jugador_2") #cambian los turnos
        #Reinicio contadores
        variables_globales["puntos_j1"] = 0
        variables_globales["puntos_j2"] = 0
        global rondas_completas
        rondas_completas = 0
        jugar_partida()
    else:
        print("\nGracias por jugar\n")

#Nombres de Jugadores
def ingresar_nombres():
    global nombre_1, nombre_2
    while nombre_1 == nombre_2: #evito nombres iguales

        nombre_1 = input("Jugador " + azul + "Azul" + formato_reset + ", ingrese su nombre: ")
        while nombre_1 == "" or " " in nombre_1: #evito espacios y nombres vacios
            if nombre_1 == "":
                print(rojo + "Los nombres no pueden ser vacios!\n" + formato_reset) #msj de error
                nombre_1 = input("Jugador " + azul + "Azul" + formato_reset + ", ingrese su nombre: ")
            if " " in nombre_1:
                print(rojo + "Los nombres no pueden tener espacios!\n" + formato_reset) #msj de error
                nombre_1 = input("Jugador " + azul + "Azul" + formato_reset + ", ingrese su nombre: ")

        print() #dejo linea vacia

        nombre_2 = input("Jugador " + morado + "Morado" + formato_reset + ", ingrese su nombre: ")
        while nombre_2 == "" or " " in nombre_2: #evito espacios y nombres vacios
            if nombre_2 == "":
                print(rojo + "Los nombres no pueden ser vacios!\n" + formato_reset) #msj de error
                nombre_2 = input("Jugador " + morado + "Morado" + formato_reset + ", ingrese su nombre: ")
            if " " in nombre_2:
                print(rojo + "Los nombres no pueden tener espacios!\n" + formato_reset) #msj de error
                nombre_2 = input("Jugador " + morado + "Morado" + formato_reset + ", ingrese su nombre: ")
        
        if nombre_1 == nombre_2:
            print(rojo + "Los nombres no pueden ser iguales!\n" + formato_reset) #msj de error
        
    #pinto nombres de colores
    variables_globales["jugador_1"] = azul + nombre_1 + formato_reset
    variables_globales["jugador_2"] = morado + nombre_2 + formato_reset

def jugar_partida():
    global intento, rondas_completas
    while rondas_completas < RONDAS:
        if rondas_completas == 0 or rondas_completas%1 == 0:
            imprimir.limpiar_pantalla()
            print(negrita + f"Ronda {int(rondas_completas) + 1}" + formato_reset)

        #ingresar frase a adivinar
        frase = input(variables_globales["jugador_1"] + ", ingrese una frase: ")
        imprimir.limpiar_pantalla()

        #desordenar frase
        lista_frase = frase.split()
        random.shuffle(lista_frase)
        frase_desordenada = " ".join(lista_frase)

        #mostrar frase desordenada
        print("La frase que ingreso " + variables_globales["jugador_1"] + f" desordenada es:\n'{frase_desordenada}'\n")

        #adivinar frase
        print(variables_globales["jugador_2"] + f", tienes {INTENTOS} intentos para adivinar la frase:")
        intento = 0
        puntos = 3
        while intento < INTENTOS:
            #adivinar
            frase_propuesta = input(f"{intento + 1}. ")

            if frase_propuesta == frase:
                if puntos == 1:
                    print(f"\nAdivinaste en el intento numero {intento +1}. Sumas {puntos} punto.\n")
                else:
                    print(f"\nAdivinaste en el intento numero {intento +1}. Sumas {puntos} puntos.\n")
                break
            else:
                intento += 1
                puntos -= 1
        else:
            print(f"\nNo adivinaste. Sumas {puntos} puntos.\n")

        #Actualizo rondas y puntos        
        variables_globales["puntos_j2"] += puntos
        rondas_completas += 0.5

        #limpio pantalla de la jugada
        time.sleep(2.5)
        imprimir.limpiar_pantalla()

        #Muestro puntajes parciales
        if rondas_completas == 1 or rondas_completas ==2:
            print(negrita + "Puntajes parciales:" + formato_reset)
            print(variables_globales["jugador_2"] + f": {variables_globales["puntos_j2"]}")
            print(variables_globales["jugador_1"] + f": {variables_globales["puntos_j1"]}")
            time.sleep(4)

        #limpio pantalla para el cambio de turnos
        imprimir.limpiar_pantalla()

        #Rotacion de variables
        enrocar("jugador_1", "jugador_2")
        enrocar("puntos_j1", "puntos_j2")
    
    #Muestro  puntajes finales
    print(negrita + "Puntajes finales:" + formato_reset)
    print(variables_globales["jugador_1"] + f": {variables_globales["puntos_j1"]}")
    print(variables_globales["jugador_2"] + f": {variables_globales["puntos_j2"]}")
    
    #Ganador
    if variables_globales["puntos_j1"] > variables_globales["puntos_j2"]:
        print(verde + "\nEl Ganador es " + formato_reset + variables_globales["jugador_1"] + verde + "! Felicitaciones :)" + formato_reset)
    elif variables_globales["puntos_j2"] > variables_globales["puntos_j1"]:
        print(verde + "\nEl Ganador es " + formato_reset + str(variables_globales["jugador_2"]) + verde + "! Felicitaciones :)" + formato_reset)
    else:
        print(amarillo + "\nEs un empate!" + formato_reset)
    
    #Limpiar pantalla
    time.sleep(6)
    imprimir.limpiar_pantalla()

    #deciden si vuelven a jugar o finaliza
    repetir_o_finalizar()

def main():
    presention_juego()
    ingresar_nombres()
    jugar_partida()

if __name__ == "__main__":
    main()