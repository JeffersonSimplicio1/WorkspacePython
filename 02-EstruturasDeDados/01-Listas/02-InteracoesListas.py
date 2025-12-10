'''#é comum a utilização do for para interações com listas

carros = [["Renegade", "Compass", "Commander"],["Wrangler", "Journey","Ram"], ["Rampage","Avenger","Town Country"]]

for carro in carros:
    print(carro)


#Compressão de listas
  #VAi ler a lista e criar uma nova lista com os valores 

numeros = [1,2,3,4,5,6,7,8,9,10,15,20,99,85,7,4568,95,4,8,52,4,5,5,654,984,6514,984,654198,4165,165,121,98,4,156,56498849846510]
pares = []

for numeros in pares:
    if numeros % 2 == 0:
        pares.append(numeros)

'''


# Interação com listas

numeros = [1,2,3,4,5,6,7,8,9,10,15,20,99,85,7,4568,95,4,8,52,4,5,5,654,984,6514,984,654198,4165,165,121,98,4,156,56498849846510]

numeros.append("Python") #Adiciona o elemento da lista
print(numeros)

lista_numero = numeros.copy() #Copia a lista
print(lista_numero)

numeros.count("Python")

print(numeros.index(4568)) # Indica a posição do elemento na lista

print(numeros.pop()) # Funciona como uma pilha de pratos, O programa ira retirando os elementos do final para o começo, porém
print(numeros.pop())  # caso entre os parenteses pode-se escolher a posição do elemento a ser retirado.
print(numeros.pop(10))
print(numeros.pop())
print(numeros.pop())

print(numeros)

numeros.clear() #Limpa os elementos da lista
print(numeros)


print("------------------------------------------------------")

numeros.append("Javascript")
numeros.append("Java")
numeros.append("Python")
numeros.append("C#")
numeros.append("Ruby")
numeros.append("Typescript")
print (numeros)


numeros.remove("Typescript") # Remove um elemento.
print(numeros)

print(len(numeros)) # Retorna a quantidade de elementos na lista

numeros.reverse()# Inverte a lista escrevendo de tras pra frente.
print(numeros)
