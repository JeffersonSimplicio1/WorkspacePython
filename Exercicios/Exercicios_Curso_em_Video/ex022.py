numero =int(input('Digite um numero: '))
print(f'Analisando o numero {numero}')
u = numero // 1 % 10
d = numero //10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'Unidade: {u}\n'
      f'Dezena: {d}\n'
      f'Centena: {c}\n'
      f'Milhar: {m}')
