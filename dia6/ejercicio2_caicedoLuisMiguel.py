lis= input()
lista=[int(i) for i in lis.split()]
print(lista)

suma=int(input())


for i in range(len(lista)):
    z=i+1
    for z in range(z,len(lista)):
        su=lista[i]+lista[z]
        if su==suma:
            print(i,z) 