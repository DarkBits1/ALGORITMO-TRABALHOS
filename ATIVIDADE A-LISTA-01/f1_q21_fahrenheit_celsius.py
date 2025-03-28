# Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).

# Entrada

fahrenheit = float(input('Insira o valor da temperatura em fahrenheit: '))

# Processamento

celsius = (5 * fahrenheit - 160) / 9

# Saída

print(f'O valor da temperatura em celsius é ==> {celsius:.2f} °C')
