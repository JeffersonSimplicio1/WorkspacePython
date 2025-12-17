'''
********* Dicionarios ************

Conjunto não ordenado de pares chave:valor, onde as chaves são unicas em uma dada instancia do dicionario. Dicionarios são delimitados por chaves: {}, e contem uma lista de pares chaves:valor separada por virgulas.

*** Formas de criar um dicionario

pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome ="Guilherme", idade =28)

*** Adicionando nova chave ao dicionario

pessoa ["telefone"] = "1234-1234"

*** Acessando as chaves
 A forma de acesso as chaves é parecida com a forma de adição das chaves porem a diferença é que a forma de acesso não possui atribuição após a igualdade

dados["nome"]  acessa a chave nome
dados["idade"] acessa a chave idade
dados["telefone"] acessa a chave telefone

******* Dicionarios aninhados ************

Dicionarios dentro de outro dicionario

Ex:
contatos ={
 "jefferson@gmail.com" : {"nome: "Jefferson", "telefone": "1234-1234"}
 "regina@gmail.com" : {"nome: "Regina", "telefone": "1234-4321"}
 "benjamin@gmail.com" : {"nome: "Benjamin", "telefone": "4321-1234"}
 "cibele@gmail.com" : {"nome: "Cibele", "telefone": "1243-4231"}
}

Dentro do dicionario Contatos existe chaves com email e dentro dessa chaves existe um novo dicionario com chaves nome e telefone

'''

# Testando

pessoa = dict(nome= "florencio", idade = 23, email = "florencio@gmail.com")
nome = pessoa["nome"]
email = pessoa["email"]
idade = pessoa["idade"]

print(nome)
print(email)
print(idade)

print("----------------------------------------------------------------------")

contatos = {
    "cibele@gmail.com" : {"nome": "Cibele", "telefone": "1243-4231"},
    "benjamin@gmail.com" : {"nome": "Benjamin", "telefone": "4321-1234"},
    "regina@gmail.com" : {"nome": "Regina", "telefone": "1234-4321"},
    "jefferson@gmail.com" : {"nome": "Jefferson", "telefone": "1234-1234"},

}

pessoa1 = contatos["cibele@gmail.com"]["telefone"]
print(pessoa1)