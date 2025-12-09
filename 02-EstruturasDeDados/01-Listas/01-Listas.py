#Listas podem armazenar de maneira sequencial qualquer tipo de objeto.
# pode-se criar listas utilizando o construtor list, a função range ou colocando valores separados por virgulas dentro do conchetes

#Ex.:

frutas = ["Laranja", "Limão", "Maçã"] # Lista com o nome de frutas (Strings)

numeros = [] #Lista vazia

letras = list ('python') # Cada letra da palavra sera um elemento da lista 

numeros = list(range(10)) # Cada numero retornado pela função range sera um elemento

carro = ["Jeep", "Compass", 120000, 2025, "Recife", True] # Lista com varios tipos de elementos (String, inteiros e booleanos)


#Acessando os valores

print(frutas[1])
print(frutas[0])

#Listas Aninhadas

#São listas que armazanam outras listas. com isso podemos criar estruturas bidmensionais (Matrizes) e acessar suas informações informando linhas e colunas 

matriz =[
    [5,10,15]
    [20,25,30]
    [35,40,45]
]

matriz[0] # Resultado sera apenas a linha 0 [5,10,15]
matriz [0][0] # Retronara o valor 5
matriz[0][-1] # Retornara o ultimo valor da primeira linha 15
matriz [-1][-1] #Retronara o ultimo valor da ultima linha
