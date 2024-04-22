lis=input()
lista=[int(i) for i in lis.split()]
print(lista)

num=int(input())
for i in range(len(lista)):
    if num==lista[i]:
        print(i)
    if num>lista[i] and num<lista[i+1]:
        print(i+1)
        