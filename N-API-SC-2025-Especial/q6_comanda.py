#INÍCIO: 9:40 25/05/2025
#FINAL: 10:23 25/05/2025


def main():
  preco = agua = quant = cerveja = tira_gosto = preco_total = 0 
  while True:
    escolha = input("""
-------------MENU-----------------
    1. Inserir produtos
    2. Calcular conta
    3. Imprimir conta
    4. Confirmar pagamento
----------------------------------
        
    Aperte a tecla da operação que deseja realizar > """)
    if escolha == '1':
      preco, quantidade, agua, quant, cerveja, tira_gosto = inserir_produto()
    elif escolha == '2':
      preco, preco_total = calcular_conta(preco, preco_total)
    elif escolha == '4':
      preco = 0
      quantidade = 0
      agua = 0
      quant = 0
      cerveja = 0
      tira_gosto = 0
      preco_total = 0
      confirmar_pagamento()
    else:
      preco, preco_total = imprimir_conta(preco, preco_total)


def inserir_produto():
  quant = 0
  cerveja = 0
  tira_gosto = 0
  agua = 0
  while True:
    quantidade, tipo = input("""
--------------
   a. Cerveja    (R$ 9)
   b. Tira-Gosto (R$ 39)
   c. Água       (R$ 5)
                           

   d. Voltar.  
-----------------------
 Insira o produto e a quantidade > """).split()
    try:
      quantidade = int(quantidade)
    except ValueError:
      input("Valor inválido. Aperte Enter para tentar novamente.")
      continue
    if tipo.lower() == 'a':
      preco = quantidade * 9
      cerveja += quantidade
      quant += quantidade
    elif tipo.lower() == 'b':
      preco = quantidade * 39
      tira_gosto += quantidade
      quant += quantidade
    elif tipo.lower() == 'c':
      preco = quantidade * 5  
      agua += quantidade
      quant += quantidade
    else:
      return preco, quantidade, agua, quant, cerveja, tira_gosto


def calcular_conta(preco, preco_total):
  preco_total += preco + (preco * 0.1)
  input("""
  Conta calculada. Aperte ENTER para voltar.
""")
  return preco, preco_total


def imprimir_conta(preco, preco_total):
  pessoas = int(input("Quantas pessoas irão pagar? > "))
  input(f"""
--------------------------
      VALOR DA CONTA > R$ {preco:.2f}
      VALOR DA CONTA POR PESSOA > R$ {preco / pessoas:.2f}
      VALOR DA TAXA DE SERVIÇO > R$ {preco * 0.1:.2f}
      VAALOR TOTAL COM TAXA DE SERVIÇO > R$ {preco_total:.2f}
--------------------------------------------------
    Aperte ENTER PARA VOLTAR.
""")
  return preco, preco_total


def confirmar_pagamento():
  input("Conta zerada. Aperte ENTER para voltar.")


main()
