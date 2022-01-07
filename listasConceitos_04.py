# acrescentando mais recursos às nossas listas
# vamos inserir o recurso de pesquisa a um determinado
# elemento da lista principal

produto = []
valor_unitario = []
quantidade = []
resposta = 'S'
while resposta == 'S':
    produto.append(input('Digite o produto: '))
    valor_unitario.append(float(input('Digite o valor unitário: ')))
    quantidade.append(int(input('Digite a quantidade: ')))
    resposta = input('Deseja Continuar? \'s\' ou \'n\': ').upper()
    print()
for i in range(len(produto)):
    print(f'Produtos em estoque......: {produto[i]}')

pesquisa = input('\nDigite o produto que deseja pesquisar: ')
for i in range(len(produto)):
    if pesquisa == produto[i]:
        print(f'Valor unitário....: R${valor_unitario[i]}')
        print(f'Estoque atual....: {quantidade[i]} unidades.')
        custo_estoque = valor_unitario[i] * quantidade[i]
        print(f'O estoque deste produto está estimado em R${round(custo_estoque,2)}')
print('\nPrograma encerrado!')
