ver=True
while ver == True:
    numlis=int(input("cuantos numeros tiene tu lista\n"))
    if numlis<300 and numlis>0:
        ver = False
    if numlis>=300 or numlis<1:
        print("la lista no puede tener mas de 300 numeros o menos de uno")
num= []
for i in range(numlis):
    numero=int(input())
    num.append(numero)

num.sort()
num=set(num)

print(num)
#DESARROLLADO POR: Caicedo Bermon Luis Miguel c.c: 1090381345