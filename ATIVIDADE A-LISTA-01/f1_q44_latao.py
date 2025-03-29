# Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada pelo usuário

# Entrada

latao = float(input('Escreva a quantidade de latão em kg ==>'))

# Processamento

cobre = latao * 0.7
zinco = latao * 0.3

# Saída

print(f'A quantidade de cobre é {cobre:.2f}kg e de zinco é {zinco:.2f}kg')
