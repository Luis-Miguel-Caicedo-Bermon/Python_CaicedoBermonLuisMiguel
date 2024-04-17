ver=True
while ver == True:
    numlis=int(input("cuantos numeros tiene tu lista\n"))
    if numlis<300 and numlis>0:#mientras que la cantidad de numeros sea menor a 300 y mayor a 0
        ver = False#ver será falso y seguirá el proceso
    if numlis>=300 or numlis<1:#si no es así se repetirá la pregunta
        print("la lista no puede tener mas de 300 numeros o menos de uno")
num= []#es donde se almacenará la lista
for i in range(numlis):#va desde 0 hasta la cantidad de numeros en la lista
    numero=int(input())#se piden los numeros
    num.append(numero)#y se van agregando a la lista

num.sort()#se ordenan los numeros de la lista de menor a mayor
num=set(num)#esto elimina los numeros repetidos

print(num)#se imprimen los numeros
#DESARROLLADO POR: Caicedo Bermon Luis Miguel c.c: 1090381345