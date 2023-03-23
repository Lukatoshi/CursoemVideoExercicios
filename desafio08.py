#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros;

metros = float(input('Quantos metros?'))
print('{}km;\n{}hm;\n{}dam;'.format((metros / 1000), (metros / 100), (metros / 10)))
print('{}dm;\n{}cm;\n{}ml;'.format((metros * 10), metros * 100, metros * 1000 ))