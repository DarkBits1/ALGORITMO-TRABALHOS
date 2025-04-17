def main():
    unidade_origem = input('Escolha a unidade de origem (kelvin/celsius/fahrenheit): ').lower()
    unidade_final = input('Escolha a unidade de destino (kelvin/celsius/fahrenheit): ').lower()

    if unidade_origem not in ['kelvin', 'celsius', 'fahrenheit']:
        print('Unidade de origem inválida.')
        return main()

    if unidade_final not in ['kelvin', 'celsius', 'fahrenheit']:
        print('Unidade de destino inválida.')
        return main()

    try:
        temp_valor = float(input('Insira o valor da temperatura: '))
    except ValueError:
        print('Valor inválido.')
        return main()

   
    if unidade_origem == 'kelvin' and temp_valor < 0:
        print('Kelvin não admite valores menores que 0.')
        return main()
    if unidade_origem == 'celsius' and temp_valor < -273.15:
        print('Celsius não admite valores menores que -273.15.')
        return main()

    if unidade_origem == unidade_final:
        print(f"A temperatura já está em {unidade_final}: {temp_valor:.2f}")
        return

    if unidade_origem == 'kelvin' and unidade_final == 'fahrenheit':
        kelvin_fahrenheit(temp_valor)
    elif unidade_origem == 'celsius' and unidade_final == 'fahrenheit':
        celsius_fahrenheit(temp_valor)
    elif unidade_origem == 'fahrenheit' and unidade_final == 'kelvin':
        fahrenheit_kelvin(temp_valor)
    elif unidade_origem == 'fahrenheit' and unidade_final == 'celsius':    
        fahrenheit_celsius(temp_valor)
    elif unidade_origem == 'kelvin' and unidade_final == 'celsius':
        kelvin_celsius(temp_valor)  
    elif unidade_origem == 'celsius' and unidade_final == 'kelvin':
        celsius_kelvin(temp_valor)    
    else:
        print('Conversão não suportada.')
        return main()


def kelvin_fahrenheit(temp_valor):
    resultado = (temp_valor - 273.15) * 9/5 + 32
    print(f"Resultado: {resultado:.2f} °F")

def celsius_fahrenheit(temp_valor):
    resultado = (temp_valor * 1.8) + 32
    print(f"Resultado: {resultado:.2f} °F")

def fahrenheit_kelvin(temp_valor):
    resultado = (temp_valor - 32) / 1.8 + 273.15
    print(f"Resultado: {resultado:.2f} K")

def fahrenheit_celsius(temp_valor):
    resultado = (temp_valor - 32) / 1.8
    print(f"Resultado: {resultado:.2f} °C")

def kelvin_celsius(temp_valor):
    resultado = temp_valor - 273.15
    print(f"Resultado: {resultado:.2f} °C")

def celsius_kelvin(temp_valor):  
    resultado = temp_valor + 273.15
    print(f"Resultado: {resultado:.2f} K")

main()
