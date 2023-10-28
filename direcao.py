import os

player = {'nome': 'Python', 'x': 0, 'y': 0}

def andar(direcao):
    if direcao == 'd':
        player['x'] += 1
    elif direcao == 'a':
        player['x'] -= 1
    elif direcao == 'w':
        player['y'] -= 1
    elif direcao == 's':
        player['y'] += 1

def linha(l):
    return l * 20

linha = linha('-')

while True:
    os.system('clear')

    print(linha)
    for y in range(5):
        print('\n')
        for x in range(10):
            if player['x'] == x and player['y'] == y:
                print('🚗', end='')
            else:
                print('🟩', end='')
    print(f'\n{linha}')

    direcao = input('Próxima direção (w,s,d,a): ')
    andar(direcao)