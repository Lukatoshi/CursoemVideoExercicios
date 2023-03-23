#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto;
produto = float(input('Qual o valor do produto? '))
desconto = (produto/100)*5
print('O valor do seu produto é R${:.2f}, com 5% de desconto fica R${:.2f}'.format(produto, produto - desconto))
