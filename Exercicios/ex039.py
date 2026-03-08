# Refaça o DESAFIO 32 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('***' * 15)
print('*   Saiba se três retas podem formar um triângulo   *')
print('***' * 15)

reta_a = int(input("Insira o valor da reta A: "))
print('---' * 15)
reta_b = int(input('Insira o valor da reta B: '))
print('---' *15)
reta_c = int(input('Insira o valor da reta C: '))
print('===' *15)

if(reta_a + reta_b > reta_c and reta_a + reta_c > reta_b and reta_b + reta_c > reta_a):
    print(f'Os segmentos de reta podem formar um triangulo')
    if(reta_a == reta_b and reta_b == reta_c):
        print(f'As retas informadas formam um triângulo Equilátero')
    elif(reta_a == reta_b and reta_a != reta_c or reta_b == reta_c and reta_c != reta_a or reta_a == reta_c and reta_a != reta_b):
        print(f'As retas informadas formam um triangulo Isósceles')
    else:
        print(f'As retas informadas formam um triângulo Escaleno')
else:
    print('Os segmentos NÃO podem formar um triangulo')