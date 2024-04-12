def contra():
    
    import random
    abrir=True
    while abrir==True:
        print("------------BIENVENIDO-----------------\n"
        "generador de contraseñas seguras\n"
        "---------menú de opciones-------\n"
        "1 longitud de la contaseña\n"
        "2 incluir mayusculas\n"
        "3 inculuir minusculas\n"
        "4 caracteres alfanumericos y símbolos\n"
        "5 mostrar la contraseña creada\n"
        "6 salir")
        opc=int(input("seleccione una opcion\n"))
        if opc==1:
            nudi=int(input("cuantos caracteres desea que tenga la contraseña\n"))
        if opc==2:
            may=input("quieres incluir mayusculas si o no?\n")
            if may=="si":
                mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            else:
                if may=="no":
                    mayus=""
        if opc==3:
            min=input("quieres incluir minusculas si o no?\n")
            if min=="si":
                minus = "abcdefghijklmnopqrstuvwxyz"
            else:
                if min=="no":
                    minus = ""
        if opc==4:
            sin=input("quiers incluir caracteres alfanumericos y símbolos si o no?\n")
            if sin=="si":
                simbo = "123456789!@#$%()-=+,./"
            else:
                if sin=="no":
                    simbo = ""
        if opc==5:
            todo = mayus+minus+simbo
            con=random.sample(todo, nudi)
            contraseña="".join(con)
            print(contraseña)
        if opc==6:
            print("gracias por utilizar el programa")
            abrir=False
contra()

#DESARROLLADO POR: Caicedo Bermon Luis Miguel c.c: 1090381345