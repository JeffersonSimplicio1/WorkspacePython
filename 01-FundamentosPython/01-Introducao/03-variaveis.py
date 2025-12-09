# variaveis são usadas para armazenar valores que podem ser reutilizados ao longo do código. Os valores das variaveis podem mudar ao longo do programa.

#Constantes são valores que não mudam ao longo do programa. Em python, por convernção, utilizamos a palavra inteira em maiusculo para nomear uma constante. ex: CPF = '123.456.789-00'

age = 23
name = 'Jefferson'

print(f'Meu nome é {name} e eu tenho {age} anos de idade.')

print()
print()

age = 31
print(f'Meu nome é {name} e eu tenho {age} anos de idade.')

print()
print()

# Para alterar o valor de uma variavel, basta atribuir um novo valor a ela.

# utiliza-se o padrão snake_case para nomear variaveis em python. Ex: minha_variavel = 10

nome_cliente = 'Ana Maria'
cpf = '123.456.789-00'
limite_saque_diario = 5000
saldo_conta_poupanca = 15000.75

print(f'Cliente: {nome_cliente}, portador do cpf: {cpf}, possui o valor de R$ {saldo_conta_poupanca} na conta poupança e um limite de saque de: R${limite_saque_diario}')

print()
print()

# Convertendo tipos de variaveis.

limite_saque_diario = float(limite_saque_diario)
print(limite_saque_diario)
print()
saldo_conta_poupanca = int(saldo_conta_poupanca)
print(saldo_conta_poupanca)

#Para saber qual o tipo de variavel, utiliza-se type na frente da variavel ex: print(type(nome_cliente))
print(type(nome_cliente))

