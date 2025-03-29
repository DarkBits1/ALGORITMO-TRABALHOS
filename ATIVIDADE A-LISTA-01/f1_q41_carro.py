# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor  seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.


# Entrada

custo_fabrica = float(input('Insira o valor do custo de fábrica: '))
porcentagem_distribuidor = float(input('Insira a porcentagem do distribuidor: '))
porcentagem_impostos = float(input('Insira a porcentagem dos impostos'))


# Processamento

custo = ((porcentagem_distribuidor / 100) * custo_fabrica) + ((porcentagem_impostos / 100) * custo_fabrica) + custo_fabrica


# Saída

print(f'O valor do custo total é ==> R${custo:.2f}')
