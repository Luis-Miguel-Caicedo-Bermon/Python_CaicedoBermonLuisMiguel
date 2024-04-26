#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

def abrirArchivo():
    miJSON=[]
    with open('dia13/info.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("dia13/info.json","w") as outfile:
        json.dump(miData,outfile)

def menu():
    print("################")
    print("## PLATAFORMA DE GESTION ##")
    print("################")
    print("")
    print("Hola! Por favor escoge alguna de las opciones:\n1.Revisar estudiantes\n2.Modificar estudiante\n3 añadir nuevo estudiante\n4 eliminar estudiante\n5 finalizar programa")



menu()
verdadero=True
while verdadero==True:
    x=int(input("Cual opción escoges:"))
    miInfo=[]
    if(x==1):
        miInfo=abrirArchivo()
        id=int(input("ingresa el id del grupo que quieres ver\n"))
        for z in range(len(miInfo)):
            if miInfo[z]["id"]==id:

                for i in miInfo[z]["estudiantes"]:
                    print("################")
                    print("ID:",i["id"])
                    print("Nombre:",i["nombre"])
                    print("Apellido:",i["apellido"])
                    print("Edad",i["edad"])
                    print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
                    print("Cédula:",i["cedula"])
                    print("E-mail:",i["email"])
                    print("GitHub:",i["github"])
                    print("################")
                    print("")
        menu()
    elif(x==2):
        miInfo=abrirArchivo()
        id=int(input("ingresa el id del grupo que quieres ver\n"))
        for z in range(len(miInfo)):
            if miInfo[z]["id"]==id:

                for i in miInfo[z]["estudiantes"]:
                    print("################")
                    print("ID:",i["id"])
                    print("Nombre:",i["nombre"])
                    print("Apellido:",i["apellido"])
                    print("Edad",i["edad"])
                    print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
                    print("Cédula:",i["cedula"])
                    print("E-mail:",i["email"])
                    print("GitHub:",i["github"])
                    print("################")
                    print("")
                estudiante = int(input("Cual numero de identificacion vas a cambiar?"))
                listo=True
                while listo==True:
                    datoCambiar=int(input("Que te gustaría cambiar del estudiante:\n"
                                        "1 nombre\n"
                                        "2 Apellido:\n"
                                        "3 edad\n"
                                        "4 fecha de nacimiento (DD-MM-AAAA)\n"
                                        "5 Cédula\n"
                                        "6 E-mail\n"
                                        "7 GitHub\n"
                                        "8 teminar\n"))
                    
                    if datoCambiar==1:
                        miInfo[z]["estudiantes"][estudiante-1]["nombre"]=input("ingresa el nuevo nombre: ")
                        guardarArchivo(miInfo)
                        print("Cambio realizado!")
                        
                    if (datoCambiar==2):
                        nuevoApellido = input("Ingresa el nuevo apellido: ")
                        miInfo[z]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
                        guardarArchivo(miInfo)
                        print("Cambio realizado!")

                    if datoCambiar==3:
                        miInfo[z]["estudiantes"][estudiante-1]["edad"]=input("ingresa la nueva edad: ")
                        guardarArchivo(miInfo)
                        print("Cambio realizado!")

                    if datoCambiar==4:
                        miInfo[z]["estudiantes"][estudiante-1]["fechaNacimiento"]=input("ingresa la nueva fecha de Nacimiento: ")
                        guardarArchivo(miInfo)
                        print("Cambio realizado!")

                    if datoCambiar==5:
                        miInfo[z]["estudiantes"][estudiante-1]["cedula"]=input("ingresa el numero de cedula: ")
                        guardarArchivo(miInfo)
                        print("Cambio realizado!")

                    if datoCambiar==6:
                        miInfo[z]["estudiantes"][estudiante-1]["email"]=input("ingresa el nuevo email: ")
                        guardarArchivo(miInfo)
                        print("Cambio realizado!")

                    if datoCambiar==7:
                        miInfo[z]["estudiantes"][estudiante-1]["github"]=input("ingresa el nuevo link de github: ")
                        guardarArchivo(miInfo)
                        print("Cambio realizado!")

                    if datoCambiar==8:
                        listo=False
        menu()
    if x==3:
        miInfo=abrirArchivo()
        print("estos son los grupos que hay")
        for i in range(len(miInfo)):
            print("-----")
            print(miInfo[i]["grupo"])
        pregun=input("a que grupo lo quieres agregar?\n")
        for i in range(len(miInfo)):
            if miInfo[i]["grupo"]==pregun:
                print("ingresa los datos del nuevo estudiante")
                id=int(input("ID\n"))
                nombre=input("nombre\n")
                apellido=input("apellido\n")
                edad=input("edad\n")
                fechaNacimiento=input("fecha de nacimiento\n")
                ceduda=input("cédula\n")
                email=input("email\n")
                github=input("link de GitHub\n")
                miInfo[i]["estudiantes"].append({"id":id, "nombre":nombre, "apellido":apellido, "edad":edad, "fechaNacimiento":fechaNacimiento, "cedula":ceduda, "email":email, "github":github})
                guardarArchivo(miInfo)
    
    if x==4:
        miInfo=abrirArchivo()
        print("estos son los grupos que hay")
        for i in range(len(miInfo)):
            print("-----")
            print(miInfo[i]["grupo"])
        pregun=input("en que grupo se encuentra el estudiante que deseas eliminar?\n")
        for i in range(len(miInfo)):
            if miInfo[i]["grupo"]==pregun:
                ideliminar=int(input("ingresa el id del estudiante\n"))
                for a in range(len(miInfo[i]["estudiantes"])):
                    if miInfo[i]["estudiantes"][a]==ideliminar:
                        del miInfo[i]["estudiantes"][a]
        guardarArchivo(miInfo)               