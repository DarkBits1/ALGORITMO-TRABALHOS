# Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2), escreva a distância entre eles, conforme fórmula abaixo.
# d = 

# Entrada
x1 = float(input('Insira a coordenada x do primeiro ponto: '))
y1 = float(input('Insira a coordenada y do primeiro ponto: '))
x2 = float(input('Insira a coordenada x do segundo ponto: '))
y2 = float(input('Insira a coordenada y do segundo ponto: '))

# Processamento
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 

# Saída
print(f'A distância entre os pontos é: {distancia:.2f}')

