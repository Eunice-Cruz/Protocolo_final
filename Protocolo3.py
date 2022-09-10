proto=[]
def main ():
    print ("¡Bienvenido! Este es un programa para crear protocolos\n\
            \n\
            MENÚ:\n\
            \n\
            1. Crear protocolo \n\
            2. Mostrar protocolo \n\
            3. Agregar paso al final del protocolo\n\
            4. Añadir paso en alguna posición indicada \n\
            5. Borrar elemento\n\
            6. Agregar subpaso\n\
            7. Salir")
while True:    
    main ()
    opc= int (input ("Elige una opción para continuar (escribe el número): "))
    if opc==1:
        num=int (input ("Inserte cantidad de pasos: "))
        for _ in range (num):
            pasos = input ("Ingrese el paso: ")
            proto.append(pasos)
        for contador, protos in enumerate(proto, start=1):           
            print(contador, protos)            
    elif opc==2:
        print ("El protocolo es: ")
        for contador, protos in enumerate(proto, start=1):
            print(contador, protos) 
    elif opc==3:
        print ("Se agregara el paso al final del protocolo ")
        pasos = input ("Ingrese el paso: ")
        proto.append(pasos)
        for contador, protos in enumerate(proto, start=1):
            print(contador, protos) 
    elif opc==4:
        print ("Se agregara el paso en la posición indicada: ")
        pasos = input ("Ingrese el paso: ")
        pos = int (input("Escribe la posición del paso (recuerda que la primera posición es 0): "))
        proto.insert(pos,pasos)
        for contador, protos in enumerate(proto, start=1):
            print(contador, protos) 
    elif opc==5:
        for contador, protos in enumerate(proto, start=1):
            print(contador, protos) 
        bor = int (input ("Escribe la posición del paso que deseas borrar (recuerda que la primera posición es 0): "))
        proto.pop(bor)
        print("Se borró ese paso")
        for contador, protos in enumerate(proto, start=1):
            print(contador, protos)
    elif opc==6:
        print ("Se agregará un subpaso: ")
        subpasos = input ("Ingrese el subpaso: ")
        pos = int (input("Escribe la posición del paso(recuerda que la primera posición es 0): "))
        proto.insert(pos,[pasos, subpasos])
        for contador, protos in enumerate(proto, start=1):
            print(contador, protos)        
    elif opc==7:
        print ("Hasta luego :]")
        break
else:
    print ("Esa opción no es válida")
