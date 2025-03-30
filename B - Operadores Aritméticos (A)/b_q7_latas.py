# Escreva um programa que calcule quantas latas de tinta são necessárias para pintar uma área.

# Entrada

area = float(input('Insira o valor da área em metros: '))
lata_area = float(input('Insira quantos metros uma lata de tinta cobre: '))

# Processamento

lata_numero = area / lata_area

# Saída

print(f'O número de latas necessária é ==> {lata_numero:.2f}')
