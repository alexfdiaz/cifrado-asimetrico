from rsa import *
import os

os.system('cls')

#Funcion para guardar el par de claves en un archivo .txt
def opcionGuardarClaves(publicKey, privateKey):
    os.system('cls')
    print("Ingrese ruta (absoluta) del archivo. Ejemplo: C:/users/juan/desktop/archivo.txt")
    ruta = input("Ruta: ")
    f = open(ruta, "w+")
    for i in range(3):
        if i == 0: f.write("Par de claves generadas:")
        elif i == 1: f.write(f"\nClave publica: {publicKey}")
        else: f.write(f"\nClave privada: {privateKey}")
    print("\nClaves guardadas con exito")
    f.close()

#Funcion que toma una cadena y devuelve una lista de enteros
def convertir(string):
    lista = list(string.split(", "))
    listaInt = [int(i) for i in lista]
    return listaInt

#Funcion que ejecuta el cifrado de un mensaje ingresado por teclado
def opcionCifrar():
    os.system('cls')
    msje = input("Ingrese el mensaje a cifrar: ")
    clavePublicaStr = input("Ingrese clave publica del destinatario (ejemplo: 221, 137): ")
    clavePublica = tuple(map(int, clavePublicaStr.split(', ')))
    msjeCifrado = cifrar(msje, clavePublica)
    print(f"Mensaje cifrado: {msjeCifrado}")
    print("\n!!!Copiar mensaje SIN corchetes!!!")

#Funcion que ejecuta el descifrado de un mensaje por teclado
def opcionDescifrar():
    os.system('cls')
    msjeCifrado = input("Ingrese el mensaje cifrado: ")
    msjeCifradoInt = convertir(msjeCifrado)
    clavePrivadaStr = input("Ingrese su clave privada (ejemplo: 253, 141): ")
    clavePrivada = tuple(map(int, clavePrivadaStr.split(', ')))
    #print(clavePrivada)
    msje = descifrar(msjeCifradoInt, clavePrivada)
    os.system('cls')
    print(f"Mensaje original: {msje}")

#Funcion generadora de par de claves publica y privada
def opcionClaves():
    os.system('cls')
    num = 10
    print("Par de claves generadas:")

    #Algoritmo RSA para generar el par de claves
    prime1 = randomPrime(num)
    prime2 = randomPrime(num)
    modulo = prime1 * prime2
    fiModulo = (prime1 - 1) * (prime2 - 1)
    publicKeyExp = randomCoprime(fiModulo)
    privateKeyExp = randomD(publicKeyExp, fiModulo)
    publicKey  = (modulo, publicKeyExp)
    privateKey = (modulo, privateKeyExp)

    print(f"Clave publica: {publicKey}")
    print(f"Clave privada: {privateKey}")

    teclaIncorrecta2 = True
    while teclaIncorrecta2:
        print("Desea guardar las claves en un archivo .txt?\n[1] SI\n[2] NO")
        tecla = input("Ingrese instruccion: ")
        if tecla == '1':
            opcionGuardarClaves(publicKey, privateKey)
            teclaIncorrecta2 = False
        elif tecla == '2':
            teclaIncorrecta2 = False
        else:
            os.system('cls')
            print("Intente nuevamente\n")

    print("\n!!!Para ingresar las claves, ignorar los parentesis!!!")

def main():
    print("Hola!")

    teclaIncorrecta = True

    #Bucle que corre el menu principal, donde se ingresan las instrucciones
    while teclaIncorrecta:
        print("Pulse [1] si quiere cifrar un mensaje\nPulse [2] si quiere descifrar un mensaje\nPulse [3] si quiere generar un par de claves")
        tecla = input("Ingrese instruccion: ")
        if tecla == '1':
            opcionCifrar()
            teclaIncorrecta = False
        elif tecla == '2':
            opcionDescifrar()
            teclaIncorrecta = False
        elif tecla == '3':
            opcionClaves()
            teclaIncorrecta = False
        else:
            os.system('cls')
            print("Intente nuevamente\n")

if __name__ == '__main__':
    main()