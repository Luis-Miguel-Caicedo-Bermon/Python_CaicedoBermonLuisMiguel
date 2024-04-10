#1. Al inicio, el programa dará la bienvenida y explicará la naturaleza de 
#la Secuencia de Fibonacci, donde solicitará al usuario ingresar un valor entero "n", 
#representando hasta qué término de la secuencia se generará. Aquí mostrará la secuencia
# de Fibonacci hasta el enésimo término ingresado por el usuario. Luego, preguntará si el
# usuario desea continuar o salir, donde si se decide salir,
# el programa se detendrá; de lo contrario, se repetirá el proceso.

fibo = int(input("ingresa un numero para la serie de fibonacci\n"))

a=0
b=1
ver = True
while ver == True:
    