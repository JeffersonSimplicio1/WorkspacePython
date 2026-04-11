#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#Desconto do IR: - Salário Bruto até 900 (inclusive) - isento - Salário Bruto até 1500 (inclusive) - desconto de 5% - Salário Bruto até 2500 (inclusive) - desconto de 10% - Salário Bruto acima de 2500 - desconto de 20%

#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#Salário Bruto: (5 * 220)        : R$ 1100,00
#(-) IR (5%)                     : R$   55,00
#(-) INSS ( 10%)                 : R$  110,00
#FGTS (11%)                      : R$  121,00
#Sindicato (3 %)                 : R$   33,00
#Total de descontos              : R$  198,00
#Salário Liquido                 : R$  902,00

valorHora = float(input('Digite o valor da hora trabalhada: '))
quantHoras = int(input('Quantas horas foram trabalhadas? '))
salarioBruto = valorHora * quantHoras
#
if salarioBruto <= 900.00:
    iR = 0
elif 900.00 < salarioBruto <= 1500.00:
    iR = 0.05
elif 1500.00 < salarioBruto <= 2500.00:
    iR = 0.1
else:
    iR = 0.2
#    
DescontoIR = salarioBruto * iR
inss = salarioBruto * 0.1
sindicato = salarioBruto * 0.03
fgts = salarioBruto * 0.11
salarioLiquido = salarioBruto - DescontoIR - sindicato - inss

print()
print("-=" * 30)
print()

print(f'Salário Bruto:       : R$ {salarioBruto:.2f}')
print(f'(-) IR ({int(iR*100)}%)          : R$ {DescontoIR:.2f}')
print(f'(-) INSS(10%)        : R$ {inss:.2f}')
print(f'FGTS (11%)           : R$ {fgts:.2f}')
print(f'Sindicato            : R$ {sindicato:.2f}')
print(f'Total de descontos   : R$ {DescontoIR + inss + sindicato:.2f}')
print(f'Salário Liquido      : R$ {salarioLiquido:.2f}')

