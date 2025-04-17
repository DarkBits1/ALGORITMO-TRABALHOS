def ano_bissexto(ano):
    return (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

def obter_ano():
    ano = int(input("Digite um ano: "))
    return ano

def main():
    ano = obter_ano()
    if ano_bissexto(ano):
        print(f'O ano {ano} é bissexto.')
    else:
        print(f'O ano {ano} não é bissexto.')

main()
