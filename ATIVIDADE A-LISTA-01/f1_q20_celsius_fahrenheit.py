# Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)

# Entrada 

celsius = float(input('Insira o valor da temperatura em celsius: '))


# Processamento

fahrenheit = (9 * celsius + 160) / 5

# Saída

print(f'O valor equivalente em fahrenheit é ==> {fahrenheit:.2f}°F')
