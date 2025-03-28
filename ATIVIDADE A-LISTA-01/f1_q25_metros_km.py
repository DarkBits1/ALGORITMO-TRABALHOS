# Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.

# Entrada

valor_metros = float(input('Insira o valor em metros: '))

# Processamento

valor_km = valor_metros // 1000
final_metros = valor_metros % 1000

# Saída

print(f'O valor em km e metros seria ==> {valor_km}km e {final_metros}m')
