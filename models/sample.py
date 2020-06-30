lista = [1,2,2,2,2,5,8,7,9,6,8]

store_repeat = {}
lista_palabra = []
palabra = input(">>: ")
letra = input(">>Letra cualquiera: ")



for z in range(0, len(palabra)):
    lista_palabra.append(" _ ")

for w in lista_palabra:
    print(w, end="")

print("\n")


for i,j in enumerate(palabra):
    print("la i %s y la j %s"%(i,j))
    store_repeat[i] = j

for x in range(0, len(palabra)):
    if(letra == store_repeat[x]):
        #for a,b in enumerate(lista_palabra):
        lista_palabra[x] = letra
            
for w in lista_palabra:
    print(w, end="")

print("\n")


print(store_repeat)

"""for k in range(len(lista)):
    m=[i for i, x in enumerate(lista) if lista.count(x)>1]
    print(m)

    
"""
##print(len(lista))

#print(lista.index(2))