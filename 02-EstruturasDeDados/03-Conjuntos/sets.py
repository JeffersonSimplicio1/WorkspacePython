#Sets são coleções que não possuem repetições. 

print(set([1,2,3,4,5,6,1,2])) # 1,2,3,4,5,6

print(set(["celta", "gol","argo","mobi","polo","celta","mobi"]))

print(set("abacaxi"))


#Set não é indexavel, ou seja, Para acessar os elementos é necessario converter em lista

'''numeros = {1,2,3,4,2}

numeros = list(numeros)

print(numeros[3])'''

# Metodos do SET


conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.union(conjunto_b)) # junta os conjuntos retirando os duplicados
print(conjunto_a.intersection(conjunto_b)) # conjunto dos comuns (Interseção)
print(conjunto_a.difference(conjunto_b))# retorna o numero diferente que esta em A
print(conjunto_a.symmetric_difference(conjunto_b))# Todos os elementos que não estão na intersecção

print("---------------------------------------------------------------------------------")

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issubset(conjunto_b)) # Pergunta se o conjunto A esta contido em B; retorna um valor boolleano
print(conjunto_a.issuperset(conjunto_b))# Pergunta se o conjunto B esta contido em A; retorna um valor boolleano
print(conjunto_a.isdisjoint(conjunto_b)) # # Pergunta se o conjunto A não toca em B; retorna um valor boolleano

print("-------------------------------------------------------------------------------------")

sorteio = {1,23}

sorteio.add(25) # Adiciona um elemento
sorteio.add(15)
sorteio.add(10)
sorteio.add(5)
sorteio.copy() # Copia 
sorteio.discard(23) #Descarta o valor 
sorteio.pop() # Retira o valor da lista de tras pra frente.
sorteio.remove(0) #Remove um valor
len(sorteio) #retorna o tamanho do set
1 in sorteio #Saber se o valor esta no conjunto
sorteio.clear() # limpa
