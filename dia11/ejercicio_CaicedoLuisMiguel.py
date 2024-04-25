import json
with open("dia11/large-file.json", encoding="utf-8") as file:
    datos=json.load(file)
eventos=[]#se guarda la lista de eventos

CreateEvent=[]
PushEvent=[]
WatchEvent=[]
ReleaseEvent=[]
PullRequestEvent=[]
IssuesEvent=[]     #se almacenan los datos en sus respectivos eventos
ForkEvent=[]
GollumEvent=[]
IssueCommentEvent=[]
DeleteEvent=[]
PullRequestReviewCommentEvent=[]
CommitCommentEvent=[]
MemberEvent=[]
PublicEvent=[]

def eventitos():
    for i in range(len(datos)):
        if datos[i]["type"]=="CreateEvent":
            CreateEvent.append(datos[i])

        if datos[i]["type"]=="PushEvent":
            PushEvent.append(datos[i])

        if datos[i]["type"]=="WatchEvent":
            WatchEvent.append(datos[i])

        if datos[i]["type"]=="ReleaseEvent":
            ReleaseEvent.append(datos[i])

        if datos[i]["type"]=="PullRequestEvent":  #todo esto es almacenar los datos en sus respectivos eventos
            PullRequestEvent.append(datos[i])

        if datos[i]["type"]=="IssuesEvent":
            IssuesEvent.append(datos[i])

        if datos[i]["type"]=="ForkEvent":
            ForkEvent.append(datos[i])

        if datos[i]["type"]=="GollumEvent":
            GollumEvent.append(datos[i])

        if datos[i]["type"]=="IssueCommentEvent":
            IssueCommentEvent.append(datos[i])

        if datos[i]["type"]=="DeleteEvent":
            DeleteEvent.append(datos[i])

        if datos[i]["type"]=="PullRequestReviewCommentEvent":
            PullRequestReviewCommentEvent.append(datos[i])

        if datos[i]["type"]=="CommitCommentEvent":
            CommitCommentEvent.append(datos[i])

        if datos[i]["type"]=="MemberEvent":
            MemberEvent.append(datos[i])

        if datos[i]["type"]=="PublicEvent":
            PublicEvent.append(datos[i])


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
        eventitos()
        for i in range(len(eventos)):
            print(eventos[i])#se imprimen los tipos de eventos
        seleccion=input("de que evento quieres ver los datos\n")
        if seleccion=="CreateEvent":
            for i in range(len(CreateEvent)):
                print(CreateEvent[i])          #se imprimen los datos que tengan ese tipo de eventos
            for i in range(len(CreateEvent)-1,-1,-1):
                CreateEvent.pop(i)#y se van borrando los datos para que cuando se vuelvan a almecenar se almacenen los que esten actualizados
        if seleccion=="PushEvent":
            for i in range(len(PushEvent)):
                print(PushEvent[i])
            for i in range(len(PushEvent)-1,-1,-1):
                PushEvent.pop(i)
        if seleccion=="WatchEvent":
            for i in range(len(WatchEvent)):
                print(WatchEvent[i])
            for i in range(len(WatchEvent)-1,-1,-1):
                WatchEvent.pop(i)
        if seleccion=="ReleaseEvent":
            for i in range(len(ReleaseEvent)):
                print(ReleaseEvent[i])
            for i in range(len(ReleaseEvent)-1,-1,-1):
                ReleaseEvent.pop(i)
        if seleccion=="PullRequestEvent":
            for i in range(len(PullRequestEvent)):
                print(PullRequestEvent[i])
            for i in range(len(PullRequestEvent)-1,-1,-1):
                PullRequestEvent.pop(i)
        if seleccion=="IssuesEvent":
            for i in range(len(IssuesEvent)):
                print(IssuesEvent[i])
            for i in range(len(IssuesEvent)-1,-1,-1):
                IssuesEvent.pop(i)
        if seleccion=="ForkEvent":
            for i in range(len(ForkEvent)):
                print(ForkEvent[i])
            for i in range(len(ForkEvent)-1,-1,-1):
                ForkEvent.po(i)
        if seleccion=="GollumEvent":
            for i in range(len(GollumEvent)):
                print(GollumEvent[i])
            for i in range(len(GollumEvent)-1,-1,-1):
                GollumEvent.pop(i)
        if seleccion=="IssueCommentEvent":
            for i in range(len(IssueCommentEvent)):
                print(IssueCommentEvent[i])
            for i in range(len(IssueCommentEvent)-1,-1,-1):
                IssueCommentEvent.pop(i)
        if seleccion=="DeleteEvent":
            for i in range(len(DeleteEvent)):
                print(DeleteEvent[i])
            for i in range(len(DeleteEvent)-1,-1,-1):
                DeleteEvent.pop(i)
        if seleccion=="PullRequestReviewCommentEvent":
            for i in range(len(PullRequestReviewCommentEvent)):
                print(PullRequestReviewCommentEvent[i])
            for i in range(len(PullRequestReviewCommentEvent)-1,-1,-1):
                PullRequestReviewCommentEvent.pop(i)
        if seleccion=="CommitCommentEvent":
            for i in range(len(CommitCommentEvent)):
                print(CommitCommentEvent[i])
            for i in range(len(CommitCommentEvent)-1,-1,-1):
                CommitCommentEvent.pop(i)
        if seleccion=="MemberEvent":
            for i in range(len(MemberEvent)):
                print(MemberEvent[i])
            for i in range(len(MemberEvent)-1,-1,-1):
                MemberEvent.pop(i)
        if seleccion=="PublicEvent":
            for i in range(len(PublicEvent)):
                print(PublicEvent[i])
            for i in range(len(PublicEvent)-1,-1,-1):
                PublicEvent.pop(i)
        
        menu()

    if opc==2:
        nuevo=input("que tipo de envento será\n")
        idevento=input("id del evento\n")
        print("DATOS DEL ACTOR")
        id=input("ID\n")
        login=input("login\n")
        avatar=input("avatar url\n")#se piden los datos para el nuevo evento
        print("REPO")
        idrepo=input("ID\n")
        name=input("nombre\n")
        pub=(input("va a ser publico (si)(no)"))
        if pub=="si":
            public=True
        else:
            public=False
        if nuevo in eventos:#y se agregan solo si el tipo de evento ya existe
            datos.append({"id":idevento, "type":nuevo, "actor":{"id":id, "login":login, "avatar_url":avatar}, "repo":{"id":idrepo, "name":name}, "public":public})
        menu()
    if opc==3:
        idperson=input("ingresa el id del evento al que le quieres actualizar los datos\n")
        for i in range(len(datos)):
            if datos[i]["id"]==idperson:# si el id coincide con alguno en los datos
                comenzar=True
                while comenzar==True:
                    actualizar=int(input("que dato deseas actualizar\n"
                                        "1 actor----2 repo---3 public----4 terminar\n"))
                    if actualizar==1:
                        id=input("ID\n")
                        login=input("login\n")#se piden los nuevos valores
                        avatar=input("avatar_url\n")
                        datos[i]["actor"]["id"]=id
                        datos[i]["actor"]["login"]=login#y se remplasan por los antiguos
                        datos[i]["actor"]["avatar_url"]=avatar

                    if actualizar==2:
                        idperson=input("id\n")#se piden los nuevos valores
                        name=input("nombre\n")
                        datos[i]["repo"]["id"]=idperson
                        datos[i]["repo"]["name"]=name#y se remplasan por los antiguos

                    if actualizar==3:
                        pub=input("va a ser publico (si)(no)\n")#se pide el nuevo valor
                        if pub=="si":
                            public=True
                        else:
                            public=False
                        datos[i]["public"]=public#y se remplaza
                    
                    if actualizar==4:
                        comenzar=False
        menu()

    if opc==4:
        ideliminar=input("ingresa el id del evento que quieres eliminar\n")
        for i in range(len(datos)-1,-1,-1):
            if datos[i]["id"]==ideliminar:#si el id conincide con alguno de los datos
                datos.pop(i)#se elimina todo lo que esté en la poscicion del id
        menu()

    if opc==5:
        print("programa finalizado")
        ver=False

with open("eventos.json","w") as outfile:
    json.dump(datos,outfile)

#DESARROLLADO POR: Caicedo Bermon Luis Miguel c.c: 1090381345