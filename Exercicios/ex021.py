nome = input("Qual o seu nome completo? ")
print(f'Maiusculas: {nome.upper()}')
print(f'Minuscula: {nome.lower()}')
print(f'Quantidade de letras sem os espaços: {len(nome) - nome.count(" ")}')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem { len(separa[0]) } letras')

