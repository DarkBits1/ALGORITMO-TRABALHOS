
def main():
  soma = 0
  media = 0
  n = int(input('Quantos algarismos serão lidos na lista? > '))
  for i in range(1, n+1, 1):
    i = int(input('Insira o algarismo > '))
    soma += i
  media = soma / n
  print(f"""
------------------------
        MÉDIA > {media:.2f}
        SOMA > {soma}
------------------------

""")
  

main()