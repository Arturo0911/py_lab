# para crear una matriz dentro de una matriz
# osea que,que haya una matriz de 4x4 y que haya una matriz de 4x4 dentro de cada uno de ellos.
import random
data_rand = [0,1]


matriz = []
matriz_1 = []
matriz_2 = []
def create_matriz():

    for fila in range (0,4):
        lista =  list()
        
        for columna in range (0,4):
            lista.append(data_rand[random.randint(0,1)])
        matriz.append(lista)

    for l in range(0,4):
        for m in range(0,4):
            
            matriz_1.append(matriz)
        matriz_2.append(matriz_1)

    for x in matriz_2:
        for y in range(0,4):
            for z in range(0,4):

                print(" %s\n"%matriz_2[y][z])
            print(end="")
        #print("\n %s \n"%x)
        


create_matriz()