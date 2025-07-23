def make_game_board(width, height):
    board = []
    for i in range(height):
        board.append([])

    for i in range(height):
        for j in range(width):
            board[i].append([])
    return board

# print(make_game_board(5,7))
