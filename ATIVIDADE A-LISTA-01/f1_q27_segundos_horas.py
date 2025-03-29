# Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.


# Entrada

valor_segundos = int(input('Insira o valor em segundos: '))

# Processamento

valor_horas = valor_segundos // 3600
horas_resto = valor_segundos % 3600
valor_minutos = horas_resto // 60
valor_segundos_final = horas_resto % 60

# Saída

print(f'O valor em horas, minutos e segundos seria ==> {valor_horas} hora(s), {valor_minutos} minuto(s) e {valor_segundos_final} segundo(s)')
