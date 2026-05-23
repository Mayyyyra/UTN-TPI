import csv
from FuncionesPrograma import *
from busquedaparcial import *
paises_lista = []
try:
    Datos = open("DatosPaises.csv", "r+",newline="")
    Columnas = ["Pais","Poblacion","Superficie","Continente"]
    Editor_Diccionarios = csv.DictWriter(Datos,Columnas)
    Recuperar_Informacion(Datos,paises_lista)
except FileNotFoundError:
    Datos = open("DatosPaises.csv", "w+",newline="")
    Columnas = ["Pais","Poblacion","Superficie","Continente"]
    Editor_Diccionarios = csv.DictWriter(Datos, Columnas)
    Editor_Diccionarios.writeheader()
except FileExistsError:
    print("no se pudo acceder al archivo")
while True:
    opcion = Menu()
    match opcion:
        case "Agregar un pais":
            Pais = Crear_Pais(paises_lista)
            if Pais != None:
                Editor_Diccionarios.writerow(Pais)
                paises_lista.append(Pais)
        case "Actualizar un pais":
            Pais_Buscar = Buscar_Pais(paises_lista)
            if Pais_Buscar != None:
                Menu_de_cambios(Pais_Buscar,paises_lista)
                with open("DatosPaises.csv", "w", newline="") as Datos:
                    Columnas = ["Pais","Poblacion","Superficie","Continente"]
                    Editor_Diccionarios = csv.DictWriter(Datos, fieldnames=Columnas)
                    Editor_Diccionarios.writeheader()
                    Editor_Diccionarios.writerows(paises_lista)
                    print("Pais actualizado")
        case "Buscar un pais":
            BusquedaParcial(paises_lista)
        case "Filtrar Pais por tipo":
            pass
        case "Ordenar paises":
            pass
        case "Mostrar Estadisticas":
            pass
        case "Salir":
            for i in range(0,len(paises_lista),1): #esto esta solo para ver, despues lo elimino
                print(f"{i}-{paises_lista[i]}")
            print("saliendo")
            Datos.close()
            break