# -*- coding: utf-8 -*-
import pickle, time, os, sys

#----------------------------------#
#         Funções Gerais           #
#----------------------------------#

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

def inicio():
	menu()
	readKey()

#----------------------------------#
#         Funções Pickle           #
#----------------------------------#

#Insere na variavel 'padrao' 'arquivo.pck'
def insertIni():
	arq = open('arquivo.pck', 'rb')
	x = pickle.load(arq)
	arq.close()
	return x

#Insere na variavel 'padrao' os resultados até o concurso 1584
def insertPadrao():
	arq = open('padrao.pck', 'rb')
	x = pickle.load(arq)
	arq.close()
	return x

#----------------------------------#
#       Impressão de texto         #
#----------------------------------#

#Menu Principal
def menu():
	print('')
	print('====================')
	print('0 - Sair')
	print('1 - Resultado do concurso X. (1 ao 1584)')
	print('2 - Imprime tabela com Frequencia, Media de Aparicao, Porcentagem')
	print('3 - Inserir 10 numeros nao jogados')
	print('? - Inserir 15 numeros jogados')
	print('8 - Testes')
	print('9 - Reseta valores para concurso 1-1584')
	print('====================')
	print('')

#Imprime tabela geral
def tabela():
	freq = frequencia()
	apar = aparicao()
	media = mediaTot()
	print "|-----------|----1|----2|----3|----4|----5|----6|----7|----8|----9|---10|---11|---12|---13|---14|---15|---16|---17|---18|---19|---20|---21|---22|---23|---24|---25|"
	print "|           |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |"
	print "| Frequencia|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s|  %s| " % (freq[0], freq[1], freq[2], freq[3], freq[4], freq[5], freq[6], freq[7], freq[8], freq[9], freq[10], freq[11], freq[12], freq[13], freq[14], freq[15], freq[16], freq[17], freq[18], freq[19], freq[20], freq[21], freq[22], freq[23], freq[24])
	print "|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|"
	print "| Media Apar| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f| %.2f|" % (apar[0], apar[1], apar[2], apar[3], apar[4], apar[5], apar[6], apar[7], apar[8], apar[9], apar[10], apar[11], apar[12], apar[13], apar[14], apar[15], apar[16], apar[17], apar[18], apar[19], apar[20], apar[21], apar[22], apar[23], apar[24])
	print "|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|"
	print "|Porcentagem|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|%s%%|" % (media[0], media[1], media[2], media[3], media[4], media[5], media[6], media[7], media[8], media[9], media[10], media[11], media[12], media[13], media[14], media[15], media[16], media[17], media[18], media[19], media[20], media[21], media[22], media[23], media[24])

#Imprime o resultado do concurso digitado
def resultConcurso():
	n = int(input('Insira um valor entre 1 e 1584: '))
	while n < 1 or n > totCont:
		n = int(input('Numero invalido. Digite novamente:'))
	cls()
	menu()
	print('Resultado do concurso %s:' % (n))
	print padrao[n-1]

def frequencia():
	freq = []
	for i in range(25):
		freq.append(0)
	for i in range(totCont):
		for j in range(15):
			freq[padrao[i][j]-1] += 1
	return freq

def aparicao():
	freq = []
	for i in range(25):
		freq.append(0.0)
	for i in range(totCont):
		for j in range(15):
			freq[padrao[i][j]-1] += 1
	for i in range(len(freq)):
		freq[i] = round((totCont / freq[i]), 2)
	return freq

def mediaTot():
	freq = []
	for i in range(25):
		freq.append(0.0)
	for i in range(totCont):
		for j in range(15):
			freq[padrao[i][j]-1] += 1
	for i in range(len(freq)):
		freq[i] = (100 * freq[i])/totCont
		freq[i] = round(freq[i], 1)
	return freq

#----------------------------------#
#  Funções para Inserir 10 Números #
#----------------------------------#

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

def saveNew10(a, padrao):
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
		vet = padrao
		vet.append(a)
				
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
	saveNew10(a, padrao)

#----------------------------------#
#  Funções para Inserir 15 Números #
#----------------------------------#

#----------------------------------#
#       Funções para Opções        #
#----------------------------------#

def readKey():
	insert = input()
	#Imprime resultado do concurso inserido
	if insert == 1:
		cls()
		menu()
		resultConcurso()
		readKey()

	#Imprime tabela com Frequencia, Media de Aparicao, Porcentagem.
	elif insert == 2:
		cls()
		menu()
		tabela()
		readKey()

	#Insere a partir de 10 numeros nao jogados.
	elif insert == 3:
		cls()
		menu()
		insertNew10()
		cls()
		menu()
		print("Numeros inseridos com sucesso.")
		readKey()

	#Insere 15 numeros jogados.
	elif insert == 4:
		cls()
		menu()
		#--
		readKey()

	#Testes
	elif insert == 8:
		padrao = insertPadrao()
		print len(padrao)


		#cls()
		#menu()
		#--
		readKey()
	#Reseta valores para concurso 1-1584
	elif insert == 9:
		padrao = insertPadrao()
		totCont = len(padrao)
		cls()
		menu()
		print("Valores resetados.")
		readKey()
	#Sair da execução	
	elif insert == 0:
		pass
	else:
		cls()
		menu()
		print('Numero Invalido, digite novamente:') 
		readKey()

#-------------------------------------------------------#
#-------------------------------------------------------#
#            AQUI COMEÇA A PORRA DO CÓDIGO              #
#-------------------------------------------------------#
#-------------------------------------------------------#

cls()
padrao = insertIni()
totCont = len(padrao)
inicio()