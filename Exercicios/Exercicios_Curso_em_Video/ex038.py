# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTE
import datetime

ano_de_nascimento = int(input("Insira o ano do seu nascimento: "))
idade = datetime.date.today().year - ano_de_nascimento

if(idade > 0 and idade <= 9):
    print(f'sua idade é: {idade}\n'
          f'você é um atleta mirim')
elif(idade > 9 and idade <= 14):
    print(f'sua idade é: {idade}\n'
          f'você é um atleta Infantil')
elif(idade > 19 and idade <=25):
    print(f'sua idade é: {idade}\n'
          f'você é um atleta Júnior')
elif(idade > 25):
    print(f'Sua idade é : {idade}\n'
          f'você é um atleta Master')
else:
    print("O ano de nascimento esta incorreto, tente novamente!")