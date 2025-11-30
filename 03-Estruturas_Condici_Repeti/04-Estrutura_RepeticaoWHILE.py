""" opcao = -1

while opcao != 0:
    opcao = int(input("Escolha uma opção: \n" \
    "[1] Sacar\n" \
    "[2] Extrato\n" \
    "[0] Sair\n"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    ("Obrigado por utilizar nossos sistemas") """



#Exemplo

#Criar um programa que vai solicitar um numero ao usuario. Se o numero inserio for par o programa informa que o numero é par e continua executando, caso seja impar o programa informa que o numero é impar e sera encerrado.

numero = -1

while numero != 0:
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        print("O numero é par!")
        print()
        numero = int(input("Digite um numero: "))
        print("O numero é par!")
        print()
    else:
        print("O numero é impar!\n" \
        "      Programa finalizado!")
        break
