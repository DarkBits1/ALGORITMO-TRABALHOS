# Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.

# Entrada

numero1 = float(input('Qual seria o primeiro número?: '))

numero2 = float(input('Qual seria o valor do segundo número?: '))

# Processamento

resultado = (numero1 + numero2) / (numero1 - numero2)

# Saída

print(f'O resultado da divisão da soma pela subtração dos números lidos é {resultado:.2f}')
