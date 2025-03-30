# Escreva um programa que determine a quantidade de notas de 50 e 10 necessárias para um determinado valor.

# Entrada

valor = int(input('Insira o valor: '))

# Processamento

nota_50 = valor // 50
nota_10 = (valor % 50) // 10

# Saída

print(f'Você precisará de {nota_50} nota(s) de R$50 e {nota_10} nota(s) de R$10')
