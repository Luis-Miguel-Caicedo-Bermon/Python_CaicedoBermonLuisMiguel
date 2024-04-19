producto=["uvas", "piñas", "papayas", "manzanas", "peras"]
precio=[6000, 8000, 5000, 2500, 1500]#listas de productos
cant=[15, 22, 12, 18, 10]
frutacom=[]
totalcom=[]#lo que compren se agrega aquí
cantcom=[]
def menu():#funcion para mostrar un menú
    print("-----tienda de frutas------\n"
          "1 ver lista de frutas\n"
          "2 comprar frutas\n"
          "3 ver productos comprados\n"
          "4 salir")

menu()
ver=True
while ver == True:
    opc=int(input("\nescoje una opcion\n"))
    if opc==1:
        print("fruta----precio----cantidad")
        for i in range(len(producto)):#i va hasta la cantidad de datos que tiene la lista
            print(i, producto[i], precio[i], cant[i])#se imprimen los productos
        menu()

    if opc==2:
        com=input("que fruta deseas comprar\n")
        for i in range(len(producto)):#i va hasta la cantidad de datos que tiene la lista
            if com==producto[i]:#si el nombre es igual a alguno que hay en la lista
                can=int(input("que cantidad quieres\n"))#se pide la cantidad que quiere
                if can<=cant[i] and can>0:#si la cantidad es menor o igual a la cantidad en stok
                    cant[i]=cant[i]-can#se le resta lo que pidio a la cantidad en stok
                    frutacom.append(producto[i])#se añade el producto a una lista que son las compras que tiene el usuario
                    cantcom.append(can)#se añade a la cantidad de compra
                    totalcom.append(can*precio[i])#se multiplica la cantidad por el precio y el resultado se agrega al total de la compra
        menu()
    
    if opc==3:
        for i in range(len(frutacom)):
            print("fruta---cantidad---precio total")
            print(frutacom[i], cantcom[i], totalcom[i])#se imprimen las compras
        menu()



    if opc==4:
        print("GRACIAS POR USAR EL PROGRAMA ;)")#se despide y termina el programa
        ver=False