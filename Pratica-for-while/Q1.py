def main():
  dias = int(input('Quantos dias serão analisados? > '))
  limite = int(input('Limite calórico diário > '))
  cal_total = 0
  maior_dia = 0
  menor_dia = 0
  for i in range(1, dias+1, 1):
    cal_diaria = 0
    cal = float(input('Quantas calorias consumiu no café da manhã? > '))
    cal_total += cal
    cal = float(input('Quantas calorias consumiu no almoço? > '))
    cal_total += cal
    cal = float(input('Quantas calorias consumiu na janta? > '))
    cal_total += cal
    cal = float(input('Quantas calorias consumiu nos lanches? > '))
    cal_total += cal
    cal_diaria += cal_total
    if cal_diaria > maior_dia:
      maior_dia = i
    if cal_diaria < menor_dia or i == 1:
      menor_dia = i
  media = cal_total / dias
  print (resultado(media, cal_total, limite, menor_dia, maior_dia))


def resultado(media, cal_total, limite, menor_dia, maior_dia):
  comparacao = ''
  mensagem = ''
  if media > limite:
    comparacao = 'foi maior que o limite.'
    mensagem = 'Reveja seus conceitos!'
  else:
    comparacao = 'está dentro do limite.'
    mensagem = 'Continue assim!'

  return print(f"""
-------------------------------
    MÉDIA CALÓRICA DIÁRIA DO PERÍODO > {media:.2f}
    DIA COM MENOR CONSUMO > {menor_dia}
    DIA COM MAIOR CONSUMO > {maior_dia}
---------------------------------------

O consumo {comparacao} {mensagem}
""")



main()
