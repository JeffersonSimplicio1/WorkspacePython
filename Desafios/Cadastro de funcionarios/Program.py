import datetime
import random

quadro_de_funcionarios = []
salarios = []
funcionario = {}
maior_salario = 0
colab_maior_remuneracao = ''
menor_salario = 0
colab_menor_remuneracao = ''
count = 0

def escolha (a):
    global maior_salario, colab_maior_remuneracao, menor_salario, colab_menor_remuneracao, count
    while True:
        if a == 1:
            funcionario['nome'] = str(input('Nome do funcionario: '))
            funcionario['id'] = random.randint(9999, 999999)
            ano_de_nascimento = int(input('Ano de nascimento: '))
            ano_atual = datetime.datetime.today().year
            idade = ano_atual - ano_de_nascimento
            funcionario['idade'] = idade
            funcionario['cargo'] = str(input('Cargo: '))
            remuneracao = float(input('Salário: '))
            if count == 0:
                maior_salario = remuneracao
                menor_salario = remuneracao
                colab_menor_remuneracao = funcionario['nome']
                colab_maior_remuneracao = funcionario['nome']
                count +=1
            if remuneracao > maior_salario:
                maior_salario = remuneracao
                colab_maior_remuneracao = funcionario['nome']
                count+=1
            if remuneracao < menor_salario:
                menor_salario = remuneracao
                colab_menor_remuneracao = funcionario['nome']

            funcionario['salario'] = remuneracao
            salarios.append(remuneracao)

            quadro_de_funcionarios.append(funcionario.copy())
            funcionario.clear()
            break
        elif a == 2:
            if len(quadro_de_funcionarios) > 0:
                for i in quadro_de_funcionarios:
                    for n, v in i.items():
                        print(f'{n} = {v} ')
                    print('---' * 20)
                break
            else:
                print(f'Não há funcionarios cadastrados!')
                break
        elif a == 3:
            if len(salarios) > 0:
                media = sum(salarios) / len(salarios)
                print(f'A media salarial dos funcionarios listados é: {media}')
                break
            else:
                print(f'Não há funcionarios cadastrados!')
                break
        elif a == 4:
            if maior_salario > 0:
                print(f'O funcionario com o maior salario é {colab_maior_remuneracao}.\n'
                  f'{colab_maior_remuneracao} recebe o valor de R$ {maior_salario}')
                break
            else:
                print(f'Não há salarios cadastrados!')
                break
        elif a == 5:
            if menor_salario > 0:
                print(f'O funcionario com o menor salario é: {colab_menor_remuneracao}\n'
                  f'{colab_menor_remuneracao} recebe o valor de R$ {menor_salario}')
                break
            else:
                print(f'Não há salarios cadastrados!')
                break
        elif a == 6:
            print(f'Finalizando programa!')
            exit()

