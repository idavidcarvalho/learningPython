"""
    Faça um progrma que leia a largura e altura
    de uma parade em metros, calcule a sua área 
    e a quantiade de tinta necessária para pinta-la,
    sabendo que cada litro de tinta pinta uma área de 2m².
"""

width = float(input("Digite a largura da parede: "))
heith = float(input("Digite a altura da parede: "))
area = width * heith
qtdInk = area/2
print('Voce vai precisar de aproximadamente {} litros de tinta para pintar a parede'.format(qtdInk))