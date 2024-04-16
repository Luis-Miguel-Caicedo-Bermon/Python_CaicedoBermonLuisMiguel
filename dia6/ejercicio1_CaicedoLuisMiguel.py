#ver=True
#while ver == True:
#    numlis=int(input("cuantos numeros tiene tu lista\n"))
#    if numlis<300 and numlis>0:
#        ver = False
#    if numlis>=300 or numlis<1:
#        print("la lista no puede tener mas de 300 numeros o menos de uno")
nodos= []
for i in range(301):
    numero=(input())
    if numero=="":
        continue
    nodos.append(numero)


norep=set(nodos)

print(norep)

