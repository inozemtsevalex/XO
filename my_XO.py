field = [["-"] * 3 for i in range(3)]
def show(field):
    print('       Y Y Y')
    print('       0 1 2')
    print(' -----------')
    for i in range(3):
        row_field = field[i]
        print(f" X {i} | {' '.join(str(j) for j in row_field)}")
def check_coord(x,y):
    if field [x] [y] != '-':
        return True
def check_win(turn, user):
    win_combination = (((0, 0), (0, 1), (0, 2)),
                       ((1, 0), (1, 1), (1, 2)),
                       ((2, 0), (2, 1), (2, 2)),
                       ((0, 2), (1, 1), (2, 0)),
                       ((0, 0), (1, 1), (2, 2)),
                       ((0, 0), (1, 0), (2, 0)),
                       ((0, 1), (1, 1), (2, 1)),
                       ((0, 2), (1, 2), (2, 2)))
    for coord in win_combination:
        symbols = []
        for c in coord:
            symbols.append(field[c[0]][c[1]])
        if symbols == [user] * 3:
            print(f" Выиграли {user} на {turn} ходу")
            return True
    return False
def input_coord():
    while True:
        coord = input("Сделайте ваш ход: ").split()
#       print(coord)
        if len(coord) != 2:
            print("Необходимо указать две координаты X и Y через пробел!")
            continue
        if not (coord[0].isdigit()) or not (coord[1].isdigit()):
            print("Введите координаты в виде целых чисел X и Y")
            continue
        if int(coord[0]) < 0 or int(coord[0]) > 2 or int(coord[1]) < 0 or int(coord[1]) > 2:
            print('Координаты должны быть в диапазоне от 0 до 2')
            continue
        if check_coord(int(coord[0]), int(coord[1])):
            print("Данная клетка занята!")
            continue
        break
    return int(coord[0]), int(coord[1])

count = 0
while True:
    show(field)
    if count % 2 == 0:
        print('Ходит игрок с крестиками')
        user = 'X'
    else:
        print('Ходит игрок с ноликами')
        user = '0'
    x, y = input_coord()
    print('ход номер: ', count + 1)
    if count < 9:
        field [x][y] = user
        if check_win(count+1, user):
            show(field)
            break
        count += 1
    if count == 9:
        print('Игра завершилась вничью')
        break




