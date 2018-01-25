# -*- coding: utf-8 -*-
import pygame, time, os, sys
from pygame.locals import *

#Dimensao da tela
screenDimension = (250, 250)
#Chama a funcao que seta o tamanho da tela
screen = pygame.display.set_mode(screenDimension, 0, 32)
#Nome da tela
pygame.display.set_caption('Pokémon')
#Set icone
a = pygame.image.load("./src/pb.png")
pygame.display.set_icon(a)

def printText(texto):
	#   MAIÚSCULAS
	aMax = pygame.image.load("./src/letras/A.png")
	bMax = pygame.image.load("./src/letras/B.png")
	cMax = pygame.image.load("./src/letras/C.png")
	dMax = pygame.image.load("./src/letras/D.png")
	eMax = pygame.image.load("./src/letras/E.png")
	fMax = pygame.image.load("./src/letras/F.png")
	gMax = pygame.image.load("./src/letras/G.png")
	hMax = pygame.image.load("./src/letras/H.png")
	iMax = pygame.image.load("./src/letras/I.png")
	jMax = pygame.image.load("./src/letras/J.png")
	kMax = pygame.image.load("./src/letras/K.png")
	lMax = pygame.image.load("./src/letras/L.png")
	mMax = pygame.image.load("./src/letras/M.png")
	nMax = pygame.image.load("./src/letras/N.png")
	oMax = pygame.image.load("./src/letras/O.png")
	pMax = pygame.image.load("./src/letras/P.png")
	qMax = pygame.image.load("./src/letras/Q.png")
	rMax = pygame.image.load("./src/letras/R.png")
	sMax = pygame.image.load("./src/letras/S.png")
	tMax = pygame.image.load("./src/letras/T.png")
	uMax = pygame.image.load("./src/letras/U.png")

	lMin = pygame.image.load("./src/letras/ll.png")
	oMin = pygame.image.load("./src/letras/oo.png")
	exclamation = pygame.image.load("./src/letras/!.png")
	vert = 50
	hor = 50
	pygame.display.flip()
	screen.fill((255, 255, 255))
	line = pygame.image.load("./src/letras/line.png")
	screen.blit(line, (0, 60))
	time.sleep(0.1)	

	for i in range(len(texto)):
		if texto[i] == "A":
			screen.blit(aMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "B":
			screen.blit(bMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "C":
			screen.blit(cMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "D":
			screen.blit(dMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "E":
			screen.blit(eMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "F":
			screen.blit(fMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "G":
			screen.blit(gMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "H":
			screen.blit(hMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "I":
			screen.blit(iMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 5
		elif texto[i] == "J":
			screen.blit(jMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "K":
			screen.blit(kMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "L":
			screen.blit(lMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "M":
			screen.blit(mMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "N":
			screen.blit(nMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "O":
			screen.blit(oMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "P":
			screen.blit(pMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "Q":
			screen.blit(qMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "R":
			screen.blit(rMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "S":
			screen.blit(sMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "T":
			screen.blit(tMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "U":
			screen.blit(uMax, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7

		# MAIÚSCULAS
		
		elif texto[i] == "l":
			screen.blit(lMin, (hor, vert))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 4
		elif texto[i] == "o":
			screen.blit(oMin, (hor, vert + 3))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 7
		elif texto[i] == "!":
			screen.blit(exclamation, (hor, vert - 1))
			pygame.display.flip()
			time.sleep(0.1)
			hor += 3

while True:
	printText("ABCDEFGHIJKLMNOPQRSTUlo!")

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)