#Maisculo, Minusculo e Titulo

curso = "JeFfErSoN"

print(curso.upper()) #Maisculo

print(curso.lower()) #Minusculo

print(curso.title()) #Apenas a primeira letra fica maiuscula

print("-------------------------------------------------------------")

#Eliminando espaços e branco

curso = "     Jefferson   "

print(curso.strip()) # remove os espaços em branco da esquerda e da direita

print(curso.lstrip()) # remove o espaço em branco da esquerda

print(curso.rstrip()) # remove o espaço em branco da direita

print("-------------------------------------------------------------")

# Junçoes e Centralizações

curso = "Jefferson"

print(curso.center(13,"*")) #Centraliza a string de acordo com a quantidade de caracters adicionado. no exemplo ficara (**Python**)

print(".".join(curso)) #Acrescenta pontos entre as letras

print("-------------------------------------------------------------")


