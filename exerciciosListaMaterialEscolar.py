# Faça um programa que receba dados de material,
# quantidade, valor unitário e código de referência
# e os armazene numa lista. Depois imprima cada
# produto individualmente e o seu subtotal. Por fim
# imprima o gasto total com materiais.

lista = []  # criando uma lista vazia

# inputando dados:

while True:  #  laco de input de dados, que só finaliza quando digitado 'fim'
    material = input('\nDigite o material (\'fim\' para encerrar): ')  # recebendo material ou 'fim'
    if material == 'fim':  # condicional 'if' para encerrar o laço de input de dados
        print('Programa encerrado!\n')  # imprimindo o resultado se digitado 'fim'
        break  # parada do programa caso seja digitado 'fim'
    quantidade = (int(input('Digite a quantidade: ')))  # recebendo a quantidade de material
    valor = float(input('Digite o valor unitário: '))  # recebendo o valor unitário do material
    cod = input('Digite o código do produto: ')  # código de referência do produto
    lista.append([material, quantidade, valor, cod])  # armazenando os elementos na lista vazia
soma = 0  # variável 'soma' para receber a soma dos subtotais da cada produto
cont = 0  # variável 'cont' para realizar a contagem dos materiais para visualização posterior

# percorrendo, operando e imprimindo os dados resultantes:

for i in lista:  # percorrendo os elementos recebidos na lista
    cont += 1  # incrementando 1 na variável 'cont' a cada produto percorrido
    print(f'Produto {cont}...: {i[0]}')  # indicando o sequenciamento e o produto
    print(f'Quantidade.......: {i[1]}')  # indicando a quantidade adquirida
    subtotal = i[1] * i[2]  # variável que recebe a qtd e multiplica pelo valor individual da cada material
    print(f'Subtotal.........: {round(subtotal,2)}\n')  # indicando o subtotal de cada material adquirido
    soma += subtotal  # variável soma recebendo a somatória de todos os subtotais
print(f'Total gasto..........: {round(soma,2)}')  # imprimindo o toal gasto com materiais
