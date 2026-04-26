# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(largura, comprimento):
    area_terreno = largura * comprimento
    return f'{area_terreno:.2f}'

# Programa Principal
dados_dos_terrenos = []
dados_primarios = {}

while True:
    dados_primarios['largura'] = float(input('Insira a largura do terreno: '))
    dados_primarios['comprimento'] = float(input('Insira o comprimento do terreno: '))
    dados_primarios['area'] = (area(dados_primarios['largura'],dados_primarios['comprimento']))
    dados_dos_terrenos.append(dados_primarios.copy())

    continua = str(input('Deseja adicionar mais um dados para calculo da area [S/N]? ').upper().strip())

    if continua == 'N':
        print()
        for indice in dados_dos_terrenos:
            for chave, valor in indice.items():
                print(f'A {chave} do terreno é de {valor}')
            print('---')
        break
    elif continua != 'S':
        print('---\nValor não corresponde com as opções.\n    Finalizando programa!!!\n     ----')
        for indice in dados_dos_terrenos:
            for chave, valor in indice.items():
                print(f'A {chave} do terreno é de {valor}')
            print('---')
        break

