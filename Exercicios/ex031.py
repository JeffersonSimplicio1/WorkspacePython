salario = float(input('Qual o valor do salario do funcionario? '))

if(salario >1250.00):
    novo_salario = (salario *0.10) + salario
    print(f'O novo salario do funcionario é: {novo_salario}')
else:
    novo_salario = (salario * 0.15) + salario
    print(f'O novo salario do funcionario é {novo_salario}')