distancia = float(input('Qual a distancia entre as cidades ? '))

if(distancia <= 200.00):
    passagem = distancia * 0.5
    print(f'O valor da passagem é: {passagem:.2f}')
else:
    passagem = distancia * 0.45
    print(f'O valor da passagem é: {passagem:.2f}')