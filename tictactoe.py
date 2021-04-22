def print_grid():
    print('---------')
    print('|', ' '.join(current_grid[:3]), '|')
    print('|', ' '.join(current_grid[3:6]), '|')
    print('|', ' '.join(current_grid[6:9]), '|')
    print('---------')

def game_state():
    game_finished = False
    win = [current_grid[:3], current_grid[3:6], current_grid[6:9], current_grid[0:9:3], current_grid[1:9:3], current_grid[2:9:3], current_grid[0:9:4], current_grid[2:7:2]]
    if abs(current_grid.count('X') - current_grid.count('O')) > 1 or ('XXX' in win and 'OOO' in win):
        print('Impossible')
        game_finished = True
    elif 'XXX' in win:
        print('X wins')
        game_finished = True
    elif 'OOO' in win:
        print('O wins')
        game_finished = True
    elif '_' not in current_grid:
        print('Draw')
        game_finished = True
    elif '_' in current_grid:
        print('Game not finished')
    return game_finished

coords = ['1', '2', '3']

current_grid = '_________'

print_grid()

player_turn = 0


while True:
    cell = input('Enter the coordinates: >').split()
    if not cell[0].isnumeric() or not cell[1].isnumeric():
        print('You should enter numbers!')
        continue
    if cell[0] in coords and cell[1] in coords:
        row = cell[0]
        column = cell[1]
        index = (((int(row) - 1) * 3) + (int(column) + 2)) - 3
        if current_grid[index] == '_':
            if player_turn % 2 == 0:
                current_grid = current_grid[:index] + 'X' + current_grid[index + 1:]
            else:
                current_grid = current_grid[:index] + 'O' + current_grid[index + 1:]
            player_turn += 1
            print_grid()
            if game_state():
                break
        else:
            print('This cell is occupied! Choose another one!')
    else:
        print('Coordinates should be from 1 to 3!')