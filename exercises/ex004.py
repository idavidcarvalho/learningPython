"""Ler algo digitado pelo teclado e mostrar na tela seu tipo primitivo
e todas as informações possíveis sobre ele"""

something = input('Digite algo: ')

print('o tipo primitivo do texto digitado é {}'.format(type(something)))
print('O texto digitado é numérico? {}'.format(something.isnumeric()))
print('O texto digitado é alfabético {}'.format(something.isalpha()))
print('O texto digitado é alfanumérico? {}'.format(something.isalnum()))
print('O texto digitado é minúsculo? {}'.format(something.islower()))
print('O texto digitado é maiúsculo? {}'.format(something.isupper()))
print('O texto digitado é decimal? {}'.format(something.isdecimal()))
print('O texto digitado é um espaço? {}'.format(something.isspace()))











