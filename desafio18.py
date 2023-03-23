#Faça ium programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo;
import math

angulo = int(input('Digite um ângulo qualquer entre 0º e 360º: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente =math.tan(math.radians(angulo))

print('Sobre o ângulo {} temos que:\nO seno é igual a: {};\nO cosseno é igual a: {}\nA tangente é igual a: {}'.format(angulo, seno, cosseno, tangente))
