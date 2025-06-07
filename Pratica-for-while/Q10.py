
anos = int(input("Quantos anos de análise? "))
temperaturas = []

for i in range(anos):
    temp = float(input(f"Temperatura média do ano {i+1}: "))
    temperaturas.append(temp)

media_geral = sum(temperaturas) / anos
maior_temp = max(temperaturas)
menor_temp = min(temperaturas)
indice_maior = temperaturas.index(maior_temp) + 1
indice_menor = temperaturas.index(menor_temp) + 1

metade = anos // 2
media_inicio = sum(temperaturas[:metade]) / metade
media_fim = sum(temperaturas[-metade:]) / metade

tendencia = "aquecimento" if media_fim > media_inicio else "resfriamento"

print(f"Ano com maior temperatura: Ano {indice_maior} - {maior_temp}°C")
print(f"Ano com menor temperatura: Ano {indice_menor} - {menor_temp}°C")
print(f"Média geral: {media_geral:.2f}°C")
print(f"Tendência de {tendencia}.")
