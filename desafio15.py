#Escreva um programa que pergunte a quantidade de Km percorrigos por um carro allugado e quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R% 0,15 por Km rodado.
print('{:=^29}'.format('Aluguel de Carros'))

km = float(input('Quantos Kms foram rodados? '))
dias = int(input('Quantos dias você ficou com o carro? '))

print('Foi percorrido {}Km e o periodo que ficou com o veiculo é de {} dias '.format(km, dias))
print('O valor total do aluguel é de R${:.2f}'.format((km * 0.15) + (dias * 60)))