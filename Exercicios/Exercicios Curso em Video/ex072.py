# Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais.

palavras = (
    "python", "programacao", "computador", "algoritmo", "dados",
    "variavel", "funcao", "lista", "tupla", "dicionario",
    "loop", "condicao", "codigo", "software", "hardware",
    "internet", "servidor", "cliente", "sistema", "desenvolvedor"
)

for n in palavras:
    print(f'\nNa palavra {n} temos as vogais: ',end='')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
