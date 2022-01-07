# passo a passo de uma lista dinâmica
# todos os elementos serão armazenados numa única lista

inventario = []
resposta = 'S'
while resposta == 'S':
    inventario.append(input('Digite o equipamento: '))
    inventario.append(float(input('Digite o valor: ')))
    inventario.append(int(input('Digite a quantidade: ')))
    inventario.append(input('Digite o serial do equipamento: '))
    resposta = input('Digite \'s\' para continuar: ').upper()

for i in inventario:
    print(i)
