from funciones import *
import questionary
def BusquedaParcial(Lista):
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
