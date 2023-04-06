"""
    Faça um algoritimo que leia o salário de um funcionário
    e mostre seu novo salário, com 15% de aumento
"""

salary = float(input('Digite seu salário atual: '))
newSalary = salary + (salary*15)/100
print ('Seu novo salário com o reajuste de 15% vai ser R$ {}'.format(newSalary))