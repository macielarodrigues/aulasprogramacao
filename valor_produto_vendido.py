# Valor do produto vendido
Produto = str(input("Digite o produto escolhido:"))
Quantidade = int(input("Informe a quantidade comprada do produto: "))
VU = float(input("Informe o preço unitário do produto: "))
if Quantidade >= 5:
    D = 15
else:
    D = 5
porcentagem = D/100
PT = Quantidade*VU
VT = PT - (PT*porcentagem)
VT2 = round(VT, 2)
print("O produto escolhido foi:", Produto, "e o valor total da venda é:", VT2)

## VU == Valor unitário and D == Desconto and PT == Preço total and VT == Valor total
