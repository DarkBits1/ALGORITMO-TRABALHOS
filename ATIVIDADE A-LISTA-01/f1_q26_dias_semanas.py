# Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

# Entrada

valor_dias = int(input('Insira o valor em dias: '))

# Processamento

valor_semanas = valor_dias // 7
valor_dias_final = valor_dias % 7

# Saída

print(f'O equivalente em semanas e dias seria ==> {valor_semanas} semanas e {valor_dias_final} dias')
