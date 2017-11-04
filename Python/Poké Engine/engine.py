# -*- coding: utf-8 -*-
import pygame, time, os, sys
from pygame.locals import *

#----------------------------------#
#        Funções Primarias         #
#----------------------------------#

def newScreen():
	pygame.display.flip()
	screen.fill(0)
	#screen.blit(mapa, mappos)
	printMap()

#----------------------------------#
#      Definição de Matrizes       #
#----------------------------------#

def matriz(txt):
	#inicia matriz
	matriz = []
	for x in range(10):
	    matriz.append([0] * 10)
	#insere na matriz
	cont = 0
	for i in range(10):
		for j in range(10):
			if txt[cont] == "0":
				matriz[i][j] = 0
			elif txt[cont] == "1":
				matriz[i][j] = 1
			cont += 1
	return matriz

def printMap():
	showMap = insert()
	for j in range(12):
		for i in range(12):
			if showMap[i][j] == 1:
				screen.blit(grass, [(j * 32), (i * 32)])
			elif showMap[i][j] == 0:
				screen.blit(bush, [(j * 32), (i * 32)])

def insert():
	matrix = matriz(map1)
	for i in range(10):
		matrix[i].insert(0, -1)
		matrix[i].append(-1)
	aux = []
	for i in range(len(matrix[0])+2):
		aux.append(-1)
	matrix.append(aux)
	matrix.insert(0, aux)
	return matrix

#----------------------------------#
#      Definição de Classes        #
#----------------------------------#

class tryMove(object):
	def __init__(self, name):
		self.name = name


	def left(self):
		matrix = insert()
		if matrix[arcaMat[1]+1][arcaMat[0]] != 1:
			return False
		elif matrix[arcaMat[1]+1][arcaMat[0]] == 1:
			return True
	def right(self):
		matrix = insert()
		if matrix[arcaMat[1]+1][arcaMat[0]+2] != 1 or arcaMat[0] > 8:
			return False
		elif matrix[arcaMat[1]+1][arcaMat[0]+2] == 1:
			return True
	def down(self):
		matrix = insert()
		if matrix[arcaMat[1]+2][arcaMat[0]+1] != 1:
			return False
		elif matrix[arcaMat[1]+2][arcaMat[0]+1] == 1:
			return True
	def up(self):
		matrix = insert()
		if matrix[arcaMat[1]][arcaMat[0]+1] != 1:
			return False
		elif matrix[arcaMat[1]][arcaMat[0]+1] == 1:
			return True


class Arcanine(object):
	def __init__(self, name):
		self.name = name

	def moveLeft(self):
		for i in range(4):
			if i % 2 == 0:
				newScreen()
				arcapos[0] = arcapos[0] - 8
				screen.blit(arcaLeft1, arcapos)
				time.sleep(0.05)
			else:
				newScreen()
				arcapos[0] = arcapos[0] - 8
				screen.blit(arcaLeft2, arcapos)
				time.sleep(0.05)

	def moveRight(self):
		for i in range(4):
			if i % 2 == 0:
				newScreen()
				arcapos[0] = arcapos[0] + 8
				screen.blit(arcaRight1, arcapos)
				time.sleep(0.05)
			else:
				newScreen()
				arcapos[0] = arcapos[0] + 8
				screen.blit(arcaRight2, arcapos)
				time.sleep(0.05)

	def moveDown(self):
		for i in range(4):
			if i % 2 == 0:
				newScreen()
				arcapos[1] = arcapos[1] + 8
				screen.blit(arcaDown1, arcapos)
				time.sleep(0.05)
			else:
				newScreen()
				arcapos[1] = arcapos[1] + 8
				screen.blit(arcaDown2, arcapos)
				time.sleep(0.05)
	
	def moveUp(self):
		for i in range(4):
			if i % 2 == 0:
				newScreen()
				arcapos[1] = arcapos[1] - 8
				screen.blit(arcaUp1, arcapos)
				time.sleep(0.05)
			else:
				newScreen()
				arcapos[1] = arcapos[1] - 8
				screen.blit(arcaUp2, arcapos)
				time.sleep(0.05)

#-------------------------------------------------------#
#-------------------------------------------------------#
#            AQUI COMEÇA A PORRA DO CÓDIGO              #
#-------------------------------------------------------#
#-------------------------------------------------------#

#----------------------------------#
#        Definição de Tela         #
#----------------------------------#

#Dimensao da tela
screenDimension = (384, 384)
#Chama a funcao que seta o tamanho da tela
screen = pygame.display.set_mode(screenDimension, 0, 32)
#Nome da tela
pygame.display.set_caption('Pokémon')
#Set icone
a = pygame.image.load("./src/pb.png")
pygame.display.set_icon(a)

#----------------------------------#
#      Definição do Arcanine       #
#----------------------------------#
arcaLeft1 = pygame.image.load("./src/arcaLeft1.png") 
arcaLeft2 = pygame.image.load("./src/arcaLeft2.png")
arcaRight1 = pygame.image.load("./src/arcaRight1.png")
arcaRight2 = pygame.image.load("./src/arcaRight2.png")
arcaUp1 = pygame.image.load("./src/arcaUp1.png") 
arcaUp2 = pygame.image.load("./src/arcaUp2.png")
arcaDown1 = pygame.image.load("./src/arcaDown1.png")
arcaDown2 = pygame.image.load("./src/arcaDown2.png")
arcaMat = [1, 1]
arcapos =[32, 32]
arcaDir = "a"
arca = Arcanine("Arcanine")

#----------------------------------#
#        Definição de Mapa         #
#----------------------------------#
tryMove = tryMove("Try Move")
mappos = [0,0]
map1 = "0100000000011100111001110011110111001110001000010001110011100111001110011111111001110011100000000000"
mapa = pygame.image.load("./src/route103.png")
bush = pygame.image.load("./src/bush.png")
grass = pygame.image.load("./src/grass.png")
tree = pygame.image.load("./src/tree.png")

# FIRST FRAME
newScreen()
screen.blit(arcaLeft2, arcapos)

test = insert()
print test

while True:

	if arcaDir == "a":
		newScreen()
		screen.blit(arcaLeft2, arcapos)
	elif arcaDir == "d":
		newScreen()
		screen.blit(arcaRight2, arcapos)
	elif arcaDir == "s":
		newScreen()
		screen.blit(arcaDown2, arcapos)
	elif arcaDir == "w":
		newScreen()
		screen.blit(arcaUp2, arcapos)

	press = pygame.key.get_pressed()
	if press[119] == 1 or press[273] == 1:
		if tryMove.up():
			arca.moveUp()
			arcaMat[1] = arcaMat[1] - 1
		arcaDir = "w"
		print(arcaMat[1], "Up.1")
	elif press[115] == 1 or press[274] == 1:
		if tryMove.down():
			arca.moveDown()		
			arcaMat[1] = arcaMat[1] + 1
		arcaDir = "s"
		print(arcaMat[1], "Down.1")
	elif press[97] == 1 or press[276] == 1:
		if tryMove.left():
			arca.moveLeft()
			arcaMat[0] = arcaMat[0] - 1
		arcaDir = "a"
		print(arcaMat[0],  "Left.1")
	elif press[100] == 1 or press[275] == 1:
		if tryMove.right():
			arca.moveRight()
			arcaMat[0] = arcaMat[0] + 1
		arcaDir = "d"	
		print(arcaMat[0], "Right.0")

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)