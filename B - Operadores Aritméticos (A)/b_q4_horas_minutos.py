# Escreva um programa que converta minutos para horas e minutos.

# Entrada

minutos = int(input('Insira a quantidade de minutos: '))

# Processamento

horas = minutos // 60
minutos_final = minutos % 60

# Saída

print(f'A quantidade traduz para ==> {horas} horas e {minutos_final} minutos')
