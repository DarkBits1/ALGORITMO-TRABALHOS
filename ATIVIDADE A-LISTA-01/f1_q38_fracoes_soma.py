# Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.


# Entrada

numerador1 = int(input('Insira o numerador da primeira fração: '))
denominador1 = int(input('Insira o denominador da primeira fração: '))
numerador2 = int(input('Insira o numerador da segunda fração: '))
denominador2 = int(input('Insira o denominador da segunda fração: '))
# Processamento

denominador_final = denominador1 * denominador2
numerador1_multiplicado = numerador1 * denominador2
numerador2_multiplicado = numerador2 * denominador1
numerador_final = numerador1_multiplicado + numerador2_multiplicado

# Saída

print(f'O valor da soma das duas frações é ==> {numerador_final}/{denominador_final}')
