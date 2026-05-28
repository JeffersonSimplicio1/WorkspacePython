import calculos

valor = float(input('Digite o valor que você deseja converter em metros: '))
num = int(input('Digite:\n1 = De m para km\n2 = De m para hm\n3= De m para dam\n4 = De m para m\n5 = De m para dm\n6 = De m para cm\n7 = De m para mm\n -> '))

if num ==1 or num <=7:
    print(f' O resultado da conversão de {valor}m em {calculos.medida(num)} é: {calculos.metros_para_cent(valor, num)}')
else:
    calculos.metros_para_cent(valor,num)

