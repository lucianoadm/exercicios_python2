## lista de materiais
reposicao = []
estoque_atual = []
estoque_minimo = []
valor = []
material = []
resposta = 'C'
while resposta == 'C':
    material.append(input('Digite o material: '))
    valor.append(float(input('Digite o valor unitário: ')))
    estoque_atual.append(int(input('Digite o estoque atual: ')))
    estoque_minimo.append(int(input('Digite o estoque mínimo: ')))
    resposta = input('Digite \'C\' para continuar \'S\' para sair:  ').upper()
subtotal = 0
soma = 0
for i in range(len(material)):
    print(f'\nProduto....: {material[i]}')
    reposicao = estoque_minimo[i] - estoque_atual[i]
    print(f'Quantidade de reposição..: {reposicao}')
    subtotal = reposicao * valor[i]
    print(f'Custo reposição: {round(subtotal,2)}')
    soma += subtotal
print(f'\nCusto total reposição: {round(soma,2)}')



