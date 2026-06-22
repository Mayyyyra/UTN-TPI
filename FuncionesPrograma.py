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
        try:
            promedioPob = sum(poblacion)/len(poblacion)
        except ZeroDivisionError:
            print("No es posible realizar el calculo de la poblacion")
        try:
            PromedioSup = sum(Superficie)/len(Superficie)
        except ZeroDivisionError:
            print("No es posible realizar el calculo de la poblacion")
    print(f"el promedio de poblacion entre todos los paises es {promedioPob}")
    print(f"el promedio de superficie entre todos los paises es {PromedioSup} km²")
    print(f"Continentes en America {America}")
    print(f"Continentes en Europa {Europa}")
    print(f"Continentes en Asia {Asia}")
    print(f"Continentes en Africa {Africa}")
    print(f"Continentes en Oceania {Oceania}")
    print(f"el pais con mayor poblacion es {mayor_pais_nom} con {mayor_pais_pob} habitantes")
    Pausar()
def filtrar_paises(lista_paises):
    """Menú secundario para filtrar el dataset bajo diferentes criterios."""
    if not lista_paises:
        print("No hay datos cargados para filtrar.")
        return
    print("\n--- OPCIONES DE FILTRADO ---")
    opcion = questionary.select(message="Seleccioná:",choices=[
    "Por Continente","Por Rango de Población", "Por Rango de Superficie"]).ask()
    resultados = []
    if opcion == "Por Continente":
        Continente = Es_Continente().lower()
        for p in lista_paises:
            if p["Continente"].lower() == Continente:
                resultados.append(p)

    elif opcion == "Por Rango de Población":
        min_pob = Es_Numerico("Ingrese población mínima: ")
        max_pob = Es_Numerico("Ingrese población máxima: ")
        for p in lista_paises:
            if min_pob <= p["Poblacion"] <= max_pob:
                resultados.append(p)

    elif opcion == "Por Rango de Superficie":
        min_sup = Es_Numerico("Ingrese superficie mínima (km²): ")
        max_sup = Es_Numerico("Ingrese superficie máxima (km²): ")
        for p in lista_paises:
            if min_sup <= p["Superficie"] <= max_sup:
                resultados.append(p)
    else:
        print("Opción inválida.")
        return

    if resultados:
        print(f"\nSe encontraron {len(resultados)} registros:")
        for p in resultados:
            print(f"- {p['Pais']} ({p['Continente']}) | Pob: {p['Poblacion']} | Sup: {p['Superficie']} km²")
    else:
        print("Ningún país cumple con los criterios ingresados.")
    Pausar()
def ordenar_paises(lista_paises):
    """Ordena la lista utilizando el método de ordenamiento Burbuja (Bubble Sort)."""
    if not lista_paises:
        print("No hay datos para ordenar.")
        return

    print("\n--- ORDENAR PAÍSES ---")
    # print("Criterios: 1. Nombre | 2. Población | 3. Superficie")
    # criterio_opc = input("Seleccione criterio (1-3): ")
    clave = questionary.select(message="Seleccioná:",choices=["Pais","Poblacion","Superficie"]).ask()
    print("Sentido: 1. Ascendente | 2. Descendente")
    sentido_opc = input("Seleccione sentido (1-2): ")

    descendente = (sentido_opc == "2")

    
    lista_ordenada = list(lista_paises)
    n = len(lista_ordenada)

    
    for i in range(n):
        for j in range(0, n - i - 1):
            val1 = lista_ordenada[j][clave]
            val2 = lista_ordenada[j + 1][clave]
            
            
            if isinstance(val1, str):
                val1 = val1.lower()
                val2 = val2.lower()

            condicion = val1 > val2 if not descendente else val1 < val2
            
            if condicion:
                
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]

    print("\n--- LISTA ORDENADA ---")
    for p in lista_ordenada:
        print(f"- {p['Pais']} | Pob: {p['Poblacion']} | Sup: {p['Superficie']} km² | Continente: {p['Continente']}")
    Pausar()
