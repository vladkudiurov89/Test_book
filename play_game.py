pl1 = "x"
pl2 = "o"
desert = " "
drawn_game = "tie"
numbers = 9


def d_instruction():
    print(
        """
      Welcome на поле "Крестики-нолики".
      Чтобы сделать ход, введи число от 0 до 8. Числа однозначно соотвествуют полям
      доски - так, как показано ниже:
                         -------------
                         | 0 | 1 | 2 |
                         -------------
                         | 3 | 4 | 5 |
                         -------------
                         | 6 | 7 | 8 |
                         -------------

      \n
      """)


def ask_1(question):
    xx1 = None
    while xx1 not in ("yes", "no"):
        xx1 = input(question).lower()
    return xx1


def ask_2(question, low, high):
    xx2 = None
    while xx2 not in range(low, high):
        xx2 = int(input(question))
    return xx2


def pieces():
    first = ask_1("Начинает первый игрок? (yes, no): ")
    if first == "yes":
        print("\n Начинает игрок")
        player = pl1
        bot = pl2
    else:
        print("\nНачинает бот")
        bot = pl1
        player = pl2
    return bot, player


def new_board():
    board = []
    for s in range(numbers):
        board.append(desert)
    return board


def d_board(board):
    print("\n\t", "-------------")
    print("\t", "|", board[0], "|", board[1], "|", board[2], "|")
    print("\t", "-------------")
    print("\t", "|", board[3], "|", board[4], "|", board[5], "|")
    print("\t", "-------------")
    print("\t", "|", board[6], "|", board[7], "|", board[8], "|")
    print("\t", "-------------")


def l_m(board):
    m = []
    for s in range(numbers):
        if board[s] == desert:
            m.append(s)
    return m


def winner(board):
    wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for r in wins:
        if board[r[0]] == board[r[1]] == board[r[2]] != desert:
            win1 = board[r[0]]
            return win1
        if desert not in board:
            return drawn_game
    return None


def pl_move(board, player, ):
    l = l_m(board)
    m = None
    while m not in l:
        m = ask_2("Игрок. Выберите одно поле (0 - 8):", 0, numbers)
        if m not in l:
            print("\n Это поле уже занято. Выберите другое.\n")
    print("Ок")
    return m


def bot_move(board, bot, player):
    board = board[:]
    bot_m = (0, 3, 2, 6, 8, 1, 5, 7, 4,)
    print("Мои ход", end=" ")
    for move in l_m(board):
        board[move] = bot
        if winner(board) == bot:
            print(move)
            return move
        board[move] = desert
    for moves in l_m(board):
        board[move] = player
        if winner(board) == player:
            print(move)
            return move
        board[move] = desert
    for move in bot_m:
        if move in l_m(board):
            print(move)
            return move


def next_turn(turn):
    if turn == pl1:
        return pl2
    else:
        return pl1


def c_winner(the_w, bot, player):
    if the_w != drawn_game:
        print("Три", the_w, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_w == bot:
        print("Победил бот \n")
    elif the_w == player:
        print("Победил игрок\n")
    elif the_w == drawn_game:
        print("Разойдемся с миром\n")


def decorator():
    d_instruction()
    bot, player = pieces()
    turn = pl1
    board = new_board()
    d_board(board)
    while not winner(board):
        if turn == player:
            move = pl_move(board, player)
            board[move] = player
        else:
            move = bot_move(board, bot, player)
            board[move] = bot
        d_board(board)
        turn = next_turn(turn)
    the_w = winner(board)
    c_winner(the_w, bot, player)


decorator()
input("Press Enter to exit.")
