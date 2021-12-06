

def main():
    #Variable usada para enviar la informacion a subCampeon
    contenedorCampeon = []
    #variable usada para almacenar datos a contenendor campeon
    datoCampeon = 0


    def subCampeon(puntajes):
        campeon = 0
        subcampeon = 0
        for n in puntajes:
            if n>campeon:
                subcampeon = campeon
                campeon = n
            elif n<campeon and n>subcampeon:
                subcampeon = n
        return subcampeon




    def modificarLetra(index,palabra,palabraCambia):
        """Funcion que permite el cambio en una cadena de texto mediante el ingreso de un string, indice y la pabra a cambiar"""
        palabra = list(palabra)
        palabra[index] = palabraCambia
        print("".join(palabra))    

    while True:
        print("Por favor, ingresa el numero del ejercicio a solicitar:\
         \n1-Funcion que cambia todos los espacios por guiones\
         \n2-Funcion que cambia las Mayusculas por Minusculas\
         \n3-Funcion que cambia la letra en un texto\
         \n4-Funcion que recibe un texto con nombre y apellido y devuelve un texto con el nombre y apellido pero con capitalizacion\
         \n5-Funcion que recibe un conjuto de numeros,los cuales representan la puntuacion de un concurso, y esta devuelve la puntuacion del subcampeon")
        
        while True:
            try:            
                buscador = int(input("Ingresa aca: "))
                if(buscador < 1 or buscador > 5):
                    print("Por favor, ingresa un numero en el margen indicado")
                    continue
                else:
                    break
            except ValueError:
                print("Por favor, ingresa un dato numerico")
                continue
        if(buscador == 4):
            while True:
                    while datoCampeon != 2:
                        try:                                 #Recordar arreglar el pronombre
                            datoCampeon = int(input(f"Ingrese la {len(contenedorCampeon)+1} calificacion: "))
                            while True:
                                    contenedorCampeon.append(int(datoCampeon))
                                    print("\nQue deseas hacer ahora?\
                                                            \n1-Eliminar la calificacion ingresada\
                                                            \n2-Dejar de ingresar calificaciones\
                                                            \n3-Continuar ingresando ")
                                    datoCampeon = int(input("Ingresa aca: "))
                                    if(datoCampeon == 1 ):
                                        if(contenedorCampeon == 0):
                                            print("\nLa lista esta vacia, ya no se pueden eliminar calificaciones")
                                        else:
                                            print(f"Eliminado: {contenedorCampeon[-1]}")
                                            contenedorCampeon.pop()
                                        continue
                                    elif(datoCampeon == 2 or datoCampeon == 3):
                                        break
                                    else:
                                        print("Ingresa una opcion valida")
                                        continue
                        except ValueError:
                            print("Por favor, ingresa datos numericos")
                            continue
                    print(f"las calificaciones son: {contenedorCampeon}")
                    print(f"El subcampeon es: {subCampeon(contenedorCampeon)}\n")
                    break
        break
            

main()