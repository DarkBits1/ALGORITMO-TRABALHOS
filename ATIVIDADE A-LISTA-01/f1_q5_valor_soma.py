# Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).

# Entrada

numero_inteiro = int(input('Insira o número inteiro: '))

# Processamento

centena = numero_inteiro // 100
unidade = (numero_inteiro % 10)
dezena = (numero_inteiro % 100) // 10

resultado = centena + dezena + unidade

# Saída

print(f'O valor da soma de seus elementos é igual a ==> {resultado}')
