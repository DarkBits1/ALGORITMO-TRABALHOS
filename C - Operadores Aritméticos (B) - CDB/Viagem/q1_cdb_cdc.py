import math

def cdb_calculo():
     investimento = float(input('Insira o valor que deseja investir: '))
     juros = float(input('Insira a taxa de juros anual(entre 1 e 20 %): '))
     tempo = int(input('Você deixará o dinheiro por quantos anos?: '))
     montante = investimento * (1 + (juros / 100)) ** tempo
     juros_cdb = montante - investimento
     
     print(f"\nVALOR QUE O BANCO IRÁ TER QUE PAGAR PARA O INVESTIDOR: R${montante:.2f}")
     print(f"VALOR TOTAL DOS JUROS: R${juros_cdb:.2f}\n")

     return juros_cdb


def cdc_calculo():
     emprestimo = float(input('Insira o valor que deseja pedir de empréstimo: '))
     juros_cdc = float(input('Insira o valor do juros mensal(1 a 17%): '))
     tempo_meses = int(input('Insira o número de parcelas: '))
     montante_cdc = emprestimo * (1 + (juros_cdc / 100)) ** tempo_meses
     juros_total_cdc = montante_cdc - emprestimo
     parcela_cdc_valor = (emprestimo * (juros_cdc / 100) * (1 + (juros_cdc / 100)) ** tempo_meses) / ((1 + (juros_cdc / 100)) ** tempo_meses - 1)

     resultado = f"""
        VALOR TOTAL DE JUROS QUE TERÁ QUE PAGAR: R${juros_total_cdc:.2f}

        VALOR DE CADA PARCELA: R${parcela_cdc_valor:.2f}
        
        VALOR TOTAL A PAGAR: R${montante_cdc:.2f}

         """
     print(resultado)


     return juros_total_cdc


juros_cdb = cdb_calculo()
juros_cdc = cdc_calculo()

lucro_banco = juros_cdc - juros_cdb
print(f'O valor que o banco irá lucrar é: R${lucro_banco:.2f}')
