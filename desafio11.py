#Faça um programa que leia a largura e a altura de uma parede em metrosm calcule a sua área e a quantidade
#de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma ária de 2m²;
print('{:=^25}'.format('Metros'))
larg = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
tinta = (larg * alt) / 2
print('{}m² de parede, precisam de {} L de tinta'.format(larg * alt, tinta))
