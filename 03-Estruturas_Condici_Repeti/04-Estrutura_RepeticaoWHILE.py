opcao = -1

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
    ("Obrigado por utilizar nossos sistemas")