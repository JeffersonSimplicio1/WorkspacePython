id_funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

salario = horas_trabalhadas * valor_hora

print(f'NUMBER = {id_funcionario}\nSALARY = U$ {salario:.2f}')