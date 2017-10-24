# -*- coding: utf-8 -*-
import pygame, time, os, sys
from pygame.locals import *


def essential();
	mapX = 10
	mapY = 10
	
class Hero(object):
	def __init__(self, name):
		self.name = name

	def moveUp(self):
		if direction == 0:
			screen.blit(heroUp, [playerpos[0] * 32, playerpos[1] * 32])
			pygame.display.flip()
		elif direction == 1:
			screen.blit(heroDown, [playerpos[0] * 32, playerpos[1] * 32])
			pygame.display.flip()
		elif direction == 2:
			screen.blit(heroLeft, [playerpos[0] * 32, playerpos[1] * 32])
			pygame.display.flip()
		elif direction == 3:
			screen.blit(heroRight, [playerpos[0] * 32, playerpos[1] * 32])
			pygame.display.flip()

def matriz(txt):
	#inicia matriz
	matriz = []
	for x in range(mapY):
	    matriz.append([0] * mapX)
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


def printMatriz(matriz):
	#inicia sqm(matriz)
	sqm = []
	for x in range(mapY):
	    sqm.append([0] * mapX)
	#insere matriz no sqm
	for i in range(10):
		for j in range(10):
			if matriz[i][j] == 1:
				sqm[i][j] = " "
			elif matriz[i][j] == 0:
				sqm[i][j] = "0"
	for i in range(10):
		for j in range(10):
			print sqm[i][j],
		print ""

def printMap():
	showMap = matriz(map1)
	for i in range(10):
		for j in range(10):
			if showMap[i][j] == 1:
				screen.blit(grass, [j * 32, i * 32])
			else:
				screen.blit(bush, [j * 32, i * 32])
	pygame.display.flip()	

def printPerson(playerpos, direction):
	if direction == 0:
		screen.blit(heroUp, [playerpos[0] * 32, playerpos[1] * 32])
		pygame.display.flip()
	elif direction == 1:
		screen.blit(heroDown, [playerpos[0] * 32, playerpos[1] * 32])
		pygame.display.flip()
	elif direction == 2:
		screen.blit(heroLeft, [playerpos[0] * 32, playerpos[1] * 32])
		pygame.display.flip()
	elif direction == 3:
		screen.blit(heroRight, [playerpos[0] * 32, playerpos[1] * 32])
		pygame.display.flip()


def moveValidation(playerpos, matriz):
	status = False


#----------------------------------------s---------------
# AQUI COMEÇA A PORRA DO CÓDIGO
#-------------------------------------------------------

essential()

#Dimensão da tela
screenDimension = (320, 320)
#Chama a funcao que seta o tamanho da tela
screen = pygame.display.set_mode(screenDimension, 0, 32)
pygame.display.set_caption('Pokémon')

map1 = "0100000000011100111001110011110111001110001000010001110011100111001110011111111001110011100000000000"

#matriz(map1)
#printMatriz(matriz(map1))
bush = pygame.image.load("./src/Tiles/bush1.png")
grass = pygame.image.load("./src/Tiles/grass1.png")
ball = pygame.image.load("./src/Persons/ball1.png")
heroDown = pygame.image.load("./src/Persons/heroDown.png")
heroUp = pygame.image.load("./src/Persons/heroUp.png")
heroLeft = pygame.image.load("./src/Persons/heroLeft.png")
heroRight = pygame.image.load("./src/Persons/heroRight.png")
keys = [False, False, False, False]
playerpos = [1,0]
positionMap = matriz(map1)
direction = 1
red = Hero("Joao")
while True:
	printMap()
	#printPerson(playerpos, direction)
	red.moveUp()
	for event in pygame.event.get():		

		if event.type == pygame.KEYDOWN:
			if event.key == K_w:
				keys[0] = True
			elif event.key == K_s:
				keys[1] = True
			elif event.key == K_a:
				keys[2] = True
			elif event.key == K_d:
				keys[3] = True

		if event.type == pygame.KEYUP:
			if event.key == K_w:
				keys[0] = False
			elif event.key == K_s:
				keys[1] = False
			elif event.key == K_a:
				keys[2] = False
			elif event.key == K_d:
				keys[3] = False

		if keys[0]:
			direction = 0
			if playerpos[1] > 0 and positionMap[playerpos[1]-1][playerpos[0]] == 1:
				playerpos[1] -= 1
		elif keys[1]:
			direction = 1
			if playerpos[1] < 9 and positionMap[playerpos[1]+1][playerpos[0]] == 1:
				playerpos[1] += 1
		if keys[2]:
			direction = 2
			if playerpos[0] > 0 and positionMap[playerpos[1]][playerpos[0]-1] == 1:
				playerpos[0] -= 1
		elif keys[3]:
			direction = 3
			if playerpos[0] < 9 and positionMap[playerpos[1]][playerpos[0]+1] == 1:
				playerpos[0] += 1

		if event.type == pygame.QUIT:			
			pygame.quit()
			exit(0)