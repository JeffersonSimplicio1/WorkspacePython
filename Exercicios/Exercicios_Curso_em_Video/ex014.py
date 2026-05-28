km_percorridos = float(input("Quantos quilometros voce percorreu? "))
dias_alugados = float(input("Quantos dias você alugou o veiculo? "))
valor_aluguel = dias_alugados *60
valor_distancia = km_percorridos*0.15
tota_a_pagar = valor_distancia + valor_aluguel

print(f'O valor a pagar é R${tota_a_pagar:.2f}')