try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou!')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero!')
else:
    print(f'O valor da divisão é {r}')
finally:
    print('=D')
