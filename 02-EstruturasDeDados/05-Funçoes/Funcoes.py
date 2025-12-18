'''
Funções

Bloco de codigo identificado por um nome. Permite organização do codigo e reutilização.
- def = palavra reservada para criar uma função
'''
#Bloco 01
def exibir_mensagem(): # função sem parametro
    print("olá mundo!")

#Bloco 02
def exibir_mensagem2(nome): # função com parametro nome
    print(f'Seja bem vindo {nome}')

def exibir_mensagem3(nome = 'Regina'):
    print(f' Seja bem vindo(a) {nome}')

#Chamando as funções
#exibir_mensagem()
#exibir_mensagem2(nome = 'Jefferson')
#exibir_mensagem3()

'''Retornando valores'''

def calcular_total(num):
    return sum(num)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero + 1

    return antecessor, sucessor

#print(calcular_total([10,20,30,50]))
#print(retornar_antecessor_e_sucessor(50))

'''Argumentos nomeados

Argumento que é passado chave e valor
'''

def salvar_funcionario(nome, matricula, cpf, setor):
    return (f'O funcionario {nome}, \npossuidor da matricula: {matricula} e \ncpf: {cpf} \ntrabalha no setor: {setor}')

#print(salvar_funcionario('jefferson', 354897, 985214599, 'Tecnologias'))
#print('---------------------------------------------------------------------------')
#print(salvar_funcionario(nome = 'João', matricula = 889758, cpf = 12345678988, setor = 'Compras'))
#print('---------------------------------------------------------------------------')
#print(salvar_funcionario(matricula = 8975896, setor = 'Saude', nome = 'Michele', cpf = 89745621355))


def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def calcular(a,b,funcao):
    resultado = funcao(a,b)
    return (f'O resultado do calculo é {resultado}')

#print(calcular(30,45, somar))
#print(calcular(80,27,subtrair))

'''Escopo Local e escopo global

Se a variavel estiver dentro da função ele é escopo local, se estiver fora da função (na raiz do programa) ele é escopo golbal
'''

salario = 2000 # variavel fora da função, ou seja, escopo global

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))