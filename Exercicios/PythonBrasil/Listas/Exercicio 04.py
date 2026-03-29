# Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

letras = []
contCons = 0
consoante = []

print('Você deverá adicionar 10 letras do alfabeto.')
for i in range(0,10):
    letra = str(input(f'Digite a {i+1}° letra: '))
    if letra.isalpha() and letra not in 'AaEeIiOoUu':
        contCons += 1
        consoante.append(letra)
    letras.append(letra)

print(f'A lista de caracteres adicionados foram: {letras}')
print(f'Foram adicionados {len(letras)} caracteres')
print(f'Foram adicionadas {len(consoante)} consoantes')
print(f'A lista de consoantes adicionadas foram: {consoante}')