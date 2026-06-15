#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Quanto o funcionario recebe por hora: "))
horas_trabalhadas = int(input("Quantas horas trabalhadas no mês: "))

valor_receber = valor_hora * horas_trabalhadas

print(f'O valor a ser recebido pelo funcionario é: {valor_receber:.2f}')

