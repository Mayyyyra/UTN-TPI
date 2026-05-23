from funciones import *

def Crear_Pais(Lista): #Crea un pais, si ningun dato es vacio, lo guarda
    while True:
        Titulo = Es_Nombre("Nombre del nuevo pais (o escriba - para salir):",Lista)
        Limpiar_Consola()
        if Titulo == "-":
            return None
        Poblacion = Es_Numerico("Poblacion del pais (o escriba - para salir):")
        Limpiar_Consola()
        if Poblacion == "-":
            return None
        Superficie = Es_Numerico("Superficie del pais (o escriba - para salir):")
        Limpiar_Consola()
        if Superficie == "-":
            return None
        Continente = Es_Continente()
        Limpiar_Consola()
        if Continente == "Salir":
            return None
        pais_Dic = {"Pais":Titulo,"Poblacion":Poblacion,"Superficie":Superficie,"Continente":Continente}
        for llave,valor in pais_Dic.items():
            print(f"{llave} - {valor}")
        Pausar()
        Limpiar_Consola()
        return pais_Dic
def Recuperar_Informacion(Datos,ListaFinal): #Extrae la informacion del archivo CSV
        next(Datos)
        for line in Datos: #por cada linea en el archivo de datos se guarda un diccionario con la informacion del pais, esto para hacer mas facil el manejo
            Data = line.strip().split(",")
            paises = {}
            paises = {"Pais":Data[0],"Poblacion":Data[1],"Superficie":Data[2],"Continente":Data[3]}
            ListaFinal.append(paises)
def Busqueda_Actualizar(Lista): #Busca a un pais, y lo devuelve
    paises_similares = []
    diccionarios_similares = []
    nombre = Es_Texto("nombre del pais a buscar:").upper()
    for Diccionarios in Lista:
        if nombre in Diccionarios["Pais"].upper():
                pais = Diccionarios["Pais"]
                paises_similares.append(pais)
                diccionarios_similares.append(Diccionarios)
    if len(paises_similares) == 0:
        print("no encontramos paises similates")
        Pausar()
    elif len(paises_similares) == 1:
        print(f"el pais que encontramos es {paises_similares[0]}")
        for dic in diccionarios_similares:
            if paises_similares[0] == dic["Pais"]:
                return dic
        Pausar()
    else:
        opcion = questionary.select(message="Seleccioná:",choices=paises_similares).ask()
        for dic in diccionarios_similares:
            if opcion == dic["Pais"]:
                return dic
        Pausar()
def Busqueda_Pais(Lista):
    paises_similares = []
    diccionarios_similares = []
    nombre = Es_Texto("nombre del pais a buscar:").upper()
    for Diccionarios in Lista:
        if nombre in Diccionarios["Pais"].upper():
                pais = Diccionarios["Pais"]
                paises_similares.append(pais)
                diccionarios_similares.append(Diccionarios)
    if len(paises_similares) == 0:
        print("no encontramos paises similates")
        Pausar()
    elif len(paises_similares) == 1:
        print(f"el pais que encontramos es {paises_similares[0]}")
        for dic in diccionarios_similares:
            if paises_similares[0] == dic["Pais"]:
                for key, value in dic.items():
                    print(f"{key}-{value}")
        Pausar()
    else:
        opcion = questionary.select(message="Seleccioná:",choices=paises_similares).ask()
        for dic in diccionarios_similares:
            if opcion == dic["Pais"]:
                for key, value in dic.items():
                    print(f"{key}-{value}")
        Pausar()
def Mostrar_Estadisticas(Lista):
    poblacion = []
    Superficie = []
    America = 0
    Europa = 0
    Asia = 0
    Africa = 0
    Oceania = 0
    mayor_pais_nom = ""
    mayor_pais_pob = 0
    for dic in Lista:
        poblacion.append(int(dic["Poblacion"]))
        Superficie.append(int(dic["Superficie"]))
        Cont = dic["Continente"]
        if mayor_pais_pob < int(dic["Poblacion"]):
            mayor_pais_pob = int(dic["Poblacion"])
            mayor_pais_nom = dic["Pais"]
        if Cont == "America":
            America += 1
        elif Cont == "Europa":
            Europa += 1
        elif Cont == "Asia":
            Asia += 1
        elif Cont == "Africa":
            Africa += 1
        elif Cont == "Oceania":
            Oceania += 1
    print(f"el promedio de poblacion entre todos los paises es {sum(poblacion)/len(poblacion)}")
    print(f"el promedio de superficie entre todos los paises es {sum(Superficie)/len(Superficie)}")
    print(f"Continentes en America {America}")
    print(f"Continentes en Europa {Europa}")
    print(f"Continentes en Asia {Asia}")
    print(f"Continentes en Africa {Africa}")
    print(f"Continentes en Oceania {Oceania}")
    print(f"el pais con mayor poblacion es {mayor_pais_nom} con {mayor_pais_pob} habitantes")
    Pausar()