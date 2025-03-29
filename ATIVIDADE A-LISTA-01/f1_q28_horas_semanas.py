# Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele corresponde.

# Entrada

valor_horas = float(input('Insira a quantidade de horas: '))

# Processamento

valor_semanas = valor_horas // 168
horas_resto = valor_horas % 168
valor_dias = horas_resto // 24
valor_horas_final = horas_resto % 24

# Saída

print(f'O valor traduz para ==> {valor_semanas} semanas, {valor_dias} dias e {valor_horas_final} horas')
