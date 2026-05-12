# DocStrings : manual que sera exibido durante a ajuda interativa do python

def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
     - I = inicio da contagem
     - F = Fim da contagem
     - P = Passo da contagem
     - return: Sem retorno
    """
    c=i
    while c<=f:
        print(f'{c} ', end='')
        c+=p
    print('FIM')

# contador(0,100,10)

# Parametros opcionais

# def somar(a,b,c):
#     s = a+b+c
#     print(f'A soma dos numeros é {s}')

    # Na função somar obrigatoriamente, para ser utilizada, devera ter os parametros a,b,c. Caso algum desses parametros não exista a função não poderar ser executada.
# Para solucionar esse problema utiliza-se os parametros opcionais deixando a função da seguinte forma:

     # def somar(a =0, b= 0, c=0):
     #         s = a + b + c
     #        print(f'A soma dos numeros é {s}')

# desta forma, caso ocorra a inxistencia de um dos paremetros (a,b,c) ele sera igual a 0, podendo assim utilizar normalmente a função


