def readFile():
	vet = []
	file = open("filename.txt", "r")
	for j in range(2):
		subVet = []
		for i in range(2):
			subVet.append(int(file.readline().strip('\n')))
		vet.append(subVet)
	file.close()

	print vet

readFile()