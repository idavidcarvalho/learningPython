"""
    Crie um programa que leia quanto dinheiro uma
    pessoa tem na carteira e mostre quantos dólares
    ela pode comprar.

    OBS: No dia da resolução desse exercício 
    o dólar está valendo R$ 5,06, portanto esse
    será o valor utilizado na conversão
"""

reais =  float(input("Quantos reais você tem? "))
formula = reais//5.06
print("Com {} você poderá comprar exatamente {} dólares".format(reais, formula))