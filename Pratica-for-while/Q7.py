
def dias_entre_datas(d1, d2):
    dia1, mes1, ano1 = map(int, d1.split("/"))
    dia2, mes2, ano2 = map(int, d2.split("/"))
    total1 = dia1 + mes1 * 30 + ano1 * 360
    total2 = dia2 + mes2 * 30 + ano2 * 360
    return total2 - total1

data_atual = input("Informe a data de hoje (DD/MM/AAAA): ")
itens = int(input("Quantos itens deseja cadastrar? "))
estoque = []

for _ in range(itens):
    nome = input("Nome do alimento: ")
    quantidade = int(input("Quantidade: "))
    compra = input("Data de compra (DD/MM/AAAA): ")
    validade = input("Data de validade (DD/MM/AAAA): ")
    estoque.append((nome, quantidade, compra, validade))

print("Alimentos com validade próxima ou vencidos:")
for nome, _, _, validade in estoque:
    dias = dias_entre_datas(data_atual, validade)
    if dias <= 10:
        status = "VENCIDO" if dias < 0 else f"vence em {dias} dias"
        print(f"{nome} - Validade: {validade} ({status})")


