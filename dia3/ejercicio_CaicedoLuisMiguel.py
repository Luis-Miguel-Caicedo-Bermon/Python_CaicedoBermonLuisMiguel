#
#1. Crear una función que determina si un número dado por el usuario es primo. Un número primo es aquel que solo es divisible por 1 y por sí mismo.
# El programa proporciona un menú interactivo que permite al usuario ingresar números para ser verificados como primos. Además, se incluye la opción
# de detener el proceso cuando el usuario lo desee.


#Al inicio, el programa dará la bienvenida y explicará el propósito del aplicativo: verificar si un número dado es primo o no.
#Se presentará un menú con opciones numeradas para que el usuario pueda elegir entre verificar un número, detener el programa u obtener información adicional.
#Si elige verificar un número, se le solicitará ingresar el número deseado.
#La función verificará si el número es primo y proporcionará un mensaje claro indicando el resultado.
#Después de cada verificación, se volverá al menú para permitir al usuario realizar más acciones.
#Si elige detener el programa, se le despedirá y el programa se cerrará.
#Si elige obtener información adicional debe arrojar una explicación de los números primos y el nombre del autor del aplicativo.


def numpri():#se hace una funcion
    cerrar=True
    while cerrar==True:
        print("---------------------menú-----------------------\n"#se muestran las opciones
            "1 programa para saber si un numero es primo o no\n"
            "2 finalizar programa\n"
            "3 explicacion sobre los numeros primos")
        me=int(input("escoje una opcion\n"))#se le pide al usuario seleccionar una opcion
        if me==1:#si escoje la opcion 1 se hace el proceso de los numeros primos
            a=0
            num=int(input("ingresa el numero que deseas verificar si es primo o no\n"))#se le pide al usuario el numero
            for i in range(1,num):#empieza desde hasta el numero pedido
                if num%i == 0:#si el residuo de la division es igual a cero
                    a=a+1#se va sumando uno al contador
            if a==1:#si el contador es igual a 1 significa que el numero es primo
                print("el numero es primo")
            else:#si se agrega mas de un numero al contador el numero no es primo
                print("el numero no es primo")
        if me==2:#si se escoje la opcion 2
            print("gracias pr utilizar el programa")
            cerrar=False#cerrar pasa a ser falso y se termina el programa
        if me==3:#si se escoje la opcion 3 se da la siguiente informacion
            print("Los números primos son aquellos que solo tienen dos divisores:\n"
                  "ellos mismos y 1. Por ejemplo, 2, 3, 5 y 7\n"
                  "son números primos porque solo pueden dividirse entre 1\n"
                  " y ellos mismos sin dejar residuo.\n"
                  "")
            print("NOMBRE DEL AUTOR:")
            print("Caicedo Bermon Luis Miguel")
numpri()

#DESARROLLADO POR: Caicedo Bermon Luis Miguel c.c: 1090381345