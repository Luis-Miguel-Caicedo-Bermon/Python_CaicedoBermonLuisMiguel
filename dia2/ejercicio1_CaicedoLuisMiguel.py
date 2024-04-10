#1. Al inicio, el programa dará la bienvenida y explicará la naturaleza de 
#la Secuencia de Fibonacci, donde solicitará al usuario ingresar un valor entero "n", 
#representando hasta qué término de la secuencia se generará. Aquí mostrará la secuencia
# de Fibonacci hasta el enésimo término ingresado por el usuario. Luego, preguntará si el
# usuario desea continuar o salir, donde si se decide salir,
# el programa se detendrá; de lo contrario, se repetirá el proceso.

print("la sucesion de fibonacci se trata de una serie infinita de numeros naturales que empieza con un 0 y un uno y continua añadiendo numeros que son la suma de los dos anteriores")
ver = True
while ver == True:#mientras ver sea verdadero va a continuar el programa
    fibo = int(input("ingresa un numero para la serie de fibonacci\n"))# se pide el numero para la serie
    a=0 
    b=1
    for i in range(0, fibo):#hace el proceso la cantidadde veses que pida el usuario
        if a>999999999:#si a es mayor a ese numero no se va a seguir imprimiendo a
            continue
        else:
            print(a)
            c=a+b
            a=b
            b=c#se va haciendo la suma hasta escribir la cantidad de numeros que quiere e usuario
    sino = input("quieres continuar con el programa? si o no\n")#se le pide una respuesta al usuario
    if sino == "no":# si la respuesta es no  ver se volvera falso y por lo tanto se acaba el programa
         print("programa finalizado")
         ver=False

# DESARROLLADO POR: Caicedo Bermon Luis Miguel c.c: 1090381345