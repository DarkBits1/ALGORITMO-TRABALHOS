# Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.

# Entrada

numero_inteiro = int(input('Insira o valor do número (3 dígitos): '))

# Processamento

centena = numero_inteiro // 100
dezena = (numero_inteiro % 100) // 10
unidade = numero_inteiro % 10
numero_inverso = unidade * 100 + dezena * 10 + centena
diferenca = numero_inteiro - numero_inverso
# Saída

print(f'O valor da diferença entre o numero e seu inverso é ==> {diferenca}')

