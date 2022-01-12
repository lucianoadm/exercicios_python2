# Faremos agora um programa que simula um inventário,
# com várias funcionalidades, embora seja mais completo
# o programa, percebemos que ele está um pouco extenso.
# por essa razão ele será 'modulado', ou seja: haverá
# partes do programa separadas por módulos, cada um com
# uma função distinta.

inventario = []
resposta = 'C'

# adicionando itens ao inventário
while resposta == 'C':
    equipamentos = [input('Digite o equipamento: '),
                    float(input('Digite o valor: ')),
                    int(input('Digite o serial: ')),
                    input('Dgite o setor: ')]
    inventario.append(equipamentos)
    resposta = input('Digite \'C\' para continuar ou \'S\' para sair: ')

# exibição dos dados do inventário
for dados in inventario:
    print(f'Equipamento....: {dados[0]}')
    print(f'Valor..........: {dados[1]}')
    print(f'Serial.........: {dados[2]}')
    print(f'Setor..........: {dados[3]}')

# pesquisando um elemento do inventário
pesquisa = input('Digite o equipamento que deseja pesquisar: ')
for dados in inventario:
    if pesquisa == dados[0]:
        print(f'Valor......: {dados[1]}')
        print(f'Serial.....: {dados[2]}')

# depreciando um ítem
depreciacao = input('Digite o nome do equipamento que deseja depreciar: ')
for dados in inventario:
    if depreciacao == dados[0]:
        print(f'Valor normal......: {dados[1]}')
        depreciado = dados[1] * 0.9
        print(f'Valor depreciado....: {depreciado}')

# eliminando um ítem do inventário
excluir = int(input('Digite o serial que deseja excluir: '))
for dados in inventario:
    if excluir == dados[2]:
        inventario.remove(dados)

# exibir os dados do inventário
for dados in inventario:
    print(f'Equipamento...: {dados[0]}')
    print(f'Valor...: {dados[1]}')
    print(f'Serial...: {dados[2]}')
    print(f'Setor...: {dados[3]}')

# valores
valores = []
for dados in inventario:
    valores.append((dados[1]))
if len(valores) > 0:
    print(f'Equipamento mais caro.....: {max(valores)}')
    print(f'Equipamento mais barato...: {min(valores)}')
    print(f'Total dos equipamentos...: {sum(valores)}')


