'''Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

Para Megabytes: Gigabytes * 1024
Para Kilobytes: Gigabytes * 1024 * 1024
Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.'''

valor_gb = float(input("Qual o tamanho em GB: "))
valor_mb = valor_gb * 1024
valor_kb = valor_mb * 1024

print(f'O tamanho em MBs é: {valor_mb}\nO tamanho em Kbs é: {valor_kb}')