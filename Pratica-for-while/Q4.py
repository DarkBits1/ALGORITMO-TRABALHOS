
def main():
    imoveis = []
    qtd_imoveis = int(input('Quantidade de imóveis > '))
    maior_retorno = float('-inf')
    menor_retorno = float('inf')
    id_maior_retorno = None
    id_menor_retorno = None

    for imovel in range(1, qtd_imoveis + 1):
        print(f'Dados do imóvel {imovel}')
        imovel_compra = float(input('Valor da compra do imóvel > '))
        valor_aluguel = float(input('Valor do aluguel mensal > '))
        qtd_anos = int(input('O imóvel esteve alugado por quantos anos? > '))
        
        lucro_atual = (valor_aluguel * (qtd_anos * 12)) - imovel_compra
        taxa_anual = (lucro_atual / imovel_compra / qtd_anos) * 100 if qtd_anos > 0 and imovel_compra > 0 else 0

        imoveis.append({
            "id": imovel,
            "lucro_total": lucro_atual,
            "taxa_anual": taxa_anual
        })

        print(f"Retorno total: R$ {lucro_atual:.2f}")
        print(f"Taxa de retorno anualizada: {taxa_anual:.2f}%")

        if lucro_atual > maior_retorno:
            maior_retorno = lucro_atual
            id_maior_retorno = imovel
        if lucro_atual < menor_retorno:
            menor_retorno = lucro_atual
            id_menor_retorno = imovel

    print('\n== Resumo final ==')
    print(f'Imóvel com MAIOR retorno total: Imóvel {id_maior_retorno} (R$ {maior_retorno:.2f})')
    print(f'Imóvel com MENOR retorno total: Imóvel {id_menor_retorno} (R$ {menor_retorno:.2f})')

main()
