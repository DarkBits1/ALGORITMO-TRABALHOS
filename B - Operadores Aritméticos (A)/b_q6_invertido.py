# Escreva um programa que receba um número de três dígitos e exiba ele invertido.

# Entrada

numero = int(input('Insira um número de 3 digitos: '))

# Processamento

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10
numero_invertido = unidade*100 + (dezena * 10) + (centena)

# Saída

print(f'O número invertido é ==> {numero_invertido}')
print({centena * 100})
