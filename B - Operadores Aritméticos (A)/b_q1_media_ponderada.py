# Escreva um programa que calcule a média ponderada de três notas, considerando seus respectivos pesos.

# Entrada

notaA = float(input('Insira a primeira nota: '))
pesoA = float(input('Insira o peso da primeira nota: '))
notaB = float(input('Insira a segunda nota: '))
pesoB = float(input('Insira o peso da segunda nota: '))
notaC = float(input('Insira a terceira nota: '))
pesoC = float(input('Insira o peso da terceira nota: '))

# Processamento

media_ponderada = (notaA * pesoA + notaB * pesoB + notaC * pesoC) /  (pesoA + pesoB + pesoC)

# Saída

print(f'A média ponderada das notas ==> {media_ponderada:.2f}')
