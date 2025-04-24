def main():
    try:
        lado1 = int(input('Insira o valor do lado 1: '))
        lado2 = int(input('Insira o valor do lado 2: '))
        lado3 = int(input('Insira o valor do lado 3: '))
        triangulo_analise(lado1, lado2, lado3)
    except ValueError:
        print('Erro: você deve inserir apenas números inteiros.')
        main()

def triangulo_analise(lado1, lado2, lado3):
    if lado1 == 0 or lado2 == 0 or lado3 == 0:
        print('Não existe triângulo com lado igual a 0.')
    elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        print('Não é possível formar triângulo.')
    elif lado1 == lado2 == lado3:
        print('Triângulo equilátero.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Triângulo isósceles.')
    else:
        print('Triângulo escaleno.')

main()
