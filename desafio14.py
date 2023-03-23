#Escreva um programa que converta uma temperatura digitando em graus Celsius e convertas para graus Fahrenheit;

temp = float(input('Quantos Graus Celsius vocês deseja converter? '))

fah = (temp * 1.8) + 32

print('{}ºC em Fahrenheit são {}ºF'.format(temp, fah))