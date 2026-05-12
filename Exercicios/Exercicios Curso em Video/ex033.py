#programa para aprovar um emprestimo bancario para a compra de um imovel. O programa vai perguntar o valor do imovel,
# o salario do comprador e em quantos anos ele pretende pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do valor do salario ou então o emprestimo será negado..
preto =  '\033[0;30;40m'
vermelho = '\033[0;31;40m'
verde = '\033[0;32;40m'
amarelo = '\033[0;33;40m'
azul = '\033[0;34;40m'
magenta = '\033[0;35;40m'
ciano = '\033[0;36;40m'
branco= '\033[0;37;40m'
padrao ='\033[m'


valor_imovel = float(input('Qual o valor do imovel que você pretende comprar: '))
salario = float(input('Qual o valor do salario do comprador do imovel: '))
tempo = int(input(f'Em quanto tempo {vermelho}(Em anos) {padrao}você pretende pagar o imovel: '))


tempo_meses = tempo * 12
prestacao = valor_imovel / tempo_meses

if(prestacao > salario*0.3):
    print('Infelizmente o emprestimo não pode ser concluido!\n'
          f'{amarelo}O valor da prestação ficou maior do que a margem de segurança do cliente\n{padrao}'
          'faça uma nova simulação com um tempo maior para pagamento ou verifique um imovel com menor valor.')
else:
    print(f'{amarelo}Parabéns!!!{padrao}\n'
          'Seu emprestimo foi aproovado! \n'
          f'O valor da prestação é: {vermelho}{prestacao:.2f}{padrao} e você deverá pagar o imovel em {ciano}{tempo_meses}{padrao} meses')

print('Obrigado por utilizar nossos serviços!')