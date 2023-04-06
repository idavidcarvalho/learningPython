"""
    Faça um algoritimo que leia o preço de um produto
    e mostre seu novo preço, com 5% de desconto.
"""

price = float(input('Digite o preço do produto: '))
discount = price - (price*5)/100
print('O novo preço do produto é R$ {}'.format(discount))