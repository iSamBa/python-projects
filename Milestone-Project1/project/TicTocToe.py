
def instructions(lst):
    num=0  # type: int
    for i in range (1,4) :
        for j in range (1,4):
            num+=1
            lst.append(num)
    print('\nIn this game we will define the positions as shown below :')

def clear(lst):
    for i in range(0, 9):
        lst[i]='-'

def update(lst, position, c) :
    lst[position-1]=c.upper()

def check(myList, c):
    # Check in lines

    for i in range(0,7,3) :
        if myList[i] == myList[i + 1] == myList[i+2]==c.upper():
            return True

    #chenck in columns
    for j in range(0,3):
        if myList[j]==myList[j+3]==myList[j+6]==c.upper() :
            return True

    #Check first diagonal
    if myList[0]==myList[4]==myList[8]==c.upper() :
        return True

    #check second diagonal
    if myList[2]==myList[4]==myList[6]==c.upper() :
        return True

    return False



def show(lst) :
    print('\n')
    print(lst[:3])
    print(lst[3:6])
    print(lst[6:9])


lst=[]
instructions(lst)
show(lst)

#Clear the matrix
clear(lst)

#Input from player 1
print('\n Let\'s start with players choice, please enter the position coordinates.')

possibilities = list(range(1,10))

result = False
while result==False :
        position_player1=int(input('\nPlayer 1 : '))
        if position_player1 in possibilities :
            possibilities.pop(possibilities.index(position_player1))
            update(lst,position_player1,'x')
            show(lst)
            result=check(lst,'x')
            if result :
                print('\n\tCongratulations Player 1 ! You have just Won the game !')
                break

        else :
           print('Position already taken')

        position_player2=int(input('\nPlayer 2 : '))
        if position_player2 in possibilities:
            possibilities.pop(possibilities.index(position_player2))
            update(lst, position_player2, '0')
            show(lst)
            result=check(lst, 'o')
            if result:
                print('\n\tCongratulations Player 2 ! You have just Won the game !')
                break

        else:
            print('Position already taken')

