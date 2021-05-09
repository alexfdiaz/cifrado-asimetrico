from random import *

def isPrime(num):
	divisores = 0
	for i in range(num):
		if num % (i + 1) == 0:
			divisores += 1
	if divisores < 3: return True
	else: return False

def randomPrime(num):
	seed(getstate())
	ran = randint(num, 2 * num)
	while not isPrime(ran):
		ran += 1
		if ran == 2 * num:
			ran = num
	return ran

def mcd(a, b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a

def areCoprime(a, b):
	if mcd(a, b) == 1: return True
	else: return False

def randomCoprime(num):
	while True:
		seed(getstate())
		ran = randint(1, num - 1)
		if areCoprime(ran, num):
			return ran

def randomD(e, fi):
	'''while True:
		seed(getstate())
		ran = randint(1, fi)
		if (e * ran - 1) % fi == 0:
			return ran'''
	for d in range(2, fi):
		if (e * d - 1) % fi == 0:
			return d

def findByMod(num, mod, div):
	while True:
		seed(getstate())
		ran = randint(1, num)
		if ran % div == mod:
			return ran

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

def descifrar(msjeCifrado, privateKey):
	msjeDescifrado = []
	for i in msjeCifrado:
		msjeCifradoExp = i ** privateKey[1]
		msjeDescifrado.append(msjeCifradoExp % privateKey[0])
	res = ''.join(map(chr, msjeDescifrado))
	return str(res)