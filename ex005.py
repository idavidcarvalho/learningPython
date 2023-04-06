"""
    Faça um programa que leia um número inteiro e mostre
    na tela seu sucessor e seu antecessor
"""

number = int(input('Digite um número qualquer: '))
print('O sucessor de {} é {}, já o seu antcessor é {}.'.format(number, number+1, number-1))