# Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)


#Entrada

velocidade_kmh = float(input('Insira velocidade em km/h: '))


#Processamento

velocidade_ms = (velocidade_kmh / 3.6)

#Saída

print(f'O valor em metros por segundo é ==> {velocidade_ms:.2f}m/s')

