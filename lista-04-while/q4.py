def main():
  num_atual = int(input('Número > '))
  for i in range(1, num_atual+1, 1):
    num_atual = num_atual / 2
    num_anterior = num_atual * 2
    if num_atual < 1:
      print(f'{num_anterior} / 2 = {num_atual}')
      break


main()