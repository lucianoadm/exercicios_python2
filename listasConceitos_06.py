# faça um programa que receba equipamentos
# e posteriormente alguns desses equipamentos
# sejam excluídos da lista
maquinario = []
seriais = []
departamento = []
while True:
    maquinario.append(input('Digite o equipamento: '))
    seriais.append(int(input('Digite o serial: ')))
    departamento.append(input('Digite o departamento: '))
    resposta = input('digite (S) sair ou (C) para continuar: ').upper()
    if resposta == 'S':
        print('\nPrograma encerrado!')
        break
    else:
        continue
print('\nResumo:')
for x in range(len(maquinario)):
    print(f'Maquinário.....: {maquinario[x]}')
    print(f'Serial.........: {seriais[x]}')
    print(f'Departamento...: {departamento[x]}')
    print()

serial = int(input('Digite o serial que deseja excluir: '))
for i in range(len(maquinario)):
    if seriais[i] == serial:
        del maquinario[i]
        del seriais[i]
        del departamento[i]
        break

for i in range(len(maquinario)):
    print(f'Maquinário....: {maquinario[i]}')
    print(f'Serial........: {seriais[i]}')
    print(f'Departamento..: {departamento[i]}')
    print()

