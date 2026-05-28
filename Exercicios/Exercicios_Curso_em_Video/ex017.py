import math
angulo =  float(input("Digite o angulo a ser calculado o seno, cosseno e tangente: "))
radiando = math.radians(angulo)
seno = math.sin(radiando)
cosseno = math.cos(radiando)
tangente = math.tan(radiando)

print(f'O angulo de {angulo} tem o seno de {seno:.2f} ')
print(f'O angulo de {angulo} tem o seno de {cosseno:.2f} ')
print(f'O angulo de {angulo} tem o seno de {tangente:.2f} ')