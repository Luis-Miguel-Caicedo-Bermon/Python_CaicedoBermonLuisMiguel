lis= input()
lista=[int(i) for i in lis.split()]#se pide una lista de numeros separando los numeros por espacios
print(lista)#se muestra la lista al usuario aunque es algo innesesario

suma=int(input())#se le pide al usuario la suma

a=0#es un contador
for i in range(len(lista)):#comienza desde el primer numero de la lista hasta el ultimo
    z=i+1#es para que el siguiente numero a analizar no sea el mismo que el primero
    for z in range(z,len(lista)):#entonces empieza desde el segundo
        su=lista[i]+lista[z]#se suma el primer numero con el que le sigue para comprobar si da el resultado que se quiere
        if a==0:#si el contador es igual a 0 se va a realizar lo siguiente
            if su==suma:#si el resultado de la suma anterior es igual a el numero que da el usuario
                print(i,z)#se van a imprimir el numero de puesto en el que estaban los numeros
                a=a+1#se le suma 1 al contador por si hay otro resultado posible ya no lo imprima
            

#DESARROLLADO POR: Caicedo Bermon Luis Miguel c.c: 1090381345