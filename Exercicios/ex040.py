# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a
# tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

altura = float(input('Insira a sua altura: '))
peso = float(input('Insira o seu peso: '))
imc = peso / (altura**2)

if(imc < 18.5):
    print(f'Seu imc é de : {imc:.2f}\n'
          f'Abaixo do peso')
elif(imc >= 18.5 and imc < 25):
    print(f'Seu imc é de : {imc:.2f}\n'
          f'Peso Ideal')
elif(imc >=25 and imc <= 30):
    print(f'Seu imc é de : {imc:.2f}\n'
          f'Sobrepeso')
elif(imc>30 and imc<=40):
    print(f'Seu imc é de : {imc:.2f}\n'
          f'Obesidade')
else:
    print(f'Seu imc é de : {imc:.2f}\n'
          f'Obesidade Morbida')