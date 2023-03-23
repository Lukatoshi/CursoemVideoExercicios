#Desenvolva um programa que leia uma variavel e mostre o máximo de informações sobre ela e seu tipo;


n =input('Digite algo: ')
print(type(n))
print('é um alphanumerico? ', n.isalnum())
print('é um número? ', n.isnumeric())
print('é Ascii?', n.isascii())
print('Está capitalizado? ', n.capitalize())
print('É um digito? ', n.isdigit())
print('É alphabético?', n.isalpha())
print('É decimal? ', n.isdecimal())
print('É um identificador? ', n.isidentifier())
print('Está em minusculo? ', n.islower())
print('É printavel? ', n.isprintable())
print('Está em maiusculo? ', n.isupper())
print('É um titulo?', n.istitle())
print('como fica em casefold? ', n.casefold())
