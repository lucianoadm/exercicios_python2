# acrescentando mais funcionalidades ao nosso programa
# simulando um estoque de produtos perecíveis, onde o
# prazo de validade está próximo, para isso alguns dos
# produtos do estoque terão o preço reduzido para aumentar
# as vendas, antes que o prazo de validade acabe.
produto = []
preco_venda = []
estoque_quantidade = []
validade = []
resposta = 'S'
while resposta == 'S':
    produto.append(input('Digite o produto: '))
    preco_venda.append(float(input('Digite o valor unitário: ')))
    estoque_quantidade.append(int(input('Digite a quantidade no estoque: ')))
    validade.append(input('Prazo ja venceu? Sim / Não: '))
    resposta = input('deseja continuar? (S) / (N): ').upper()
    print()
for x in range(len(produto)):
    print(f'Produto: {produto[x]}')
    print(f'Validade vencida? {validade[x]}')
    if validade[x] == 's':
        print(f'Preço de venda normal: {preco_venda[x]}')
        print(f'Preço de venda com desconto: {preco_venda[x]*0.9} ')
    else:
        print(f'Esse produto ainda está na validade!')
        print(f'Preço de venda....: {preco_venda[x]}')
print('Programa encerrado!')


