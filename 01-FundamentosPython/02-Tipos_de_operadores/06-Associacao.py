#Operadores de Associação
  # São operadores utilizados para verificar se um objeto esta presente em uma sequencia.

curso = 'Curso de Python'
frutas = ["Laranja","Limão","Goiaba","Manga"]
idades = [10,20,35,12,6]

verifique = "Python" in curso
print(verifique)

verifique = "Banana" not in curso
print(verifique)

verifique = 85 in idades
print(verifique)
