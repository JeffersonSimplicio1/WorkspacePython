def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    if inicio < fim and passo < 0:
        passo = abs(passo)
    if inicio > fim and passo > 0:
        passo = -passo

    if passo > 0:
        fim += 1
    else:
        fim -= 1

    for i in range(inicio, fim, passo):
        print(i, end=' ')
    print('Fim')


print('~' * 20)
print('Contagem de 1 a 10 de 1 em 1')
contador(1, 10, 1)

print('~' * 20)
print('Contagem de 10 a 0 de 2 em 2')
contador(10, 0, -2)

print('~' * 20)
print('Agora é sua vez de personalizar a contagem!')
comeco = int(input('Início: '))
fim = int(input('Fim: '))
pula = int(input('Passo: '))

contador(comeco, fim, pula)