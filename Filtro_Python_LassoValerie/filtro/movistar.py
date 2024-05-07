import json
with open("usuario.json","r")as openfile:
    miJosn= json.load(openfile)

print("---MODULO DE USUARIOS---")
print("Administrador")
opcion= int(input("1. Registro y Gestión de Usuarios\n2. Seguimiento del Historial de Usuarios\n3. Personalización de Servicios\n4. Gestión de la Fidelización de Clientes\n"))

if opcion==1:
    print("---Registro y Gestión de Usuarios---")
    print("1. Nuevo usuario\n2. Ver datos del usuario\n3. Actualizar datos del usuario\n4. Eliminar usuarios")
    OpcionGestion= int(input("\nIngresa el número de la opción que deseas:\n"))

    if OpcionGestion==1:
        print("---Nuevo usuario---")

        nombreUsurio= input("\nNombre del nuevo usurio: ")
        apellidoUsuario= input("\nApellido del nuevo usuario: ")
        idUsuario= input("\nID  del usuario: ")
        direccionUsuario= input("\nDirección del usuario: ")
        NcelularUsuario= input("\nNúmero telefonico :")
        categoria= input("\nCategoría: ")

        nuevoUsuario= [
            {
                "nombre": nombreUsurio,
                "apellido": apellidoUsuario,
                "id": idUsuario,
                "direccion": direccionUsuario,
                "celular": NcelularUsuario,
                "categoria": categoria
            }
        ]

        nuevo= [
            {
                "usuario": [

                ]
            }
        ]

        nuevo += [nuevoUsuario]
        with open("usuario.json","w")as openfile:
            miJosn= (nuevo, openfile)
    
    if OpcionGestion==2:

        print("---Ver datos del usuario---\n")
        print("id de los usuarios\n")

        for i in miJosn:
            for x in i["nuevos"]:
                print(x["id"],x["nombre"])
        idUsu= input("\nIngrese el id del usuario que deseas ver\n")

        for i in miJosn:
            for x in i["nuevos"]:
                if x["id"]==idUsu:
                    print("\n---Datos del usuario---\n")
                    print(x["nombre"])
                    print(x["apellido"])
                    print(x["id"])
                    print(x["direccion"])
                    print(x["celular"])
                    print(x["categoria"])
                    
                
    if OpcionGestion==3:

        print("Actualizar datos del usuario\n")

        for i in miJosn:
            for x in i["nuevos"]:
                print(x["id"],x["nombre"])

        crear=int(input("\nIngrese el id del usuario que deseas actualizar\n"))

        for i in miJosn:
            for x in i["nuevos"]:
                if x["id"]==crear:
                    print(x["nombre"])
                    print("\n---Datos actualizar---\n")
                    datoac=input ("Nombre: ")
                    datoac=miJosn
                    miJosn +=({"nombre": datoac})

    if OpcionGestion==4:
        print("Eliminar datos del usuario")

        for i in miJosn:
            for x in i["nuevos"]:
                print(x["id"],x["nombre"])

        idUsu= input("\nIngrese el id del usuario que deseas eliminar\n")

        for i in miJosn:
            for x in i["nuevos"]:
                if x["id"]==idUsu:
                    del [x["nombre"]]
if opcion==2:
    print("\n---Seguimiento del Historial de Usuarios---\n")
    for i in miJosn:
        for x in i["nuevos"]:
            print(x["id"],x["nombre"])

    crear=int(input("\nIngrese el id del usuario que deseas actualizar\n"))

    for i in miJosn:
        for x in i["nuevos"]:
            if x["id"]==crear:
                print(x["nombre"])

if opcion==3:
    print("\n---Personalización de Servicios---\n")
    print("1. Internet de Fibra Óptica\n2. planes pospago\n3. planes prepago")

if opcion==4:
    print("\n---Gestión de la Fidelización de Clientes---\n") 
    print("Los clientes leales son los que llevan 10 años en la empresa")
    for i in miJosn:
        for x in i["nuevos"]:
            if x["categoria"]==["clientes leales"]:
                print(x["nombre"], x["categoria"])
#valerie
        
