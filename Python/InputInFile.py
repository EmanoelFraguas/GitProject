from itertools import chain

def insert_file():
	vet = []
	subVet = []
	for j in range(2):
		subVet = []
		for i in range(2):
			subVet.append(raw_input())
		vet.append(subVet)

	file = open("filename.txt", "w")
	file.close()

	file = open("filename.txt", "w")
	for j in range(2):
		for i in range(2):
			file.write(vet[i][j]+'\n')
	file.close()

	file = open("filename.txt", "r")
	print(file.read())
	file.close()


insert_file()