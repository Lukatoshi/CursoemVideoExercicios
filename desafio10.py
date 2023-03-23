#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
#quantos dólares ela pode comprar;     considere o valor do dólar = R$ 3,27;

n = float(input('Quanto dinheiro você tem na carteira? R$'))
dol = (n / 5.19)
print('Com R${:.2f} você consegue comprar US${:.2f}'.format(n, dol))
