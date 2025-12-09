#Em python existem 3 formas de interpolar variaveis em strings, usando o sinal %, utilizando o metodo format e f Strings.

nome = "Jefferson"
idade = 31
profissao = "Programador"
linguagem = "Python"


print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso %s." %(nome,idade,profissao,linguagem))

#OBS: A forma % é antiga e pouquissimo usada entre os programadores.
print("----------------------------------------------------------------------------------------------------------------------------")

print(f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso {linguagem}.')
#Obs: f String mais utilizado e recomendado.

print("----------------------------------------------------------------------------------------------------------------------------")

print('Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso {}.'.format(nome,idade,profissao,linguagem))
print('Olá, me chamo {1}. Eu tenho {2} anos de idade, trabalho com {3} e estou matriculado no curso {0}.'.format(linguagem,nome,idade,profissao))

# O metodo format pode ser utilizado de varias formas, sendo acima exemplos de como utilizar.  
