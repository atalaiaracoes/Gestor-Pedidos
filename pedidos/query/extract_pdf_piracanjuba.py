from PyPDF2 import PdfFileReader

arquivo = open('consulta_vendas_pedido_piracanjuba.txt', 'w')


def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        page = pdf.getPage(0)
        text = page.extractText()
        return text

def consulta_pedido(dici):
    tnp = "Número do pedido: " + dici[3] + "\n"
    ss = dici[5].split()
    ss = ''.join(ss)
    tde = "Data de emissão: " + ss + "\n"
    ttp = "Tipo de pedido: " + dici[7] + "\n"
    tf = "Função: " + dici[12] + "\n"

    st = dici[15].split()
    st = ''.join(st)
    tcc = "CNPJ do comprador: " + st + "\n"
    tec = "EAN do comprador: " + dici[17] + "\n"

    st1 = dici[20].split()
    st1 = ''.join(st1)
    tcf = "CNPJ do fornecedor: " + st1 + "\n"
    tef = "EAN do fornecedor: " + dici[22] + "\n"

    tdie = "Data início de entrega: " + ''.join(dici[25].split()) + "\n"
    tdfe = "Data final de entrega: " + ''.join(dici[27].split()) + "\n"

    print("\n\n" + tnp + tde + ttp + tf + tcc + tec + tcf + tef + tdie + tdfe + "\n")


def consulta_itens(dici):
    it = 0

    total = 0

    for key, val in dici.items():
        if val == "Item":
            it = key + 1

    while (it < len(dici)):
        ti = "Item: " + dici[it] + "\n"
        tc = "EAN: " + dici[(it + 1)] + "\n"

        tes = 0
        while (tes != 1):
            if ((dici[it] == "Unidade ") or (dici[it] == " ")):
                tes = 1
            else:
                it += 1

        tpb = "Preço bruto: R$ {}\n".format(converte_casas(dici[(it + 4)]))
        tqp = "Quantidade pedida: {}\n".format(converte_casas(dici[(it + 2)]))
        tvt = "Valor total: R$ {}".format(converte_casas(dici[(it + 9)]))
        print(ti + tc + tpb + tqp + tvt + "\n")

        total += converte_casas(dici[it + 9])

        it += 10

        if (dici[it] == "Sumário"):
            break

    print("O total deste pedido foi de: R$ {}".format(total))


def converte_casas(valor):
    aux = valor.replace(".", "")
    aux = aux.replace(",", ".")
    aux = float(aux)
    return aux


if __name__ == '__main__':

    campdf = input("Digite o caminho do arquivo em formato PDF a ser transformado em texto: ")

    tv = text_extractor(campdf).split('\n')

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