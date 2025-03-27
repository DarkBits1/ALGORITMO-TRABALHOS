# Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.


# Entrada

valor_horas = int(input('Diga o valor das horas: '))
valor_minutos = int(input('Diga o valor dos minutos: '))

# Processamento

processamento_minutos = valor_horas * 60
final_minutos = processamento_minutos + valor_minutos
# Saída

print(f'O valor final é {final_minutos} minutos')