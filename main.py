doska = ["*", "*", "*",
         "*", "*", "*",
         "*", "*", "*"]
name = input("Кто ты воин?\n-")


def printd():
    for i in range(3):
        print(doska[i * 3] + "  " + doska[i * 3 + 1] + "  " + doska[i * 3 + 2])


def win(igrok):
    win = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
    ]
    for i in win:
        if doska[i[0]] == igrok and doska[i[1]] == igrok and doska[i[2]] == igrok:
            return True
    return False


def draw():
    for i in doska:
        if i == "*":
            return False
    return True


def move():
    while True:
        move = int(input(f"{name}, ходи (1-9): ")) - 1
        if move >= 0 and move < 9 and doska[move] == "*":
            doska[move] = 'X'
            break
        else:
            print("Занято или неверный ввод. Выбери другую.")


# Признаюсь честно, эту часть посмотрел вгпт но основную суть понял :/
def minimax(is_maximizing):
    if win('O'):
        return 1
    if win('X'):
        return -1
    if draw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if doska[i] == "*":
                doska[i] = 'O'
                score = minimax(False)
                doska[i] = "*"
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if doska[i] == "*":
                doska[i] = 'X'
                score = minimax(True)
                doska[i] = "*"
                best_score = min(score, best_score)
        return best_score


def computer_move():
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if doska[i] == "*":
            doska[i] = 'O'
            score = minimax(False)
            doska[i] = "*"
            if score > best_score:
                best_score = score
                best_move = i
    doska[best_move] = 'O'


def X_O():
    while True:
        printd()
        move()
        if win('X'):
            printd()
            print(f"{name} победил")
            break
        if draw():
            printd()
            print("Ничья")
            break

        computer_move()
        if win('O'):
            printd()
            print("Компьютер победил, лох")
            break
        if draw():
            printd()
            print("Ничья")
            break


X_O()