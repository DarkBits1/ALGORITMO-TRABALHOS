# Escreva um programa que aplique um desconto percentual sobre um preço inicial.

# Entrada

produto = float(input('Insira o valor do produto: '))
desconto = float(input('Insira o desconto: '))

# Processamento
desconto_final = (desconto / 100) * produto
novo_preco = produto - desconto_final

# Saída

print(f'O novo preço é ==> {novo_preco}')
