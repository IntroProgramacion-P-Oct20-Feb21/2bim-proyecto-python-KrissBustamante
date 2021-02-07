
              
            

def crearFacebook():
    """
        explicación de método
    """
    print("Creando cuenta de Facebook")
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese el nombre de su ciudad: ")
    pais = input("Ingrese el nombre de su pais: ")
    idioma = input("Ingrese que idioma habla: ")
    correo = input("Ingrese su correo electronico: ")
    print("Nombre: %s\nEdad: %d\nCiudad: %s\nPais: %s\nIdioma: %s\nCorreo: %s\n" %\
    (nombre,edad,ciudad,pais,idioma,correo))



def crearTwitter():
    """
        explicación de método
    """
    print("Creando cuenta de Twitter")
    nombres = input("Ingrese sus nombres: ")
    apellidos = input("Ingrese sus apellidos: ")
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese el nombre de su ciudad: ")
    pais = input("Ingrese el nombre de su pais: ")
    idioma = input("Ingrese que idioma habla: ")
    correo = input("Ingrese su correo electronico: ")
    print("Nombres: %s\nApellidos: %s\nEdad: %d\nCiudad: %s\nPais: %s\nIdioma: %s\nCorreo: %s\n" %\
    (nombres,apellidos,edad,ciudad,pais,idioma,correo))


def crearWhatsapp():
    """
        explicación de método
    """
    print("Creando cuenta de Whatsapp")
    nombres = input("Ingrese sus nombres: ")
    numero = int(input("Ingrese su numero de celular: "))
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese el nombre de su ciudad: ")
    pais = input("Ingrese el nombre de su pais: ")
    print( "Nombres: %s\nNuemro: %s\nEdad: %d\nCiudad: %s\nPais: %s\n" %\
    (nombres,numero,edad,ciudad,pais))



def crearTelegram():
    """
        explicación de método
    """
    print("Creando cuenta de Telegram")
    nombres = input("Ingrese sus nombres: ")
    numero = int(input("Ingrese su numero de celular: "))
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese el nombre de su ciudad: ")
    pais = input("Ingrese el nombre de su pais: ")
    area = input("Ingrese su area de interes: ")
    print ("Nombres: %s\nNuemro: %s\nEdad: %d\nCiudad: %s\nPais: %s\nArea:%s\n" %\
    (nombres,numero,edad,ciudad,pais,area))

def crearSignal():
    """
        explicación de método
    """
    print("Creando cuenta de Signal")
    nombres = input("Ingrese sus nombres: ")
    numero = int(input("Ingrese su numero de celular: "))
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese el nombre de su ciudad: ")
    pais = input("Ingrese el nombre de su pais: ")
    hobby = input("Ingrese su hobby principal: ")
    print("Nombres: %s\nNuemro: %s\nEdad: %d\nCiudad: %s\nPais: %s\nHobby:%s\n" %\
    (nombres,numero,edad,ciudad,pais,hobby))


def crearInstagram():
    """
        explicación de método
    """
    print("Creando cuenta de Instagram")
    nombres = input("Ingrese sus nombres: ")
    ciudad = input("Ingrese el nombre de su ciudad: ")
    edad = int(input("Ingrese su edad: "))
    correo = input("Ingrese correo electronico: ")
    print ("Nombres: %s\nCiudad: %s\nEdad: %d\nCorreo:%s\n" %\
    (nombres,ciudad,edad,correo))

def crearFlickr():
    """
        explicación de método
    """
    print("Creando cuenta de Flickr")
    nombres = input("Ingrese sus nombres: ")
    correo = input("Ingrese correo electronico: ")
    print("Nombres: %s\nCorreo:%s\n" %\
    (nombres,correo))

def obtenerMensaje(indice):
    """
    explicación de método
    """
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    if(contador >= 1 and contador <= 5):
        cadena = (mensajeFinal[0])
    else:
        if(contador >= 6 and contador <= 15):
            cadena = (mensajeFinal[1])
        else:
            if(contador <= 16):
                cadena = (mensajeFinal[2])
    return cadena


   """
Proyecto Bimestral
Segundo Bimestre

Problemática:

"""
if __name__ == "__main__":
    print("proceso inicial")
    bandera = True
    while(bandera):
        
        print("Ingrese cualquiera de las opciones para crear una cuenta: \n")
        opcion = int(input("Ingrese 1 para crear una cuenta en Facebook: \n"\
        "Ingrese 2 para crear una cuenta en Twiter: \n"\
        "Ingrese 3 para crear una cuenta en Whatsapp: \n"\
        "Ingrese 4 para crear una cuenta en Telegram: \n"\
        "Ingrese 5 para crear una cuenta en Signal: \n"\
        "Ingrese 6 para crear una cuenta en Instagram: \n"\
        "Ingrese 7 para crear una cuenta en Flickr: \n"))
        if(opcion == 1):
            facebook = crearFacebook()
            indice = indice +1
        else:
            if(opcion == 2):
                Twitter = crearTwitter()
                indice = indice +1
            else:
                if(opcion == 3):
                    Whatsapp = crearWhatsapp()
                    indice = indice +1
                else:
                    if(opcion == 4):
                        Telegram = crearTelegram()
                        indice = indice +1
                    else:
                        if(opcion == 5):
                            Signal = crearSignal()
                            indice = indice +1
                        else:
                            if(opcion == 6):
                                Instagram = crearInstagram()
                                indice = indice +1
                            else:
                                if(opcion == 7):
                                    Flickr = crearFlickr()
                                    indice = indice +1
                                else:
                                    print("Opcion incorrecta")
                                    

        salida = input( "Ingrese (si) si desea salir del ciclo \n" )
        if(salida == "si"):
            bandera = False
        
        print ("Resultado de Campaña es: +\n" + obtenerMensaje) 
            


