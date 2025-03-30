# Escreva um programa que calcule o montante final em uma aplicação financeira com juros simples.

# Entrada

capital = float(input('Insira o capital: '))
juros = float(input('Insira o juros: '))
tempo = int(input('Insira o período: '))

# Processamento
juros_final = juros * 0.01 * tempo * capital
montante_final = capital + juros_final

# Saída

print(f'O valor final é ==> {montante_final}')
