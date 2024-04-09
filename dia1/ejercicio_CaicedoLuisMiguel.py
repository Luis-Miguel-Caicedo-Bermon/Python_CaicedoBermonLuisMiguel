#--------------------------------
#---- DIA 1 CHEAT SHEET PYTHON ------
#--------------------------------

#Imprimir hola mundo
print("Hola mundoooooooooooooo!!!")

#Datos primitivos

#Numero
numerito = 1 #nombreVariable = valor
print(numerito) #imprimir(variable)
print(type(numerito)) #imprimir(tipo(variable))

#Decimal
numeritoDecimal = 1.1
print(numeritoDecimal)
print(type(numeritoDecimal))


#Booleano
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito))

#Cadena de texto
texto = "MI TIBU"
print(texto)
print(type(texto))

#Ingresa por teclado la infomarcion
print("ingresa tu edad")
edad = input()
print(type(edad))
#Conversion de tipos de variable
numerito = float
numerito = 19.8
print(type(numerito))
#Bucles For y While

#bucle for
nombres = ("luis", "miguel", "caicedo", "bermon")
for x in nombres:
    print(x)

#bucle while
i=2
while i < 10:
    print(i)
    i +=2
#Funciones (4 Tipos)

#sin parametros ni retorno
def suma():
    print("ingresa dos numeros para la suma")
    y = int(input())
    x = int(input())
    z = y+x
    print("el resultado de la suma es")
    print(z)

suma()

#con parametros sin retorno
def luis(a):
    print(a+10)
luis(5)

#sin parametros con retorno
def mi():
    resul=5/2
    return resul
resul = mi()
print(resul)

#con parametros y con retorno
def yo(u):
    b = u + 7
    return b
b = yo(9)
print(b)

