"""
    Escreva um programa que leia um valor em
    metros e o exiba convertido para centímetros
    e milímetros
"""

meters = int(input('Digite o valor em metros: '))
metersToCentimeters = meters*100
metersToMelimeters = meters*1000
print('{}m em centímetros é {}cm e em milímetros é {}mm34'.format(meters, metersToCentimeters, metersToMelimeters))