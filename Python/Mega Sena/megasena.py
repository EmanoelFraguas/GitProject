# -*- coding: utf-8 -*-
import pickle, time, os, sys

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

def inicio():
	loadVet()
	menu()
	readKey()

def insertPadrao():
	arq = open('padrao.pck', 'rb')
	x = pickle.load(arq)
	arq.close()

def checkNew(n, a):
	test =  False
	for j in range(len(a)):
		if n == a[j]:
			test = True
			break
	return test

def checkSave(n):
	test = False
	if n == 1 or n == 2:
		test = True
	return test


def saveNew10(a):
	print('====================')
	print('Deseja salva-los?')
	print('1 - Sim')
	print('2 - Nao')
	print('====================')
	n = input()
	checks = checkSave(n)
	while checks == False:
		print('Numero invalido. Digite novamente:')
		n = input()
		checks = checkSave(n)
	if n == 1:
		arq = open('arquivo.pck', 'rb')
		vet = pickle.load(arq)
		arq.close()
		for i in range(len(a)):
			vet[a[i]-1] -= 1
		for i in range(len(vet)):
			vet[i] += 1
				
		arq = open('arquivo.pck', 'wb')
		pickle.dump(vet, arq)
		arq.close()
		


def insertNew10():
	a = []
	print('Digite os 10 valores:')
	for i in range(10):
		n = input()
		check = checkNew(n, a)
		while check or (n < 1) or (n > 25):
			print('Digite novamente:')
			n = input()
			check = checkNew(n, a)
		a.append(n)
	print('Numeros Digitados:')
	#a = a.sorted()
	a.sort()
	print a
	saveNew10(a)
	printVet()
	


def loadVet():
	arq = open('arquivo.pck', 'rb')
	x = pickle.load(arq)
	arq.close()
	return x

def menu():
	print('')
	print('====================')
	print('0 - Sair')
	print('1 - Inserir resultados do concurso 1584')
	print('2 - Imprime na tela vetor')
	print('3 - Inserir 10 numeros nao jogados')
	print('4 - Mostra numeros por ordem frequencia')
	print('====================')
	print('')

def printVet():
	arq = open('arquivo.pck', 'rb')
	x = pickle.load(arq)
	print('Valores do vetor:')
	for i in range(len(x)):
		#print("|%s-%s" % (i+1,x[i])),
		print('%02d' %(i+1)),
	print('')
	for i in range(len(x)):
		#print("|%s-%s" % (i+1,x[i])),
		print('%02d' % x[i]),
	print ('')
	arq.close()

def bubbleSort(z, y):
	pass


def showOrder():
	#y = sorted(x)
	x1 = []
	for i in range(25):
		x1.append(i+1)
	y1 = loadVet()
	for j in range(25):
		for i in range(24):
			if y1[i]>y1[i+1]:
				aux1 = y1[i+1]
				y1[i+1] = y1[i]
				y1[i] = aux1
				#---
				aux2 = x1[i+1]
				x1[i+1] = x1[i]
				x1[i] = aux2


	x1 = x1[::-1]
	y1 = y1[::-1]
	print('Valores mais frequentes.')
	l1 = True
	l2 = True
	for i in range(len(x1)):
		if y1[i] < y1[9] and l1 == True:
			print('-'),
			l1 = False
		print('%02d' %(x1[i])),
	print('')
	for i in range(len(x1)):
		if y1[i] < y1[9] and l2 == True:
			print('-'),
			l2 = False
		print('%02d' % y1[i]),
	print('')
	#bubbleSort(x, y)


def readKey():
	insert = input()
	if insert == 1:
		cls()
		menu()
		insertPadrao()
		readKey()
	elif insert == 2:
		cls()
		menu()
		printVet()
		readKey()
	elif insert == 3:
		cls()
		menu()
		insertNew10()
		cls()
		menu()
		printVet()
		readKey()
	elif insert == 4:
		cls()
		menu()
		showOrder()
		readKey()
	elif insert == 0:
		pass
	else:
		cls()
		menu()
		print('Numero Invalido, digite novamente:') 
		readKey()


#----------
cls()
inicio()
