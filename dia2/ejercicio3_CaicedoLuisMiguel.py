#3.
#El programa selecciona aleatoriamente un número secreto entre 1 y 100.,
# donde el usuario tiene un total de 10 intentos para adivinar el número secreto.
# Después de cada intento, el programa dará pistas indicando si el número secreto
# es mayor o menor que la suposición actual del usuario. Si el usuario adivina correctamente,
# el programa felicitará al jugador y mostrará en cuántos intentos lo logró.
#El programa debe ser amigable y explicar claramente las instrucciones al usuario.
print("vamos a jugar algo")
print("se va a crear un numero aleatorio y tendras que adivinarlo")
print("por cada intento te daré una pista")
print("tienes 10 intentos para adivinar el numero")# son indicaciones para el usuario
print("el numero se encuentra entre el 1 y el 100")
import random
azar = random.randint(1,100)#se crea el numero aleatirio
print (azar)
a=0
yo = True
while yo == True:#mientras que "yo" sea verdadero el proceso se va a repetir
    usu = int(input("ingresa tu intento\n"))#se lee el intento del usuario
    if usu>azar:# si el intento es mayor al numero va a mostrar el siguinte mensaje
        print("el numero es menor")
    if usu<azar:# si el intento es menor al numero va a mostrar el siguinte mensaje
        print("el numero es mayor")
    a=a+1#es un contador para saber cuantos intentos van
    if usu == azar:# si el intento es igual a numero va a decirle a usuario que acertó
        print("acertaste\nlo lograste en", a, "intentos")#va a decirle a usuario que acertó
        yo = False# y "yo" pasa a ser falso por lo tanto acaba el programa
    if a > 10:#si la cantidad de intentos es mayor a 10
        print("perdiste todos los intentos:(")#se escribe esto
        yo = False #y yo pasa a ser falso por lo tanto se acaba el programa

#DESARROLLADO POR: Caicedo Bermon Luis Miguel c.c: 1090381345