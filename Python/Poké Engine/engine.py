# -*- coding: utf-8 -*-
import pygame, time, os, sys
from pygame.locals import *

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
				screen.blit(arca1, arcapos)
				time.sleep(0.07)
			else:
				pygame.display.flip()
				screen.fill(0)
				screen.blit(mapa, mappos)
				arcapos[0] = arcapos[0] - 8
				screen.blit(arca2, arcapos)
				time.sleep(0.07)
	

#-------------------------------------------------------#
#-------------------------------------------------------#
#            AQUI COMEÇA A PORRA DO CÓDIGO              #
#-------------------------------------------------------#
#-------------------------------------------------------#

#Dimensao da tela
screenDimension = (384, 365)
#Chama a funcao que seta o tamanho da tela
screen = pygame.display.set_mode(screenDimension, 0, 32)
#Nome da tela
pygame.display.set_caption('Pokémon')
#Set icone
a = pygame.image.load("./src/pb.png")
pygame.display.set_icon(a)

#------------------
keys = [False, False, False, False]
mappos = [0,0]
arca1 = pygame.image.load("./src/arca1.png")
arca2 = pygame.image.load("./src/arca2.png")
mapa = pygame.image.load("./src/frpallet.png")
arcapos =[180, 180]
arca = Arcanine("Arcanine")

# FIRST FRAME
#pygame.display.flip()
#screen.fill(0)
#screen.blit(mapa, mappos)
#screen.blit(arca2, arcapos)

while True:
	pygame.display.flip()
	screen.fill(0)
	screen.blit(mapa, mappos)
	screen.blit(arca2, arcapos)
	

	

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
			pass
		elif keys[1]:
			pass
		if keys[2]:
			arca.moveLeft()
		elif keys[3]:
			pass	

		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)