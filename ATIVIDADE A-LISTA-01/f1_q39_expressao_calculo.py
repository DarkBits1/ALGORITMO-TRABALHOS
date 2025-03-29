 # Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão: D = R + S / 2 ; R = (A + B)^2 e S = (B + C)^2


# Entrada
numeroA = int(input('Insira o primeiro valor: '))
numeroB = int(input('Insira o segundo valor: '))
numeroC = int(input('Insira o terceiro valor: '))

# Processamento
R = (numeroA + numeroB) ** 2 
S = (numeroB + numeroC) ** 2  
expressao = (R + S) / 2  

# Saída
print(f'O valor da expressão é ==> {expressao:.2f}')

