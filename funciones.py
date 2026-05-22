from Errores import *
import questionary
import os
def Limpiar_Consola():
    os.system('cls')
def Es_Numerico(Texto):
    while True:
        Comprobar = input(Texto)
        if Comprobar == "-":
            return Comprobar
        else:
            try:
                if not Comprobar.isnumeric():  
                    raise TypeError
                else:
                    return Comprobar
            except TypeError:
                print("tipo erroneo")
    
def Es_Numerico2(Texto): #este es especifico para flotantes
    while True:
        try:
            Comprobar = input(Texto)
            if Comprobar == "-":
                Limpiar_Consola()
                return Comprobar
            else:
                return float(Comprobar)
        except:
            print("tipo erroneo")
def Verificar_Existencia(Verificar,Lista):
    for i in Lista:
        if i["Pais"] == Verificar:
            return False
    return True
def Es_Texto(Texto):
    while True:
        Comprobar = input(Texto).capitalize()
        if Comprobar == "-":
            return Comprobar
        else:
            try:
                if not Comprobar.isalpha():
                    raise TypeError
                else:
                    return Comprobar
            except TypeError:
                print("tipo erroneo")
def Es_Nombre(Texto,Lista): #funcion especifica para el nombre de los paises, revisa tambien si esta en un dic
    while True:
        Comprobar = input(Texto).capitalize()
        if Comprobar == "-":
            return Comprobar
        else:
            try:
                if not Comprobar.isalpha():
                    raise TypeError
                elif Verificar_Existencia(Comprobar,Lista) == False:
                    raise Nombre_Repetido
                else:
                    return Comprobar
            except Nombre_Repetido:
                print("Dicho pais ya existe")
            except TypeError:
                print("tipo erroneo")
def Pausar():
    input("precione cualquier tecla para continuar")
def Menu():
    opcion = questionary.select(message="Seleccioná:",choices=["Agregar un pais",
    "Actualizar un pais","Buscar un pais", "Filtrar Pais por tipo","Ordenar paises","Mostrar Estadisticas","Salir"]).ask()
    Limpiar_Consola()
    print(f"Elegiste: {opcion}")
    return opcion
def Menu_de_cambios(Pais,Lista):
    while True:
        opcion = questionary.select(message="Seleccioná:",choices=["Cambiar Nombre",
    "Cambiar poblacion","Cambiar Superficie", "Cambiar Continente","Salir"]).ask()
        Limpiar_Consola()
        print(f"Elegiste: {opcion}")
        match opcion:
            case "Cambiar Nombre":
                nuevo_nombre = Es_Nombre("Nombre del pais (o escriba - para salir):",Lista)
                if nuevo_nombre == "-":
                    Limpiar_Consola()
                    break
                else:
                    Pais["Pais"] = nuevo_nombre
                    print("el pais a sido actualizado")
                    Pausar()
                    Limpiar_Consola()
                    break
            case "Cambiar poblacion":
                nueva_poblacion = Es_Numerico("Cantidad de poblacion (o escriba - para salir):")
                if nueva_poblacion == "-":
                    Limpiar_Consola()
                    break
                else:
                    Pais["Poblacion"] = nueva_poblacion
                    print("el pais a sido actualizado")
                    Pausar()
                    Limpiar_Consola()
                    break
            case "Cambiar Superficie":
                Es_Superficie = Es_Numerico("Tamaño de la superficie (o escriba - para salir):")
                if Es_Superficie == "-":
                    Limpiar_Consola()
                    break
                else:
                    Pais["Superficie"] = Es_Superficie
                    print("el pais a sido actualizado")
                    Pausar()
                    Limpiar_Consola()
                    break
            case "Cambiar Continente":
                Es_Continente = Es_Texto("Nombre del continente (o escriba - para salir):")
                if Es_Continente == "-":
                    Limpiar_Consola()
                    break
                else:
                    Pais["Continente"] = Es_Continente
                    print("el pais a sido actualizado")
                    Pausar()
                    Limpiar_Consola()
                    break
            case "Salir":
                break