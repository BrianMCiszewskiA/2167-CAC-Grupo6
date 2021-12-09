from subcampeon import subCampeon
from modificarletra import modificarLetra



"""
1 - Dado un string, escribir una funcion que cambie todos los espacios por guiones.

2- Cambiar Mayusculas por Minusculas. (Ejemplo: "Hola Mundo" -> "hOLA mUNDO"). Tiene como limite 100 caracteres.

3- Los strings son inmutables, escribir una funcion que reciba un string, un indice y una letra a modificar de ese string y que devuelve el string modificado.

4- Escribir una funcion que reciba un string con nombre y apellido y devuelva un string con el nombre y apellido pero con capitalizacion(primera letra mayuscula).

5- Escribir una funcion que reciba N numeros, los cuales representan la puntuacion de un concurso, y esta devuelve la puntuacion del subcampeon. (ejemplo de ingreso de datos... [2,6,10,10,7,5,6], debe devolver 7)

Extra: a- Escribir una funcion que recibe un numero entero y imprima por salida estandar(usando print) un triangulo de numeros de altura igual al numero ingresado. Ej. Si se ingresa el numero 5, debe imprimir:"""



def main():
    #usamos buscador para seleccionar el ejercicio
    #datoGeneral para tener control de opciones de cada ejercicio
    #contenedorCampeon para almacenar los datos del ejercicio 5
    buscador = 6
    datoGeneral = 1
    contenedorCampeon = []
    opciones = ["Por favor, ingresa el numero del ejercicio a solicitar:","1-Funcion que cambia todos los espacios por guiones","2-Funcion que cambia las Mayusculas por Minusculas","2-Funcion que cambia las Mayusculas por Minusculas","3-Funcion que cambia la letra en un texto","4-Funcion que recibe un texto con nombre y apellido y devuelve un texto con el nombre y apellido pero con capitalizacion","5-Funcion que recibe un conjuto de numeros,los cuales representan la\npuntuacion de un concurso y esta devuelve la puntuacion del subcampeon","0-Finaliza el programa"]
    print("Bienvendido al grupo de ejercicios de Codo a Codo")
    while not buscador < 6 and buscador >= 0:
        try:
            for listaOpciones in opciones:
                print(listaOpciones)
            buscador = int(input("Ingresa aca: "))
        except ValueError:
            print("Por favor, ingresa un dato valido")
    #Si no es != no cierra el programa
    if(buscador != 0):
        #Protocolo pregunta 4
        if(buscador == 5):
            while datoGeneral != 3:
                #Menu de opciones
                if(datoGeneral == 0):
                    print("\nQue deseas hacer ahora?\
                        \n1-Continuar ingresando\
                        \n2-Eliminar la calificacion ingresada\
                        \n3-Dejar de ingresar calificaciones")
                    try:
                        datoGeneral = int(input("Ingresa aca: "))
                    except ValueError:
                        print("Por favor ingresa un valor numerico")
                #Ingresa datos
                elif(datoGeneral == 1):
                    try:
                        valorPricipal = int(input(f"Ingresa la {len(contenedorCampeon)+1} Calificacion: "))
                    except ValueError:
                            print("Por favor ingresa un dato numerico")
                            continue
                    contenedorCampeon.append(valorPricipal)
                    datoGeneral = 0
                #Elimina en contenedorCampeon
                elif(datoGeneral == 2):
                    contenedorCampeon.pop()
                    print(f"lista actualizada: {contenedorCampeon}")
                    datoGeneral = 0
                #Salimos del bucle
                elif(datoGeneral == 3):
                    continue
                #En caso de no escoger una opcion valida
                else:
                    print("Por favor, elige una opcion valida")
                    datoGeneral = 0
            #Resultado final buscador 5
            if(datoGeneral == 3):                                
                resultadoCampeon = subCampeon(contenedorCampeon)
                print(contenedorCampeon,"\nEste es el Subcampeon: "+ str(resultadoCampeon))
        #Protocolo de pregunta 3
        elif(buscador == 3):
            while datoGeneral != 3:
                if(datoGeneral == 1):
                    try:
                        #palabra
                        palabra = str(input("Por favor, ingrese la frase: "))
                        if(palabra == "-1"):
                            print("---Repitiendo entrada de datos---")
                            continue
                        contador = 0
                        for valor in palabra:
                            print(f"[{valor}={contador}]",end=" ")
                            contador += 1
                        #Index
                        index = int(input("\nIngrese la ubicacion de la palabra a ser cambiada: "))
                        if(index == "-1" or index > len(palabra)-1 or index < 0):
                            print("---Repitiendo entrada de datos---")
                            continue
                        #letra
                        letra = str(input("ingresa la letra a ser cambiada: "))
                        if(letra == "-1"):
                            print("---Repitiendo entrada de datos---")
                            continue
                        datoGeneral = 2
                    except ValueError:
                        print("Por favor ingresa un dato valido")
                #valida el ingreso de datos
                elif(datoGeneral == 2):
                    print(f"{palabra}\n{palabra[index]} sera cambiado por: {letra}")
                    try:
                        datoGeneral = str(input("Esta correcto el ingreso de los datos?Si/No: ")).lower()
                        if(datoGeneral == "si"):
                            datoGeneral = 3
                        elif(datoGeneral == "no"):
                            datoGeneral = 1
                        else:
                            print("Ingresa un valor valido")
                            datoGeneral = 2
                    except ValueError:
                        print("Por favor, ingresa un dato valido\n")
            #Imprime el resultado de buscador 3
            if(datoGeneral == 3):
                print("Resultado: ",modificarLetra(index,palabra,letra))

    else:
        print("programa finalizado")

                              
                      

                           
        



if __name__ == "__main__":
    main()
