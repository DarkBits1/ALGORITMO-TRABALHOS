
# Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235)

# Entrada

numero = int(input('Insira um numero inteiro de 3 digitos: '))

# Processamento

numero_centena = numero // 100
numero_unidade = numero % 10
numero_dezena  = (numero % 100) // 10


# Saída


print(f'{numero_unidade}{numero_dezena}{numero_centena}')
