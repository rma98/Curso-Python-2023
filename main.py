# teste
# print('Quero meu primeiro emprego!')
# boolean
# is_python, is_java = True, False
# python, java = is_python, is_java
# print(f'É python? {python}\nÉ java? {java}')
# armazenando condições
# ingressos, compradores = 50, 250
# tem_ingresso_suficiente = (ingressos >= compradores)
# print(f'Tem ingressos suficientes? {tem_ingresso_suficiente}')
# variáveis
# nome, idade, peso = 'Programador Python', 27, 70.3
# print(f'Nome: {nome}\nIdade: {idade}\nPeso: {peso}')
# input - > armazena entrada de dados do usuário
# nome = input('Nome: ')
# idade = int(input('Idade: '))
# peso = float(input('Peso: '))
# print(f'Nome: {type(nome)}\nIdade: {type(idade)}\nPeso: {type(peso)}')
# operadores
# soma = 1 + 1
# subtracao = 2 - 1
# multiplicacao = 4 * 4
# divisao = 10 / 2
# potencia = 7 ** 2
# print(f'Soma: {soma}\nSubtração: {subtracao}\nMultiplicacao: {multiplicacao}\nDivisão: {divisao}\nPotencia: {potencia}')
# condicionais
# valor1, valor2 = 10, 50
# if valor1 > valor2:
#     print(f'{valor1} é maior que {valor2}')
# else:
#     print(f'{valor2} é maior que {valor1}')
# idade = int(input('Idade: '))
# if idade >= 18:
#     print('PERMITIDO!')
# else:
#     print('BLOQUEADO!')
# salario = float(input('Salário: R$'))
# if salario <= 3000:
#     print('programador júnior')
# elif salario > 3000 and salario <= 6000:
#     print('programador plênior')
# elif salario > 6000 and salario <= 15000:
#     print('programador sênior')
# else:
#     print('gerente de projetos')
# listas
# lista_numeros, lista_strings, lista_decimais, lista_vazia, numeros  = [1, 2, 3], ['Jõao', 'Maria', 'Bruxa'], [10.8, 15.2, 33.3], [], [10, 9, 8, 7, 6]
# print(f'{lista_numeros[0]}\n{lista_numeros[1]}\n{lista_numeros[2]}')
# lista_numeros[0] = 5
# print(f'\n{lista_numeros[0]}\n{lista_numeros[1]}\n{lista_numeros[2]}\nInteiros: {lista_numeros}\nStrings: {lista_strings}\nFlutuantes: {lista_decimais}\nLista Vazia: {lista_vazia}')
# lista_vazia.append('Olá')
# lista_vazia.append('Mundo')
# print(f'Adiciona valores a lista vazia: {lista_vazia}')
# print(f'Tamanho da lista: {len(numeros)}\nMenor valor: {min(numeros)}\nMaior valor: {max(numeros)}')
# loops
# for x in range(10):
#     print(x)
# while True:
#     print('Se eu rodar o script meu pc morre')
# notas, contador = [], 1
# for x in range(3):
#     codigo_aluno = input('RM: ')
#     nota = float(input('Nota: '))
#     resultado = [codigo_aluno, nota]
#     notas.append(resultado)
# print(f'Notas: {notas}\nQuantidade de notas: {len(notas)}')
# for n in notas:
#     codigo_aluno = n[0]
#     nota = n[1]
#     print(f'O RM {codigo_aluno} tirou a nota: {nota}')
# while contador <= 3:
#     codigo_aluno = input('RM: ')
#     nota = float(input('Nota: '))
#     resultado = [codigo_aluno, nota]
#     notas.append(resultado)
#     # alternativa: contador += 1
#     contador = contador + 1
# print(f'Quantidade de notas: {len(notas)}')
# dicionários
# pessoa = {
#     'nome': 'Programador Python',
#     'idade': 27,
#     'peso': 70.2
# }
# print(f'{pessoa["nome"]}\n{pessoa["idade"]}\n{pessoa["peso"]}')
# informações do jogador
# player = {
#     'nome': 'Guilherme',
#     'level': 1,
#     'hp': 100,
#     'exp': 0,
#     'dano': 5
# }
# lista de inimigos
# npcs = [
#     {'nome': 'Monstrinho', 'dano': 2, 'hp': 50, 'exp': 5},
#     {'nome': 'Monstro', 'dano': 5, 'hp': 100, 'exp': 10},
#     {'nome': 'Monstrão', 'dano': 10, 'hp': 150, 'exp': 15},
#     {'nome': 'chefão', 'dano': 25, 'hp': 200, 'exp': 20}
# ]
# print(f'{player}\n{npcs}')