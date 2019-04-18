def instructions(main_list):
    num = 0  # type: int
    for i in range(1, 4):
        for j in range(1, 4):
            num += 1
            main_list.append(num)
    print('\nIn this game we will define the positions as shown below :')


def clear(main_list):
    for i in range(0, 9):
        main_list[i] = '-'


def update(main_list, position, c):
    main_list[position - 1] = c.upper()


def check(my_list, c):
    # Check in lines

    for i in range(0, 7, 3):
        if my_list[i] == my_list[i + 1] == my_list[i + 2] == c.upper():
            return True

    # check in columns
    for j in range(0, 3):
        if my_list[j] == my_list[j + 3] == my_list[j + 6] == c.upper():
            return True

    # Check first diagonal
    if my_list[0] == my_list[4] == my_list[8] == c.upper():
        return True

    # check second diagonal
    if my_list[2] == my_list[4] == my_list[6] == c.upper():
        return True

    return False


def show(main_list):
    print('\n')
    print(main_list[:3])
    print(main_list[3:6])
    print(main_list[6:9])


game = []
instructions(game)
show(game)

# Clear the matrix
clear(game)

# Input from player 1
print('\n Let\'s start with players choice, please enter the position coordinates.')

possibilities = list(range(1, 10))

result = False
while result == False and len(possibilities) > 0:
    position_player1 = int(input('\nPlayer 1 : '))
    loop = position_player1 in possibilities
    while not loop:
        print('Position already taken')
        position_player1 = int(input('\nPlayer 1 : '))
        loop = position_player1 in possibilities
    else:
        possibilities.pop(possibilities.index(position_player1))
        update(game, position_player1, 'x')
        show(game)
        result = check(game, 'x')
        if result:
            print('\n\tCongratulations Player 1 ! You have just Won the game !')
            break

    position_player2 = int(input('\nPlayer 2 : '))
    loop = position_player2 in possibilities
    while not loop:
        print('Position already taken')
        position_player2 = int(input('\nPlayer 2 : '))
        loop = position_player2 in possibilities
    else:
        possibilities.pop(possibilities.index(position_player2))
        update(game, position_player2, '0')
        show(game)
        result = check(game, 'x')
        if result:
            print('\n\tCongratulations Player 2 ! You have just Won the game !')
            break

if len(possibilities) == 0 and result == False:
    print("\nNO Winner for this game try next time !")
