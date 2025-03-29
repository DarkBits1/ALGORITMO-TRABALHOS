# Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso. (Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).


# Entrada

numero_inteiro = int(input('Insira um número inteiro (3 dígitos): '))

# Processamento

unidade = numero_inteiro % 10
dezena = (numero_inteiro % 100) // 10
centena = numero_inteiro // 100
numero_inverso = unidade * 100 + dezena * 10 + centena
diferenca = numero_inteiro + numero_inverso
# Saída
 
print(f'O resultado da soma desse número com o seu inverso é igual a ==> {diferenca}')
