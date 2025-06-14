from random import randint

afiliados = {}

while True:
    print("\n---BIENVENIDO A ISAPRE MÁS VIDA---")
    print("\n1. Grabar afiliado")
    print("2. Buscar afiliado")
    print("3. Imprimir certificado")
    print("4. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        rut = input("RUT: ")
        if rut in afiliados:
            print("RUT ya registrado")
            continue

        nombre = input("Nombre: ")
        apellido = input("Apellido paterno/materno: ")

        try:
            edad = int(input("Edad: "))
            if edad < 18:
                print("Edad debe ser mayor o igual a 18.")
                continue
        except:
            print("Edad inválida. Debe ingresar un número.")
            continue

        estado_civil = input("Estado civil (C/S/V): ").upper()
        genero = input("Género (M/F): ").upper()
        fecha = input("Fecha afiliación (dd-mm-aaaa): ")

        monto = randint(1000, 1500)

        afiliados[rut] = {
            "Nombre": nombre,
            "Apellido": apellido,
            "Edad": edad,
            "Estado Civil": estado_civil,
            "Género": genero,
            "Fecha Afiliación": fecha,
            "Monto Certificado": monto
        }
        print("Afiliado registrado")
    
    elif opcion == "2":
        rut = input("RUT a buscar: ")
        if rut in afiliados:
            print("Nombre:", afiliados[rut]["Nombre"])
            print("Apellido:", afiliados[rut]["Apellido"])
            print("Edad:", afiliados[rut]["Edad"])
            print("Estado Civil:", afiliados[rut]["Estado Civil"])
            print("Género:", afiliados[rut]["Género"])
            print("Fecha Afiliación:", afiliados[rut]["Fecha Afiliación"])
            print("Monto Certificado:", afiliados[rut]["Monto Certificado"])
        else:
            print("Afiliado no encontrado")
    
    elif opcion == "3":
        
    
    elif opcion == "4":
        

    else:
        print("Opción inválida")
