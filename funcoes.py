# def minha_funcao(valor1, valor2):
#     return valor1 + valor2

# while True:
#     valor1 = int(input('Valor 1: '))
#     valor2 = int(input('valor 2: '))

#     resposta = minha_funcao(valor1, valor2)
    
#     print(f'{valor1} + {valor2} = {resposta}')
# title = '@ Fluxo caixa'
# def linha(l):
#     return l * len(title)

# linha = linha('-')

# fluxo_caixa = []

# print(linha)
# print(f'{title}')
# print(linha)
# print('1 - Adicionar receita')
# print('2 - Adicionar despesa')
# print('\nDigite outro número para encerrar #\n')

# def adicionar_transacao():
#     nome = input('Nome: ')
#     valor = float(input('Valor:' ))
#     fluxo_caixa.append({
#             'nome': nome,
#             'valor': valor
#         })

# while True:
#     opc = int(input('Digite a opção: '))
#     if opc == 1:
#         adicionar_transacao()
#     elif opc == 2:
#         adicionar_transacao()
#     else:
#         break
# nota fiscal
# total = 0
# for fc in fluxo_caixa:
#     print(f'Nome: {fc["nome"]}\nvalor: R${fc["valor"]}')
#     total = total + fc['valor']
# print(f'Saldo atual: R${total}')

# calcular IMC
# def calcular_imc(peso, altura):
#     imc = peso / (altura ** 2)
#     return imc

# peso = float(input('Peso (kg): '))
# altura = float(input('Altura (m): '))

# imc = calcular_imc(peso, altura)
# print(f'Seu IMC é: {imc:.2f}')
