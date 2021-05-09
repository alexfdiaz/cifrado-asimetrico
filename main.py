from rsa import *
import os

os.system('cls')

def convertir(string):
    lista = list(string.split(", "))
    listaInt = [int(i) for i in lista]
    return listaInt

def opcion1():
    os.system('cls')
    msje = input("Ingrese el mensaje a cifrar: ")
    clavePublicaStr = input("Ingrese clave publica del destinatario (ejemplo: 221, 137): ")
    clavePublica = tuple(map(int, clavePublicaStr.split(', ')))
    msjeCifrado = cifrar(msje, clavePublica)
    print(f"Mensaje cifrado: {msjeCifrado}")
    print("\n!!!Copiar mensaje SIN corchetes!!!")

def opcion2():
    os.system('cls')
    msjeCifrado = input("Ingrese el mensaje cifrado: ")
    msjeCifradoInt = convertir(msjeCifrado)
    clavePrivadaStr = input("Ingrese su clave privada (ejemplo: 253, 141): ")
    clavePrivada = tuple(map(int, clavePrivadaStr.split(', ')))
    #print(clavePrivada)
    msje = descifrar(msjeCifradoInt, clavePrivada)
    os.system('cls')
    print(f"Mensaje original: {msje}")

def opcion3():
    os.system('cls')
    num = 10
    print("Par de claves generados:")

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
    print("\n!!!Para ingresar las claves, ignorar los parentesis!!!")

print("Hola!")

teclaIncorrecta = True

while teclaIncorrecta:
    print("Pulse [1] si quiere cifrar un mensaje\nPulse [2] si quiere descifrar un mensaje\nPulse [3] si quiere generar un par de claves")
    tecla = input("Ingrese instruccion: ")
    if tecla == '1':
        opcion1()
        teclaIncorrecta = False
    elif tecla == '2':
        opcion2()
        teclaIncorrecta = False
    elif tecla == '3':
        opcion3()
        teclaIncorrecta = False
    else:
        os.system('cls')
        print("Intente nuevamente")


msje = 'bolas'

#100000
num = 10

prime1 = randomPrime(num)
prime2 = randomPrime(num)
modulo = prime1 * prime2
fiModulo = (prime1 - 1) * (prime2 - 1)
publicKeyExp = randomCoprime(fiModulo)
privateKeyExp = randomD(publicKeyExp, fiModulo)

publicKey  = (modulo, publicKeyExp)
privateKey = (modulo, privateKeyExp)

'''print(f"Primo 1: {prime1}")
print(f"Primo 2: {prime2}")
print(f"Modulo: {modulo}")
print(f"φ(modulo): {fiModulo}")
print(f"exponente de clave publica: {publicKeyExp}")
print(f"exponente de clave privada: {privateKeyExp}")
print(f"Clave publica: {publicKey}")
print(f"Clave privada: {privateKey}")'''

'''msjeCifrado = cifrar(msje, publicKey)
msjeDescifrado = descifrar(msjeCifrado, privateKey)
#print(msjeCifrado)
print(msjeDescifrado)'''