# -*- coding: utf-8 -*-
import pygame, time, os, sys
from pygame.locals import *
from msvcrt import getch
from random import randint

#----------------------------------#
#           Funções Gerais         #
#----------------------------------#

#Limpa a tela
def cls():
	os.system('cls' if os.name=='nt' else 'clear')

#----------------------------------#
#       Funções para Matrizes      #
#----------------------------------#

def moves(matrizNum, matrizColor):
	for j in range(10):
		for i in range(10):
			#Color Red
			if matrizColor[i][j] == 'R':
				if matrizNum[i][j] > 0 and matrizNum[i][j] < 4 and (j < 9):
					moveDir = randint(1,6)
					#Move Color(1 e 2 = Right;Dir); (3 e 4 = South;Baixo); (5 = Left;Esq); (6 = North;Cima)
					if moveDir == 1 or moveDir == 2:
						if matrizNum[i][j+1] == 4 and matrizNum[i][j] == 3: 
							matrizNum[i][j+1] = 3
							matrizNum[i][j] = 4
							i += 1												
						elif matrizNum[i][j+1] < 3:
							matrizNum[i][j+1] = matrizNum[i][j] - 1
							matrizNum[i][j] = 4
							matrizColor[i][j+1] = 'R'
						

	return (matrizNum, matrizColor)				


def genGridNum():
	for x in range(10):
	    matrizGridNum.append([0] * 10)
	return matrizGridNum

def insertGridNum():
	matrizGridNum[0][0] = 3
	matrizGridNum[1][1] = 3
	matrizGridNum[9][9] = 3
	return matrizGridNum

def gengridColor():
	for x in range(10):
	    matrizGridColor.append(['.'] * 10)
	return matrizGridColor

def insertGridColor():
	matrizGridColor[0][0] = 'R'
	matrizGridColor[1][1] = 'R'
	matrizGridColor[9][9] = 'B'
	return matrizGridColor

def printMat(matriz):
	for i in range(10):
		for j in range(10):
			print matriz[i][j],
		print ""
	print ""
	print("Ctrl + C for Quit")




#-------------------------------------------------------#
#-------------------------------------------------------#
#            AQUI COMEÇA A PORRA DO CÓDIGO              #
#-------------------------------------------------------#
#-------------------------------------------------------#

matrizGridNum = []
matrizGridColor = []
genGridNum()
gengridColor()
matrizGridNum = insertGridNum()
matrizGridColor = insertGridColor()
cont = 0

while True:
	"""key = ord(getch())
				if key == 27:
					break
				cls()"""
	cls()
	matriz = moves(matrizGridNum, matrizGridColor)
	printMat(matriz[1])
	#print "=========="
	#printMat(matriz[1])
	time.sleep(.5)

	cont += 1
	if cont == 3: 
		matrizGridNum[0][0] = 3
		matrizGridNum[1][1] = 3
		cont = 0

	#KEYS = Down = 80|Up = 72|Left = 75|Right = 77|Enter = 13|Esc = 27