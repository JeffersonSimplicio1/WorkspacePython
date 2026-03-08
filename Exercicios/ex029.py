import calendar

ano = int(input("Digite um ano para saber se ele é bissexto: "))
if(calendar.isleap(ano)):
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')