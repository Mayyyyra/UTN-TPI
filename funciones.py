from Errores import *
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