# Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)
#Entrada 

velocidade_metros = float(input('Insira velocidade em m/s: '))

#Processamento

velocidade_kmh = (velocidade_metros * 3.6 )

#Saída

print(f'Sua velocidade em m/s era {velocidade_metros:.2f}, logo sua velocidade em km/h é {velocidade_kmh:.2f}')
