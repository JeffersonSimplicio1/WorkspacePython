# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota_01 = float(input("Digite a primeira nota: "))
nota_02 = float(input("Digite a segunda nota: "))
media = (nota_01 + nota_02)/2.0

if(media < 5.0):
    print(f"A media do aluno é: {media}\n"
          f"Aluno Reprovado!")
elif(media>= 5.0 and media <= 6.9):
    print(f"A media do aluno é: {media}\n"
          f"Aluno em Recuperação")
else:
    print(f'A media do aluno é: {media}\n'
          f'Aluno Aprovado')