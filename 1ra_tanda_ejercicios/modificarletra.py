def modificarLetra(index,palabra,palabraCambia):
        """Funcion que permite el cambio en una cadena de texto mediante el ingreso de un string,\
             indice y la pabra a cambiar"""
        palabra = list(palabra)
        palabra[index] = palabraCambia
        print("".join(palabra)) 

