import datetime
import random

quadro_de_funcionarios = []


def opcao(num):
    if num == 1:
        cadastrar()
    elif num == 2:
        listar_funcionarios()
    elif num == 3:
        media_salarial()
    elif num == 4:
        salario_alto()
    elif num == 5:
        salario_baixo()
    elif num == 6:
        finalizar_programa()


def cadastrar():
    funcionario = {}

    funcionario['nome'] = str(input('Nome do funcionário: '))
    funcionario['id'] = random.randint(9999, 999999)
    ano_de_nascimento = int(input('Ano de nascimento: '))
    ano_atual = datetime.datetime.today().year
    idade = ano_atual - ano_de_nascimento
    funcionario['idade'] = idade
    funcionario['cargo'] = str(input('Cargo: '))
    funcionario['salario'] = float(input('Salário: '))

    quadro_de_funcionarios.append(funcionario)

def listar_funcionarios():
    if len(quadro_de_funcionarios) > 0:
        for i in quadro_de_funcionarios:
            for n, v in i.items():
                print(f'{n} = {v} ')
            print('---' * 20)

    else:
        print(f'Não há funcionarios cadastrados!')

def media_salarial():
    if len(quadro_de_funcionarios) > 0:
        media = sum(funcionario['salario']
                    for funcionario in quadro_de_funcionarios) / len(quadro_de_funcionarios)
        print(f'A media salarial dos funcionarios listados é: {media:.2f}')

    else:
        print(f'Não há funcionarios cadastrados!')

def salario_alto():
    if len(quadro_de_funcionarios) > 0:
        maior = max(quadro_de_funcionarios, key=lambda funcionario: funcionario['salario'])

        print(f' Funcionário: {maior["nome"]}\n Salário: R$ {maior["salario"]:.2f}')

    else:
        print(f'Não há salarios cadastrados!')

def salario_baixo():
    if len(quadro_de_funcionarios) > 0:
        menor = min(quadro_de_funcionarios, key=lambda funcionario: funcionario['salario'])

        print(f'Funcionário: {menor['nome']}\n Salário: R${menor['salario']:.2f}')

    else:
        print(f'Não há salarios cadastrados!')

def finalizar_programa():
    print(f'Finalizando programa!')
    exit()
