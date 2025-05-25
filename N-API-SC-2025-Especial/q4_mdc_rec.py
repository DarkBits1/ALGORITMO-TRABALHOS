#INÍCIO: 21:26 24/05/2025
#FIM: 21:48 24/05/2025

from q1_number_utils import positive_int_number

def main():
    x = positive_int_number('Número 1 > ')
    y = positive_int_number('Número 2 > ')
    mdc_real = 1
    mdc_teste = 0
    calculo(x, y, mdc_real, mdc_teste)

def calculo(x, y, mdc_real, mdc_teste):
    mdc_teste += 1
    if mdc_teste > x or mdc_teste > y: 
        return print(f'O MDC ({x}, {y}) é {mdc_real}')
    if x % mdc_teste == 0 and y % mdc_teste == 0:
        mdc_real = mdc_teste
    calculo(x, y, mdc_real, mdc_teste)

main()