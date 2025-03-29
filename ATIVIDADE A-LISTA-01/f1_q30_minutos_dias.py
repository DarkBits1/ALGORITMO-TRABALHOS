# Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele corresponde

# Entrada

valor_minutos = int(input('Insira o valor em minutos: '))

# Processamento

valor_dias = valor_minutos // 1440
valor_resto = valor_minutos % 1440
valor_horas = valor_resto // 60
valor_minutos = valor_resto % 60

# Saída

print(f'O valor equivale a ==> {valor_dias} dia(s), {valor_horas} hora(s) e {valor_minutos} minuto(s)')
