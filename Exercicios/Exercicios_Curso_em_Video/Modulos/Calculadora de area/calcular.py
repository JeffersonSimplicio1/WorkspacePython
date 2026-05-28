import math

def area_quadrado (lado):
    resp = lado * lado
    return resp

def area_triangulo (base,altura):
    resp = (base * altura)/2
    return resp

def area_circulo (raio):
    resp = math.pi * (raio * raio)
    return resp

def area_retangulo (base, altura):
    resp = base * altura
    return resp

def area_trapezio (base_a, base_b, altura):
    resp = ((base_a+base_b)*altura)/2
    return resp

def area_losango (diag_g, diag_p):
    resp = (diag_g*diag_p)/2
    return resp

def escolha (a):
    if a ==1:
        lado = float(input('Digite o valor do lado do quadrado: '))
        print (f'A area do quadrado é: {area_quadrado(lado)}')
    elif a == 2:
        base = float(input('Digite o valor da base do triangulo: '))
        altura = float(input('Digite a altura do triangulo: '))
        print (f' A area do triangulo é: {area_triangulo(base, altura)}')
    elif a ==3:
        raio = float(input('Digite o valor do raio do circulo: '))
        print (f' A area do circulo é: {area_circulo(raio)}')
    elif a == 4:
        base = float(input('Digite o valor da base do retangulo: '))
        altura = float(input('Digite a altura do retângulo: '))
        print (f' A area do retangulo é:  {area_retangulo(base, altura)}')
    elif a == 5:
        base_maior = float(input('Digite o valor da base maior do trapezio: '))
        base_menor = float(input('Digite o valor da base menor do trapezio: '))
        altura = float(input('Digite a altura do trapezio: '))
        print (f' A area do trapezio é:  {area_trapezio(base_maior, base_menor, altura)}')
    elif a == 6:
        diag_maior = float(input('Digite o valor da diagonal maior: '))
        diag_menor = float(input('Digite o valor da diagonal menor: '))
        print (f' A area do losango é:  {area_losango(diag_maior, diag_menor)}')
    else:
        print('Valor invalido!')