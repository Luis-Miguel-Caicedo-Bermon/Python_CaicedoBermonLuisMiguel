#5.1 Cambio de moneda
#Problema del cambio de dinero
#Calcula el número mínimo de monedas necesarias para cambiar el valor dado en monedas de denominaciones 1, 5 y 10.
#Entrada: Dinero entero.
#Salida: El número mínimo

#3de monedas con denominaciones 1, 5
#y 10 que cambia el dinero.
#¢1
#¢5
#¢10
#En este problema, implementará un sencillo algoritmo codicioso utilizado por los cajeros de todo el mundo.
# Suponemos que un cajero tiene un número ilimitado de monedas de cada denominación.
#Formato de entrada. Dinero entero.
#Formato de salida. El número mínimo de monedas con denominaciones 1, 5, 10 que cambia el dinero.
#Restricciones. 1 < dinero ≤ 103.
#Ejemplo 1.
#Entrada:
#2
#Output:
#2
#2=1+1.
#Muestra 2.
#Entrada:
#28
#Salida: 6
#28 10+10+5+1+1+1.
#=
cont1=0
cont5=0#contadores
cont10=0

uno=1
cinco=5#se les asigna valor
diez=10
print("cambio de monedas")
abrir=True
while abrir==True:
    diner=int(input("cuanto dinero tiene\n"))#pide la cantidad y se le asigna a la variable "diner"
    if diner>0 and diner<1001:#si el numero cumprle los parametros sigue con la operacion
        abrir=False
    if diner<1 or diner>1000:#si es mayor que 1000 o nenor que 1 no cumple con los parametros y se repite la pregunta
        print("ingreseun numero mayor a 1 y mernor que 1000")
if diner>9:#si la cantidad de de diner es mayor a a 9 hace la siguiente operacion
    for i in range(9, diner, 10):#comienza desde el puesto 9 hasta diner con paso 10
        print(diez)
        cont10=cont10+1#es un cotador para que cada vez que diner sea mayor o =10 va sumando una moneda
        diner=diner-10#se le va restando 10 a diner para la siguielte operacion
if diner<10:#si el resultado anterior es menor a diez
    for i in range(4, diner, 5):#cominza desde el puesto 4 hasta diner con paso 5
        print(cinco)
        cont5=cont5+1#es un contador para sumar una moneda cada ves que se cumplka la condicion
        diner=diner-5#se le va restando 5 a diner para la siguielte operacion
if diner<5:#si diner es menor que 5
    for i in range(0, diner, 1):#empieza desde la posicion 0 hasta diner con paso 1
        print(uno)
        cont1=cont1+1#es un contador para saber cuantas monedas van sulo se suma si se cumple la condicion
if cont10>0:#si el contador de monedas de 10 es mayor a 0
    print("nesesitas",cont10,"monedas de 10")#se imprime la cantidad de monedas
if cont5>0:#si el contador de monedas de 5 es mayor a 0
    print("nesesitas",cont5,"monedas de 5")#se imprime la cantidad de monedas
if cont1>0:#si el contador de monedas de 1 es mayor a 0
    print("nesesitas",cont1,"monedas de 1")#se imprime la cantidad de monedas
    