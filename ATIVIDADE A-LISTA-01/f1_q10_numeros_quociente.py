# Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1o pelo 2o.

# Entrada

numeroA = int(input('Insira o primeiro numero: '))

numeroB = int(input('Insira o segundo numero: '))


# Processamento

quociente = numeroA // numeroB

resto = numeroA % numeroB

# Saída

print(f'O quociente da divisao do primeiro numero com o segundo numero é {quociente} e o resto da divisão é {resto}')
