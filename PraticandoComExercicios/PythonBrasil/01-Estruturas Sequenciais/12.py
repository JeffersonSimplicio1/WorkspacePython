'''Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:

Formula
Gigabytes * 1024'''

valor_gb = float(input("Quantos gb's tem a memoria: "))
formula = valor_gb * 1024

print(f"Ela possui: {formula} Megabytes")