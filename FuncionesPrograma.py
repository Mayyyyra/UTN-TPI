from funciones import *

def Crear_Pais(Lista):
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
        Continente = Es_Texto("Continente del pais (o escriba - para salir):")
        Limpiar_Consola()
        if Continente == "-":
            return None
        pais_Dic = {"Pais":Titulo,"Poblacion":Poblacion,"Superficie":Superficie,"Continente":Continente}
        for llave,valor in pais_Dic.items():
            print(f"{llave} - {valor}")
        Pausar()
        Limpiar_Consola()
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
        Pausar()
        Limpiar_Consola()