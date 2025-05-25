#INÍCIO: 19:59 24/05/2025
#FINAL: 20:45 24/05/2025
def main():
   dias = 0
   total_casos = 0
   while True:
      if dias == 0:
       valor_anterior = 0
      else:
        valor_anterior = num
      num = input('Insira o número de casos no dia > ')
      if num == 'fim':
        print('Programa encerrado.')
        break
      num = int(num)
      if num < 0:
        print('O número de casos deve ser positivo.')
        continue
      if num >= 0:
        valor_atual = num
        total_casos += valor_atual
        dias += 1
        
        if valor_atual > (valor_anterior + valor_anterior * 0.15):
          print('Conceito > Em alta.')
        elif valor_atual < (valor_anterior - valor_anterior * 0.15):
          print('Conceito > Em queda.')
        else:
          print('Conceito > Em estabilidade.')
   media_dia = total_casos / dias
   resultado(total_casos, media_dia)



def resultado(total_casos, media_dia):
  print(f"""
-----------------------
        TOTAL DE CASOS > {total_casos}
        MEDIA DE CASOS POR DIA > {media_dia:.2f}
-----------------------------------

""")



main()