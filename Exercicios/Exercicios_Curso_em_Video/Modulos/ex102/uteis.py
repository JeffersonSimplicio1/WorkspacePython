def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError,NameError):
            print(f'Por favor, digite um numero inteiro valido')
            continue
        else:
            return n


def leia_real(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError,NameError):
            print(f'Valor inserido não é um numero real')
            continue
        else:
            return n

