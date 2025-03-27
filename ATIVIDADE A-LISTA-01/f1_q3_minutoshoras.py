#Entrada

inicial_minutos = int(input('Diga o valor dos minutos: '))

#Processamento

final_horas = inicial_minutos // 60

final_minutos = inicial_minutos % 60

#Saída

print(f'O valor final é {final_horas} horas e {final_minutos} minutos')
