# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:

# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*nota, situacao = False ):
    r = {}
    r['total'] = len(nota)
    r['maior'] = max(nota)
    r['menor'] = min(nota)
    r['media'] = sum(nota)/len(nota)

    if situacao:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media']  >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'

    return r


resp = notas(5.2,6.3,4.1,4)
print(resp)


