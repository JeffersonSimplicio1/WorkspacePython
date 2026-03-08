# mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

tabuada = int(input('Qual a tabuada que você deseja saber? '))

for t in range (1,11):
    resp = tabuada * t
    print(f'{tabuada} * {t} = {resp}' )
print('Obrigado!')
