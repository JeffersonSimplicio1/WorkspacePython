velocidade = float(input("Qual a velocidade do veiculo??"))
if(velocidade > 80.00):
 print("Você foi multado.")
 multa = (velocidade - 80.00) * 7.00
 print(f'O valor da multa é: R${multa:.2f}')