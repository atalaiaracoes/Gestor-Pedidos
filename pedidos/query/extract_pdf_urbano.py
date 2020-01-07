import textract


arquivo = open('consulta_vendas_pedido_urbano.txt', 'w')


def text_extractor(path):
        text = textract.process(path, encoding='ascii')
        text = str(text)
        return text


def consulta_pedido(dici):
    tnp = "Número do pedido: " + dici[15] + "\n"
    ss = dici[21].split()
    ss = ''.join(ss)
    tde = "Data de emissão: " + ss + "\n"
    ttp = "Tipo de pedido: " + dici[25] + "\n"
    tf = "Função: " + dici[29] + "\n"

    st = dici[39].split()
    st = ''.join(st)
    tcc = "CNPJ do comprador: " + st + "\n"
    tec = "EAN do comprador: " + dici[47] + "\n"

    st1 = dici[43].split()
    st1 = ''.join(st1)
    tcf = "CNPJ do fornecedor: " + st1 + "\n"
    tef = "EAN do fornecedor: " + dici[51] + "\n"

    tdie = "Data início de entrega: " + ''.join(dici[60].split()) + "\n"
    tdfe = "Data final de entrega: " + ''.join(dici[62].split()) + "\n"

    print("\n\n" + tnp + tde + ttp + tf + tcc + tec + tcf + tef + tdie + tdfe + "\n")


def consulta_itens(dici):
    it = 0

    total = 0

    for key, val in dici.items():
        if val == "ITENS DO PEDIDO":
            it = key + 11

    while (it < len(dici)):
        ti = "Item: " + dici[it] + "\n"
        tc = "EAN: " + dici[(it + 2)] + "\n"

        tes = 0
        while (tes != 1):
            if dici[it] == 'Unidade':
                tes = 1
            else:
                it += 1

        tpb = "Preço bruto: R$ {}\n".format(converte_casas(dici[(it + 24)]))
        tqp = "Quantidade pedida: {}\n".format(converte_casas(dici[(it + 20)]))
        tvt = "Valor total: R$ {}".format(converte_casas(dici[(it + 46)]))
        print(ti + tc + tpb + tqp + tvt + "\n")

        total += converte_casas(dici[it + 46])

        it += 51

        if (dici[it] == "SUMRIO"):
            break

    print("O total deste pedido foi de: R$ {}".format(total))


def converte_casas(valor):
    aux = valor.replace(".", "")
    aux = aux.replace(",", ".")
    aux = float(aux)
    return aux


if __name__ == '__main__':

    campdf = input(str("Digite o caminho do arquivo em formato PDF a ser transformado em texto: "))

    tv = text_extractor(campdf).split('\\n', 500)


    tk = []
    i = 0

    while (i < len(tv)):
        tk.append(i)
        i += 1

    tv = dict(zip(tk, tv))

    arquivo.write(str(tv))

    consulta_pedido(tv)

    consulta_itens(tv)

    arquivo.close()