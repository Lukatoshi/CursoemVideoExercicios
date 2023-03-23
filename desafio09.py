#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada;

n = int(input('Write one number: '))

for count in range(10):
    print('{} x {} = {}'.format(n, count+1, n * (count + 1)))