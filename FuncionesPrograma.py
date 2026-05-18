from funciones import *
def Crear_Pais(Lista):
    while True:
        Titulo = Es_Nombre("Nombre del nuevo pais (o escriba - para salir):",Lista)
        if Titulo == "-":
            return None
        Poblacion = Es_Numerico("Poblacion del pais (o escriba - para salir):")
        if Poblacion == "-":
            return None
        Superficie = Es_Numerico("Superficie del pais (o escriba - para salir):")
        if Superficie == "-":
            return None
        Continente = Es_Texto("Continente del pais (o escriba - para salir):")
        if Continente == "-":
            return None
        pais_Dic = {"Pais":Titulo,"Poblacion":Poblacion,"Superficie":Superficie,"Continente":Continente}
        return pais_Dic
def Recuperar_Informacion(Datos,ListaFinal):
        next(Datos)
        for line in Datos: #por cada linea en el archivo de datos se guarda un diccionario con la informacion del pais, esto para hacer mas facil el manejo
            Data = line.strip().split(",")
            paises = {}
            paises = {"Pais":Data[0],"Poblacion":Data[1],"Superficie":Data[2],"Continente":Data[3]}
            ListaFinal.append(paises)
def Buscar_Pais(Lista):
    encontrado = False
    Buscar = Es_Texto("Nombre del pais a buscar:")
    for i in Lista:
        if Buscar == i["Pais"]:
            encontrado = True
            return i
    if encontrado == False:
        print("no pudimos encontrar dicho pais")
def Menu_de_cambios(Pais,Lista):
    while True:
        print("======================================")
        print("1.Cambiar Nombre\n" \
        "2.Cambiar poblacion\n" \
        "3.Cambiar Superficie\n" \
        "4.Cambiar Continente\n" \
        "5.Regresar")
        opcion = input("que deseas cambiar:")
        match opcion:
            case "1":
                nuevo_nombre = Es_Nombre("Nombre del pais (o escriba - para salir):",Lista)
                if nuevo_nombre == "-":
                    break
                else:
                    Pais["Pais"] = nuevo_nombre
                    break
            case "2":
                nueva_poblacion = Es_Numerico("Cantidad de poblacion (o escriba - para salir):")
                if nueva_poblacion == "-":
                    break
                else:
                    Pais["Poblacion"] = nueva_poblacion
                    break
            case "3":
                Es_Superficie = Es_Numerico("Tamaño de la superficie (o escriba - para salir):")
                if Es_Superficie == "-":
                    break
                else:
                    Pais["Superficie"] = Es_Superficie
                    break
            case "4":
                Es_Continente = Es_Texto("Nombre del continente (o escriba - para salir):")
                if Es_Continente == "-":
                    break
                else:
                    Pais["Continente"] = Es_Continente
                    break
            case "5":
                break