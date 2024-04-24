import json
with open("dia11/large-file.json", encoding="utf-8") as file:
    datos=json.load(file)
eventos=[]#se guarda la lista de eventos

for i in range(len(datos)):#va desde 0 hata el ultmo dato
    if datos[i]["type"] not in eventos:#si el tipo de dato no está en evento entoces
        eventos.append(datos[i]["type"])#se almacena en eventos


def menu():#es una funcion para llamar el menú
    print("----------menú----------\n"
          "1 ver lista de eventos\n"
          "2 crear nuevo evento\n"
          "3 actualizar un evento\n"
          "4 eliminar algun evento\n"
          "5 finalizar programa")

menu()

ver=True
while ver==True:
    opc=int(input("selecciona una opcion\n"))
    if opc==1:#si selecciona el 1 se imprimen los tipos de eventos
        print(eventos)
        menu()

    if opc==2:
        nuevo=input("ingresa el nombre del nuevo evento\n")
        dicci={"type":nuevo}#se crea un nuevo diccionario y se le agrega al tipo de evento el nombre que le puso el usuario
        datos.append(dicci)#y el diccionario se agrega al final de la lista
        eventos.append(nuevo)#se agrega el nuevo evento a la lista de eventos

    if opc==3:
        actualizar=input("que evento quieres actualizar\n")
        remplazo=input("ingresa el nuevo nombre\n")
        for i in range(len(datos)):
            if datos[i]["type"]==actualizar:#si el tipo de evento coincide con el que ingresa el usuario
                datos[i]["type"]=remplazo#se remplasa por el nombre qu el usuario quiere

        for i in range(len(eventos)):
            if eventos[i]==actualizar:
                eventos[i]=remplazo#se remplaza el nombre tambien de la lista de eventos
        menu()

    if opc==4:
        eliminar=input("que evento quieres eliminar\n")
        for i in range(len(datos)-1,-1,-1):#va en reversa desde el ultimo dato hasta el primero
            if datos[i]["type"]==eliminar:#si el dato coincide con el que quiere eliminar el usuario
                datos.pop(i)#se eliminan los que tengan ese dato
        eventos.remove(eliminar)#y tambien se elimina de la lista de texto
        menu()

    if opc==5:
        print("programa finalizado")
        ver=False

#DESARROLLADO POR: Caicedo Bermon Luis Miguel c.c: 1090381345