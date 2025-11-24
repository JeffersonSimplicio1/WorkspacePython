#Operadores de Identidade

curso ='Curso de Python'
nome_curso = curso
saldo = 200
limite = 200

pertence = curso is nome_curso
print(pertence)

pertence = curso is not nome_curso
print(pertence)

pertence = saldo is limite
print(pertence)
