# Leia o valor do raio de uma esfera, calcule e escreva seu volume. (v = (4 * p * r3 ) / 3) (p = 3,14)

# Entrada

raio = float(input('Insira o valor do raio da esfera: '))
p = float(3.14)

# Processamento

volume =  (4 * p * (pow(raio, 3)) ) / 3

# Saída

print(f'O volume da esfera é ==> {volume:.2f}')
