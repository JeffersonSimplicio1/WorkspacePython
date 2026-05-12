# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os
# experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas
# no laboratório e o percentual de cada tipo de cobaia utilizada.
#
# Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe
# exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas
# em cada experimento

eventos = int(input('Qunatos testes serão feitos ao todo? '))
cont=1
quantidadeTotal = 0
totalCoelhos = 0
totalRatos = 0
totalSapos = 0

while cont < eventos:
    quantidade = int(input('Quantas cobaias foram utilizadas nesse evento? '))
    quantidadeTotal += quantidade

    tipo = str(input('Qual o tipo de cobaia utilizada\nC = Coelhos\nR = Ratos\nS = Sapos\n ->').strip().upper())
    if tipo == 'C':
        totalCoelhos+=quantidade
    elif tipo == 'R':
        totalRatos += quantidade
    elif tipo == 'S':
        totalSapos +=quantidade
    cont +=1
print(f'Quantidade total de individuos = {quantidadeTotal}')
print(f'Total de Coelhos = {totalCoelhos}')
print(f'Total de Ratos = {totalRatos}')
print(f'Total de Sapos = {totalSapos}')
print(f'Percentual de Coelhos: {(totalCoelhos*100)/quantidadeTotal:.2f} %')
print(f'Percentual de Ratos: {(totalRatos*100)/quantidadeTotal:.2f} %')
print(f'Percentual de Sapos: {(totalSapos*100)/quantidadeTotal:.2f} %')




