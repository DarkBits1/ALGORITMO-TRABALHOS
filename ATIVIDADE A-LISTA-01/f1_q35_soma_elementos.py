# Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. Ex.: número = 9534 ; soma = 9+5+3+4 = 21.

# Entrada

numero_inteiro = int(input('insira um número de 4 dígitos aqui ==> '))

# Processamento

milhar = numero_inteiro // 1000
centena = (numero_inteiro % 1000) // 100
dezena = ( (numero_inteiro % 1000) % 100)// 10
unidade = numero_inteiro % 10

soma = milhar + centena + dezena + unidade

# Saída

print(f'O resultado da soma dos elementos que o compõem o número de 4 digitos é é ==> {soma}')


