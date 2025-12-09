# Builtin input é utilizado quando deseja-se ler dados de entrada do usuario. Esses dados chega ao programa como uma String, independente do tipo de dado informado pelo usuario.

nome = input('Qual o seu nome? ')
ano_nascimento = input('Informe o ano em que você nasceu: ')
print(type(ano_nascimento))

print(2025 - int(ano_nascimento))

# print(2025 - ano_nascimento) esta forma estaria incorreta visto que a informação do ano de nascimento, por ser entrada do usuario, seria uma String o que causaria erro no programa. 

print(nome)
