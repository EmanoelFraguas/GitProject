# -*- coding: utf-8 -*-
import pygame, time, os, sys
from pygame.locals import *
from msvcrt import getch

#----------------------------------#
#         Funções Gerais           #
#----------------------------------#

#Limpa a tela
def cls():
	os.system('cls' if os.name=='nt' else 'clear')

#----------------------------------#
#      Definição de Camadas        #
#----------------------------------#

#Camada do chão
def layerFloor():
	matriz = []
	for x in range(10):
	    matriz.append([0] * 10)
	return matriz

#Camada de paredes
def layerWall(wall):
	matriz = []
	for x in range(10):
	    matriz.append([0] * 10)
	cont = 0
	for i in range(10):
		for j in range(10):
			if wall[cont] == "0":
				matriz[i][j] = 1
			cont += 1
	return matriz

#Camada de baús
def layerChest(chest):
	matriz = []
	for x in range(10):
	    matriz.append([0] * 10)
	cont = 0
	for i in range(10):
		for j in range(10):
			if chest[cont] == "1":
				matriz[i][j] = 1
			cont += 1
	return matriz

#Camada que define a posição do player(Zera sempre a matriz, e insere 0 na posição)
def layerPlayer(x, y):
	matriz = []
	for cont in range(10):
	    matriz.append([0] * 10)
	for i in range(10):
		for j in range(10):
				if x == i and y == j:
					matriz[i][j] = 1
	return matriz

#Mescla de camadas
def mergeLayers():
	matriz = layerFloor()
	playerPos = layerPlayer(playerX, playerY)
	wall = layerWall(wallCode)
	chest = layerChest(chestCode)
	for i in range(10):
		for j in range(10):
			if wall[i][j] == 1:
				matriz[i][j] = 1
			elif chest[i][j] == 1:
				matriz[i][j] = 2
			elif playerPos[i][j] == 1:
				matriz[i][j] = 9
	return matriz

#Camada que concatena todas as camadas com itens intransponíveis
def layerSolid():
	wall = layerWall(wallCode)
	chest = layerChest(chestCode)
	matriz = []
	for x in range(10):
	    matriz.append([0] * 10)
	for i in range(10):
		for j in range(10):
			if wall[i][j] == 1:
				matriz[i][j] = 1
			if chest[i][j] == 1:
				matriz[i][j] = 2
	return matriz

#----------------------------------#
#    Funções que imprimem algo     #
#----------------------------------#

#Imprime a mescla de todas as camadas visíveis
def printMatriz():
	matriz = mergeLayers()
	#inicia sqm(matriz)
	sqm = []
	for x in range(10):
	    sqm.append([0] * 10)
	#insere matriz no sqm
	for i in range(10):
		for j in range(10):
			if matriz[i][j] == 0:
				sqm[i][j] = " "
			elif matriz[i][j] == 1:
				sqm[i][j] = "0"
			elif matriz[i][j] == 2:
				sqm[i][j] = "#"
			elif matriz[i][j] == 9:
				sqm[i][j] = "X"
	for i in range(10):
		for j in range(10):print sqm[i][j],
		print ""

def showChest():
	print"       __________"
	print("      /\____;;___\ ")
	print "     | /         /"
	print("     `. ())oo() . ")
	print "      |\(%()*^^()^\ "
	print("     %| |-%-------| ")
	print "     % \ | %  ))   |"
	print("     %  \|%________| ")
	print("      %%%		")

#Códigos para a definição de camadas
wallCode = "0100000000011100111001110011110111001110000000010001110011100111001110011111111001110011100000000000"
chestCode = "0000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000"

#-------------------------------------------------------#
#-------------------------------------------------------#
#            AQUI COMEÇA A PORRA DO CÓDIGO              #
#-------------------------------------------------------#
#-------------------------------------------------------#

playerX = 7
playerY = 3
#wall = layerWall(wallCode)
solid = layerSolid()
chest = layerChest(chestCode)

while True:
	printMatriz()

	key = ord(getch())
	cls()
	print(ord(getch()))
	#Down = 80|Up = 72|Left = 75|Right = 77|Enter = 13|Esc = 27
	if key == 27:
		break
	elif key == 115 and solid[playerX+1][playerY] == 0:
		print 'down'
		playerX += 1
	elif key == 119 and solid[playerX-1][playerY] == 0:
		print 'up'
		playerX -= 1
	elif key == 97 and solid[playerX][playerY-1] == 0:
		print 'left'
		playerY -= 1
	elif key == 100 and playerY <= 8:
		if solid[playerX][playerY+1] == 0:
			print 'right'
			playerY += 1
	elif key == 119 and chest[playerX-1][playerY] == 1:
		showChest()
	elif key == 100 and chest[playerX][playerY+1] == 1:
		showChest()

	if playerX == 2 and playerY == 9 and key == 13:
		wallCode ='0100000000011100111001110011110111001110001000010001110011100111001110011111111001110011100000000000'
		layerSolid()
		solid = layerSolid()

	print 'px', playerX,'| py', playerY

	