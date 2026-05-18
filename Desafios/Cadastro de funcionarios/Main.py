import Program

print(f'Cadastro de Funcionarios!')
print('==' * 15)
print('Este programa te ajudara a cadastrar e manter informações sobre os seus funcionarios.')


while True:
    opcao = int(input('Digite o numero da opção desejada:\n'
                      '1 - Cadastrar funcionário\n'
                      '2 - Listar funcionários\n'
                      '3 - Mostrar media salarial\n'
                      '4 - Funcionário com o maior salário\n'
                      '5 - Funcionário com o menor salário\n'
                      '6 - Sair\n'
                      '-->  '))

    Program.escolha(opcao)

