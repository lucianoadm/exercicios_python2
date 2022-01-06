# Faça um programa que receba dados de material,
# quantidade, valor unitário e código de referência
# e os armazene cada um numa lista individual. Depois
# imprima cada produto com o seu subtotal. Por fim
# imprima o gasto total com materiais.

# definindo as listas, todas vazias
produtos = []  # lista para produtos
quantidade = []  # lista para quantidade
valor = []  # lista de valores unitários
cod = []  # lista de código dos produtos
resposta = 'C'  # variável de continuidade do programa
while resposta == 'C':  # laço de repetição
    produtos.append(input('Digite o produto: '))  # entrada de dados de produto
    quantidade.append(int(input('Digite a quantidade: ')))  # entrada de dados de quantidade
    valor.append(float(input('Digite o valor: ')))  # entrada de dados de valor unitário
    cod.append(int(input('Digite o código do produto: ')))  # entrada de dados de código do produto
    resposta = input('Digite \'C\' para continuar \'S\' para sair: ').upper()  # variável de interrupção
    if resposta == 'S':  # condicional para encerrar o programa
        print('Programa encerrado!\n')  # mensagem de encerramento do programa
        break  # Comando de parada
soma = 0  # variável que receberá a soma de todos os subtotais
for i in range(len(produtos)):  # percorrendo todos os lementos da lista produtos
    print(f'\nProduto.....: {i+1}')  # estabelecendo uma unidade de contador de produtos
    print(f'Nome..........: {produtos[i]}')  # nome do produto de acordo com o contador
    print(f'Quantidade....: {quantidade[i]}')  # quantidade do produto
    subtotal = quantidade[i] * valor[i]  # subtotal quantidade x valor unitário de cada produto
    print(f'Subtotal.....: {subtotal}')  # imrpimindo a variável subtotal
    soma += subtotal  # variável soma que recebe todos os subtotais
print(f'\nCusto total.....: {soma}')  # imprimindo o cuto total dos produtos
