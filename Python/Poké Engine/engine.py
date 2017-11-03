# -*- coding: utf-8 -*-
import pygame, time, os, sys
from pygame.locals import *

#----------------------------------#
#        Funções Primarias         #
#----------------------------------#

def newScreen():
	pygame.display.flip()
	screen.fill(0)
	screen.blit(mapa, mappos)

#----------------------------------#
#      Definição de Classes        #
#----------------------------------#

class Arcanine(object):
	def __init__(self, name):
		self.name = name

	def moveLeft(self):
		for i in range(4):
			if i % 2 == 0:
				newScreen()
				arcapos[0] = arcapos[0] - 4
				screen.blit(arcaLeft1, arcapos)
				time.sleep(0.05)
			else:
				newScreen()
				arcapos[0] = arcapos[0] - 4
				screen.blit(arcaLeft2, arcapos)
				time.sleep(0.05)

	def moveRight(self):
		for i in range(4):
			if i % 2 == 0:
				newScreen()
				arcapos[0] = arcapos[0] + 4
				screen.blit(arcaRight1, arcapos)
				time.sleep(0.05)
			else:
				newScreen()
				arcapos[0] = arcapos[0] + 4
				screen.blit(arcaRight2, arcapos)
				time.sleep(0.05)

	def moveDown(self):
		for i in range(4):
			if i % 2 == 0:
				newScreen()
				arcapos[1] = arcapos[1] + 4
				screen.blit(arcaDown1, arcapos)
				time.sleep(0.05)
			else:
				newScreen()
				arcapos[1] = arcapos[1] + 4
				screen.blit(arcaDown2, arcapos)
				time.sleep(0.05)
	
	def moveUp(self):
		for i in range(4):
			if i % 2 == 0:
				newScreen()
				arcapos[1] = arcapos[1] - 4
				screen.blit(arcaUp1, arcapos)
				time.sleep(0.05)
			else:
				newScreen()
				arcapos[1] = arcapos[1] - 4
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
screenDimension = (320, 349)
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
arcapos =[160, 160]
arcaDir = "a"
arca = Arcanine("Arcanine")

#----------------------------------#
#        Definição de Mapa         #
#----------------------------------#
mappos = [0,0]
mapa = pygame.image.load("./src/route103.png")

# FIRST FRAME
pygame.display.flip()
screen.fill(0)
screen.blit(mapa, mappos)
screen.blit(arcaLeft2, arcapos)

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
	if press[119] == 1:
		arca.moveUp()
		arcaDir = "w"
	elif press[115] == 1:
		arca.moveDown()
		arcaDir = "s"
	elif press[97] == 1:
		arca.moveLeft()
		arcaDir = "a"
	elif press[100] == 1:
		arca.moveRight()
		arcaDir = "d"	

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)