import math

cateto_oposto = float(input("Qual o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Qual o comprimento do cateto adjacente: "))


hipotenusa = math.sqrt(math.pow(cateto_oposto,2) +math.pow(cateto_adjacente,2))
print(f'O valor da hipotenusa é: {hipotenusa:.2f}')