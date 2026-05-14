import calcular

print('==='*15)
print('                      Calculadora de areas!!')
print('==='*15)

decisao = int(input('selecione qual figura você deseja calcular a area:\n'
                    '1 -  Quadrado\n'
                    '2 - Triângulo\n'
                    '3 - Circulo\n'
                    '4 - Retângulo\n'
                    '5 - Trapézio\n'
                    '6 - Losangoz\n'
                    '->'))

calcular.escolha(decisao)