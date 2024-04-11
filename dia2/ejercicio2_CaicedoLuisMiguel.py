#2.
#Este programa simula un juego interactivo en el que el usuario debe adivinar
# un número secreto elegido aleatoriamente por el programa. El número secreto
# está en el rango de 1 a 100. Después de cada intento del usuario, el programa
# proporciona pistas indicando si el número secreto es mayor o menor que la suposición
# actual. El objetivo es adivinar el número secreto en la menor cantidad de intentos posible.
print("vamos a jugar algo")
print("se va a crear un numero aleatorio y tendras que adivinarlo")
print("por cada intento te daré una pista")
print("trata de adivinarlo en la menor cantidad de intentos posibles")# son indicaciones para el usuario
print("el numero se encuentra entre el 1 y el 100")
import random
azar = random.randint(1,100)#se crea el numero aleatirio
yo = True
while yo == True:#mientras que "yo" sea verdadero el proceso se va a repetir
    usu = int(input("ingresa tu intento\n"))#se lee el intento del usuario
    if usu>azar:# si el intento es mayor al numero va a mostrar el siguinte mensaje
        print("el numero es menor")
    if usu<azar:# si el intento es menor al numero va a mostrar el siguinte mensaje
        print("el numero es mayor")
    if usu == azar:# si el intento es igual a numero va a decirle a usuario que acertó
        print("acertaste")#va a decirle a usuario que acertó
        yo = False# y "yo" pasa a ser falso por lo tanto acaba el programa

#DESARROLLADO POR: Caicedo Bermon Luis Miguel c.c: 1090381345