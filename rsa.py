from random import *

#Funciones para la generacion del par de claves (desde linea 3 hasta linea 50)

#Funcion que toma un numero y devuelve un valor booleano en relacion a si es primo o no
def isPrime(num):
	divisores = 0
	for i in range(num):
		if num % (i + 1) == 0:
			divisores += 1
	if divisores < 3: return True
	else: return False

#Generador aleatorio de numeros primos. Primero genera un numero cualquiera y despues comprueba si es primo, si lo es devuelve el numero
def randomPrime(num):
	seed(getstate())
	ran = randint(num, 2 * num)
	while not isPrime(ran):
		ran += 1
		if ran == 2 * num:
			ran = num
	return ran

#Funcion que calcula el minimo comun divisor (para luego comprobar si dos numeros son coprimos)
def mcd(a, b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a

#Funcion que toma dos numeros y devuelve un booleano en relacion a si son coprimos o no
def areCoprime(a, b):
	if mcd(a, b) == 1: return True
	else: return False

#Funcion que toma un numero  n y genera un coprimo aleatorio en el rango (1, n-1)
def randomCoprime(num):
	while True:
		seed(getstate())
		ran = randint(1, num - 1)
		if areCoprime(ran, num):
			return ran

#Funcion que genera un exponente de la clave privada
def randomD(e, fi):
	for d in range(2, fi):
		if (e * d - 1) % fi == 0:
			return d

#Funcion que genera un numero aleatorio que cumpla que al dividirlo por div tenga el mismo resto que mod
def findByMod(num, mod, div):
	while True:
		seed(getstate())
		ran = randint(1, num)
		if ran % div == mod:
			return ran

#Funcion que encripta el mensaje introducido
def cifrar(msje, publicKey):
	lista = []
	msjeCifrado = []
	for caracter in msje:
		lista.append(ord(caracter))
	for i in lista:
		msjeExp = i ** publicKey[1]
		mod = msjeExp % publicKey[0]
		msjeCifrado.append(findByMod(msjeExp, mod, publicKey[0]))
	return msjeCifrado


#Funcion que desencripta el mensaje introducido
def descifrar(msjeCifrado, privateKey):
	msjeDescifrado = []
	for i in msjeCifrado:
		msjeCifradoExp = i ** privateKey[1]
		msjeDescifrado.append(msjeCifradoExp % privateKey[0])
	res = ''.join(map(chr, msjeDescifrado))
	return str(res)