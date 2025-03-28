# Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.

# Entrada

nota1 = float(input('Insira a sua primeira nota:'))
peso1 = float(input('Insira o peso da primeira nota:'))
nota2 = float(input('Insira a sua segunda nota:'))
peso2 = float(input('Insira o peso da segunda nota:'))
nota3 = float(input('Insira a sua terceira nota:'))
peso3 = float(input('Insira o peso da terceira nota:'))

# Processamento

calculo_final = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# Saída

print(f'O valor da média ponderada é: {calculo_final}')
