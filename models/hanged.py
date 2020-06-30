import random
lista_numeros = [0,1,2,3,4]
lista_palabras = ["arbitrario","investigacion","metodologia","lunes","articulo"]
lista_juego = list()
lista_intentos = list()
store_repeat = {} # almacenamos la palabra al azar con sus respectivos indices 
lista_palabra = [] # aqui las palabras se van a descomponer en letras para ser añadidas a esta lista
key_word = lista_palabras[lista_numeros[random.randint(0,4)]] # de aqui viene la palabra al azar




print("Juego del ahorcado...")
jugador = input(">>ingrese su nombre: ")
numero_intentos = 3

for z in range(0, len(key_word)):
    lista_palabra.append(" _ ")

def imprimir_lista():
    for w in lista_palabra:
        print(w, end="")

"""for m in lista_juego:
    print(m, end="")"""


for i,j in enumerate(key_word):
    #print("la i %s y la j %s"%(i,j))
    store_repeat[i] = j

while(numero_intentos > 0):


    
    imprimir_lista()
    print("\n")

    print("\n\n>>le quedan %s intentos"%numero_intentos)
    #print(">>la palabra de este juego es %s"%key_word)
       
    
    word = input(">>ingrese una letra o la palabra si es que ya la sabe: ")
    
    if (word == key_word):
        print("ACABAS DE GANAR EL JUEGO")
        break
    elif(word in key_word):
        for x in range(0, len(key_word)):
            if(word == store_repeat[x]):
                #for a,b in enumerate(lista_palabra):
                lista_palabra[x] = word
    else:
        numero_intentos = numero_intentos - 1



