import math

def main():
    lado_a = int(input('lado A:'))
    lado_b = int(input('lado B:'))
    lado_c = int(input('lado C:'))

    if eh_triangulo(lado_a, lado_b, lado_c):
        print('Os lados formam um triângulo!')
        
        if eh_degenerado(lado_a, lado_b, lado_c):
            print('Entretanto, ele é um DEGENERADO!')
        
        perimetro = calcular_perimetro(lado_a, lado_b, lado_c)
        area = calcular_area(lado_a, lado_b, lado_c)
        
        print(f'Perímetro: {perimetro}')
        print(f'Área: {area:.2f}')
        
        classificacao_lados = classificar_por_lados(lado_a, lado_b, lado_c)
        print(f'Classificação por lados: {classificacao_lados}')
        
        classificacao_angulos = classificar_por_angulos(lado_a, lado_b, lado_c)
        print(f'Classificação por ângulos: {classificacao_angulos}')
    
    else:
        print('Os lados NÃO formam um triângulo!')
    
    print('Fim por fim feito por mim!')

def eh_triangulo(a: int, b: int, c: int): 
    return a + b > c and a + c > b and b + c > a

def eh_degenerado(a: int, b: int, c: int):
    return (a == b + c or b == a + c or c == a + b)

def calcular_perimetro(a: int, b: int, c: int):
    return a + b + c

def calcular_area(a: int, b: int, c: int):
    s = calcular_perimetro(a, b, c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def classificar_por_lados(a: int, b: int, c: int):
    if a == b == c:
        return 'Equilátero'
    elif a == b or a == c or b == c:
        return 'Isósceles'
    else:
        return 'Escaleno'

def classificar_por_angulos(a: int, b: int, c: int):
    a2 = a**2
    b2 = b**2
    c2 = c**2
    
    if a2 + b2 > c2 and a2 + c2 > b2 and b2 + c2 > a2:
        return 'Acutângulo'
    elif a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
        return 'Retângulo'
    else:
        return 'Obtusângulo'

main()
