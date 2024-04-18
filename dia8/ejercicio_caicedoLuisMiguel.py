def menu():
    print("============MENÜ==========\n"
          "1 comprar una suscripcion\n"
          "2 regalar una suscripcion\n"
          "3 agregar dinero a tu cuenta\n"
          "4 ver subscripciones compradas\n"
          "5 finalizar programa")

nombres=[]#aquí se almacenan los nombres
diner=[]#se almacena el dinero

info={}#se almacenan la compras

valsub=50#valor de la subscripcion

menu()#se llama la funcion
c=0#un contador
ver=True
while ver==True:
    opc=int(input("elige una opción\n"))
    if opc==1:
        comnom=input("ingresa tu nombre de usuario\n")
        for i in range(len(nombres)):
            if comnom==nombres[i]:#compara los nombres y si son iguales hace lo siguiente
                años=(input("para qué años quieres comprar la suscripcion\n"
                            "(solo se agregaran los años que esten entre 1990 y 2020)"))
                años=[int(a) for a in años.split()]#pide los años que quiere comprar
                for b in range(len(años)):
                    if años[b]>=1990 and años[b]<=2020:#si se cumplen los parametros 
                        c=c+1#aumenta uno al contadorpara saber si es valida la fecha
                    else:#si la fecha no cumple los parametros
                        años[b]=""#la fecha se elimina
                c=c*valsub#el valor de la sub se multiplica por la cantidad de años validos
                
                if c<=diner[i]:#si el total de la compra es menor o igual al dinero que tiene la cuenta
                    diner[i]=diner[i]-c#se le resta el dinero de la compra al dinero del usuario
                    info[nombres[i]]=[años,c]#y se guardan los datos en info
                c=0
        menu()


    if opc==2:
        comnom=input("ingresa tu nombre de usuario\n")
        otro=input("a que usuario le quieres regalar una subscripcion\n")
        for i in range(len(nombres)):
            if comnom==nombres[i]:
                años=(input("para qué años quieres comprar la suscripcion\n"
                            "(solo se agregaran los años que esten entre 1990 y 2020)"))
                años=[int(a) for a in años.split()]
                for b in range(len(años)):
                    if años[b]>=1990 and años[b]<=2020:
                        c=c+1
                    else:
                        años[b]=""
                c=c*valsub
              
                if c<=diner[i]:
                    diner[i]=diner[i]-c
                    nombres[i]=otro
                    info[nombres[i]]=[años,c]
                c=0
        menu()
    if opc==3:
        nom=input("ingresa tu nombre de usuario\n")
        dineuser=int(input("cuanto dinero quieres añadir a tu cuenta\n"))
        nombres.append(nom)#se añade el nombre al final de la lista
        diner.append(dineuser)#se añade el dinero al final de la lista
        menu()


    if opc==4:
        print(info)
        menu()
    if opc==5:
        print("gracias por utilizar el programa :)")
        ver=False
#DESARROLLADO POR: Caicedo Bermon Luis Miguel c.c: 1090381345