# Leia um número inteiro (4 dígitos binários) e calcule o equivalente na base decimal

# Entrada
numero_binario = int(input('Insira um número binário de 4 dígitos: '))

# Processamento
digito1 = (numero_binario // 1000) % 10 
digito2 = (numero_binario // 100) % 10  
digito3 = (numero_binario // 10) % 10   
digito4 = numero_binario % 10           

numero_decimal = (digito1 * 8) + (digito2 * 4) + (digito3 * 2) + (digito4 * 1)

# Saída
print(f'O número na base decimal é ==> {numero_decimal}')
