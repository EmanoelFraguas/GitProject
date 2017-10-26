from itertools import chain

def insert_file(filename):
    with open(filename, "w") as file:
        matrix = []
        for i in range(2):
            row = []
            for j in range(2):
                row.append(raw_input())
            matrix.append(row)
        file.write("\n".join(chain(*matrix)))
        
def read_file(filename):
    with open(filename, "r") as file:
        matrix = []
        for i in range(2):
            row = []
            for j in range(2):
                row.append(int(file.readline().strip()))
            matrix.append(row)
    return matrix
        
insert_file("data.txt")
data = read_file("data.txt")

print(data)