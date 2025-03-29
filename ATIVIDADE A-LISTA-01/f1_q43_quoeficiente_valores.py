# Um sistema de equações lineares do tipo , pode ser resolvido segundo mostrado abaixo
        
# Escreva um algoritmo que leia os coeficientes a, b, c, d, e e f, calcule e escreva os valores de x e y.

# Entrada

a = float(input('Insira o valor de a ==> '))
b = float(input('Insira o valor de b ==> '))
c = float(input('Insira o valor de c ==> '))
d = float(input('Insira o valor de d ==> '))
e = float(input('Insira o valor de e ==> '))
f = float(input('Insira o valor de f ==> '))

# Processamento

x = (c*e - b*f)/(a*e - b*d)
y = (a*f - c*d)/(a*e - b*d) 


# Saída

print(f'O valor de x é {x:.2f} e y {y:.2f}')
