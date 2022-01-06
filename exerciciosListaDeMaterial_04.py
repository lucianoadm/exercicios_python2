# Faça um programa que receba dados de material,
# quantidade, valor unitário e código de referência
# os armazene numa sublista e os envie para uma
# lista principal, cada um dos itens será acessado
# pelo seu índice. Depois imprima cada produto com
# o seu subtotal. Por fim imprima o gasto total com
# todos os materiais.

inventario = []  # lista rincipal vazia
resposta = 'S'  # variável de continuidadedo programa
while resposta == 'S':  # laço condiconal
    equipamentos = [input('Digite o produto: '),  # sublista equipamentos / com entrada de produto
                    int(input('Digite a quantidade: ')),  # entrada de quantidade
                    float(input('Digite o valor unitário: ')),  # entrada do valor unitário
                    int(input('Digite o código do produto: '))]  # entrada de código do produto
    inventario.append(equipamentos)  # aramzenamento da sublista a lista principal
    resposta = input('Deseja continuar?\n'  # condicional de interrupção doprograma
                     '(s) Sim / (n) Não: ').upper()
soma = 0  # variável soma que recebe todos os subtotais
for i in inventario:  # laço para percorrer todos os lementos da lista principal
    # impressão dos elementos da sublista de acordo com índice na lista principal
    print(f'\nProduto........:{equipamentos[0]}')  # imprimindo o elemento de índice 0  - produto
    print(f'Quantidade......: {equipamentos[1]}')  # imprimindo o elemento de índice 1 - quantidade
    subtotal = equipamentos[1] * equipamentos[2]  # subtotal que recebe a quantidade * valor unitário
    print(f'Subtotal........: {round(subtotal,2)}')  # imprimindo o subtotal e arredondando 2 casas decimais
    soma += subtotal  # variável soma que recebe todos os subtotais
print(f'\nTotal gasto.......: {round(soma,2)}')  # impressão do total gasto
