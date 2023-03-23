#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calucle e mostre
#o comprimento da hipotenusa;
from math import sqrt, pow


catop = float(input('Digite o valor do Cateto oposto: '))
catad = float(input('Digite o valor do Cateto Adjacente: '))
hipo = sqrt(pow(catop, 2) + (pow(catad, 2)))

print('O valor da hipotenusa do triângulo retângulo é {:.2f}'.format(hipo))
