import csv
from FuncionesPrograma import *
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
    print(
        "1.Agregar un pais\n" \
        "2.Actualizar un pais\n" \
        "3.Buscar un pais\n" \
        "4.Filtrar Pais por tipo\n" \
        "5.Ordenar paises\n" \
        "6.Mostrar Estadisticas\n" \
        "7.Salir"
        )
    opcion = input("que desea realizar:")
    match opcion:
        case "1":
            Pais = Crear_Pais(paises_lista)
            if Pais != None:
                Editor_Diccionarios.writerow(Pais)
                paises_lista.append(Pais)
        case "2": #nota: esto actualiza los diccionarios pero no el csv
            Pais_Buscar = Buscar_Pais(paises_lista)
            if Pais_Buscar != None:
                Menu_de_cambios(Pais_Buscar,paises_lista)
                with open("DatosPaises.csv", "w", newline="", encoding="utf-8") as Datos:
                    Columnas = ["Pais","Poblacion","Superficie","Continente"]
                    Editor_Diccionarios = csv.DictWriter(Datos, fieldnames=Columnas)
                    Editor_Diccionarios.writeheader()
                    Editor_Diccionarios.writerows(paises_lista)
                    print("Pais actualizado")
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("saliendo")
            Datos.close()
            break
        case _:
            print("opcio no disponible")
            for i in range(1,len(paises_lista),1): #esto esta solo para ver, despues lo elimino
                print(f"{i}-{paises_lista[i]}")
