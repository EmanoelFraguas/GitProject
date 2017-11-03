# -*- coding: utf-8 -*-
import pygame, time, os, sys
from pygame.locals import *

#----------------------------------#
#      Definição de Classes        #
#----------------------------------#

class Arcanine(object):
	def __init__(self, name):
		self.name = name

	def moveLeft(self):
		for i in range(4):
			if i % 2 == 0:
				pygame.display.flip()
				screen.fill(0)
				screen.blit(mapa, mappos)
				arcapos[0] = arcapos[0] - 8
				screen.blit(arcaLeft1, arcapos)
				time.sleep(0.07)
			else:
				pygame.display.flip()
				screen.fill(0)
				screen.blit(mapa, mappos)
				arcapos[0] = arcapos[0] - 8
				screen.blit(arcaLeft2, arcapos)
				time.sleep(0.07)

	def moveRight(self):
		for i in range(4):
			if i % 2 == 0:
				pygame.display.flip()
				screen.fill(0)
				screen.blit(mapa, mappos)
				arcapos[0] = arcapos[0] + 8
				screen.blit(arcaRight1, arcapos)
				time.sleep(0.07)
			else:
				pygame.display.flip()
				screen.fill(0)
				screen.blit(mapa, mappos)
				arcapos[0] = arcapos[0] + 8
				screen.blit(arcaRight2, arcapos)
				time.sleep(0.07)

	def moveDown(self):
		for i in range(4):
			if i % 2 == 0:
				pygame.display.flip()
				screen.fill(0)
				screen.blit(mapa, mappos)
				arcapos[1] = arcapos[1] + 8
				screen.blit(arcaDown1, arcapos)
				time.sleep(0.07)
			else:
				pygame.display.flip()
				screen.fill(0)
				screen.blit(mapa, mappos)
				arcapos[1] = arcapos[1] + 8
				screen.blit(arcaDown2, arcapos)
				time.sleep(0.07)
	
	def moveUp(self):
		for i in range(4):
			if i % 2 == 0:
				pygame.display.flip()
				screen.fill(0)
				screen.blit(mapa, mappos)
				arcapos[1] = arcapos[1] - 8
				screen.blit(arcaUp1, arcapos)
				time.sleep(0.07)
			else:
				pygame.display.flip()
				screen.fill(0)
				screen.blit(mapa, mappos)
				arcapos[1] = arcapos[1] - 8
				screen.blit(arcaUp2, arcapos)
				time.sleep(0.07)

#-------------------------------------------------------#
#-------------------------------------------------------#
#            AQUI COMEÇA A PORRA DO CÓDIGO              #
#-------------------------------------------------------#
#-------------------------------------------------------#

#----------------------------------#
#      Definição de Tela        #
#----------------------------------#

#Dimensao da tela
screenDimension = (384, 365)
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
#Arca Sprites
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

keys = [False, False, False, False]
mappos = [0,0]
mapa = pygame.image.load("./src/frpallet.png")

# FIRST FRAME
pygame.display.flip()
screen.fill(0)
screen.blit(mapa, mappos)
screen.blit(arcaLeft2, arcapos)

while True:
	pygame.display.flip()
	screen.fill(0)
	screen.blit(mapa, mappos)

	if arcaDir == "a":
		screen.blit(arcaLeft2, arcapos)
	elif arcaDir == "d":
		screen.blit(arcaRight2, arcapos)
	elif arcaDir == "s":
		screen.blit(arcaDown2, arcapos)
	elif arcaDir == "w":
		screen.blit(arcaUp2, arcapos)

	

	

	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:
			if event.key == K_w:
				arca.moveUp()
				#keys[0] = True
				arcaDir = "w"
			elif event.key == K_s:
				#keys[1] = True
				arca.moveDown()
				arcaDir = "s"
			elif event.key == K_a:
				#keys[2] = True
				arca.moveLeft()
				arcaDir = "a"
			elif event.key == K_d:
				#keys[3] = True
				arca.moveRight()
				arcaDir = "d"

		if event.type == pygame.KEYUP:
			if event.key == K_w:
				keys[0] = False
			elif event.key == K_s:
				keys[1] = False
			elif event.key == K_a:
				#keys[2] = False
				pass
			elif event.key == K_d:
				#keys[3] = False
				pass

		if keys[0]:
			pass
		elif keys[1]:
			pass
		if keys[2]:
			arca.moveLeft()
		elif keys[3]:
			arca.moveRight()	

		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)