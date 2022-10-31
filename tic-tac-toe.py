def show(field):
    print(' ', 0, 1, 2)
    for i in range(3):
        print(i, end=' ')
        print(*field[i])


def check_win(field):
    win_keys = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for key in win_keys:
        symbols = []
        for c in key:
            symbols.append(field[c[0]][c[1]])
        if symbols in (["x", "x", "x"], ["0", "0", "0"]):
            print(f"Победа за {'крест' if symbols[0] == 'x' else 'нол'}иком!!!")
            return True
    return False


def check_move(field, flag):
    try:
        x, y = map(int, input(f"{'Крест' if flag == 'x' else 'Нол'}ик твой ход.\n"))
        if -1 < x < 3 and -1 < y < 3:
            if field[x][y] == '-':
                print(x, y)
                return x, y
            else:
                print('Данное поле занято!')
                return check_move(field, flag)
        else:
            print('Некорректные данные!')
            return check_move(field, flag)
    except ValueError:
        print('Некорректные данные!')
        return check_move(field, flag)


def move(field, flag, npc=False):
    if npc:
        free_place = set()
        for index, value in enumerate(field):
            if '-' in value:
                free_place.add((index, value.index('-')))
        x, y = map(int, free_place.pop())
        field[x][y] = flag
    else:
        x, y = check_move(field, flag)
        field[x][y] = flag
    show(field)
    return check_win(field)


def game_loop(npc=False):
    field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    show(field)
    for flag in 'x0x0x0x0x':
        if flag == 'x':
            if move(field, flag):
                start(first=False)
                break
        else:
            if move(field, flag, npc):
                start(first=False)
                break
        continue
    else:
        start(first=False)
        print('Победила дружба!')


def start(first=True):
    if first:
        if input('Добро пожаловать, хотите сыграть?\nY/N\n').upper() in 'YН':
            print('Координаты вводятся без пробелов,\n'
                  'Сначала идёт строка, затем столбец\n'
                  'Что-бы поставить крестик в левый нижний угол,\n'
                  'нужно ввести координаты "20"')
            print('   0  1  2\n'
                  '0 00 01 02\n'
                  '1 10 11 12\n'
                  '2 X  21 22')
        else:
            print('До свидания!')
            return None
    if input('Будем играть против компьютера?\nY/N\n').upper() in 'YН':
        print('Удачи в игре против компьютера, первый ход за вами.')
        game_loop(npc=True)
    else:
        print('Игра с другом началась, первыми ходят крестики')
        game_loop()


start()
