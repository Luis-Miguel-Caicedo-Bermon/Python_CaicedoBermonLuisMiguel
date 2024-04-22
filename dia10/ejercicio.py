lis=input()#se piden los numeros separados por espacios
lista=[int(i) for i in lis.split()]#se transforma en una lista

c=0#un contador
num=int(input())
for i in range(len(lista)):#va hasta el ultimo numero de la lista
    if num==lista[i]:#si e el numero es igual al numero en la posicion i
        print(i)#se imprime la posicion
    if num not in lista:#si el numero no esta en la lista
        if num>lista[i]:#si el numero es mayor al numero en esa posicion
            c=c+1#se suma 1 a contador que va contando las casillas
if num not in lista:
    print(c)#se imprime el valor del contador solo si el numero no está enn la lista