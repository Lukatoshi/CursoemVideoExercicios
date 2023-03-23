#crie um algoritmo que leia um número e mostre o seu dobro(**2), triplo(**3) e raiz quadrada(**1/2);
#pow(n, (1/2)) também calcula raiz quadrada

n = int(input('Digite um número: '))

print('Seu número é {}. \nSeu dobro é {}. \nSeu triplo é {}. \nSua raiz quadrada é {:.2f}.'.format(n, (n * 2), (n * 3), (n **(1/2))))