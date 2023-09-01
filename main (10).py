import random

datosPerros = {
    "nombre": [],
    "huellaDactilar": []
}
fotosPoliPerros = {
    "FOTO": []
}
datosDueños = {
    "Nombre": [],
    "Apellido": [],
    "facultad": [],
    "cedula": []

}

tipoA = 0


def menu():
    print("----------------POLIPERROS----------------")
    print("---------------BIEN VENIDOS----------------")
    print("\nIngrese una opcion: ")
    print("1) Regitrar perros y dueños")
    print("2) Mostrar Perros ")
    print("3) Registrar foto ")
    print("4) Mostrar dueños  ")
    print("5) Salir ")
    tipoA = int(input("Ingrese la opcion: "))
    return tipoA


# ----------------------------------------------------------
tipoA= menu()
while tipoA != 5:
    if tipoA == 1:
        print("Caso 1")  # registra el numero de perros y los datos
        nPerros = int(input("Ingrese el numero de perros:"))
        for i in range(nPerros):
            print("_"*40)
            print("\nIngresa los datos del poliperro: ", i + 1)
            nombre = input("Nombre: ")
            huellaDactilar = input("Huella: ")
            datosPerros['nombre'].append(nombre)
            datosPerros['huellaDactilar'].append(huellaDactilar)
            print("_" * 45)
            print("\nIngrese los datos del dueño del perro ", i + 1)
            nombreD = input("\nNombre del Dueño: ")
            apellidoD = input("Apellido del Dueño: ")
            facultadD = input("Facultad a la que pertenece: ")
            cedulaD = int(input("Ingrese la cédula: "))
            datosDueños['Nombre'].append(nombreD)
            datosDueños['Apellido'].append(apellidoD)
            datosDueños['facultad'].append(facultadD)
            datosDueños['cedula'].append(cedulaD)

        tipoA = menu()

    elif tipoA == 2:
        print("Caso 2")  # Imprime los datos ingresados
        for i in range(nPerros):
          print("_" * 40)
          print("Mostrar datos del poliperro", i + 1)
          print("* Nombre ", datosPerros['nombre'][i])
          print("* Huella ", datosPerros['huellaDactilar'][i])
          print("_" * 40)
            
          if "FOTO" in datosPerros:
            print("* Foto", datosPerros['FOTO'][i])
          tipoA = menu()

    elif tipoA == 3:
        print("Caso 3")
        for i in range(nPerros):
            print("Ingrese la foto del poliperro")
            print("El polipeero dispone de una foto??")
            foto = input("Ingrese si o no: ")
            if foto == "si":
                foto = input("Foto: ")
                fotosPoliPerros['FOTO'].append(foto)
            else:
                fotosPoliPerros['FOTO'].append("foto-prieba.png")

        datosPerros.update(fotosPoliPerros)
        tipoA = menu()

    elif tipoA == 4:
      print("Registros")
      for i in range(nPerros):
        print("_"*45)
        print("Mostrar datos del Dueño",i+1)
        print("* Datos Dueño: ",datosDueños['Nombre'][i],datosDueños['Apellido'][i])
        print("* Su Perro es: ",datosPerros['nombre'][i])
      tipoA = menu()

    elif tipoA == 5:
      print("GRACIAS")


#Notificacione
#modulo del dueño