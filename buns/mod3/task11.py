def check_winner(board):
    for row in board:
        for i in range(len(row) - k + 1):
            if all(cell == 'X' for cell in row[i:i + k]):
                return 'X'
            elif all(cell == 'O' for cell in row[i:i + k]):
                return 'O'

    for j in range(len(board[0])):
        for i in range(len(board) - k + 1):
            if all(row[j] == 'X' for row in board[i:i + k]):
                return 'X'
            elif all(row[j] == 'O' for row in board[i:i + k]):
                return 'O'

    for i in range(len(board) - k + 1):
        for j in range(len(board[0]) - k + 1):
            if all(board[i + x][j + x] == 'X' for x in range(k)):
                return 'X'
            elif all(board[i + x][j + x] == 'O' for x in range(k)):
                return 'O'

    for i in range(len(board) - k + 1):
        for j in range(k - 1, len(board[0])):
            if all(board[i + x][j - x] == 'X' for x in range(k)):
                return 'X'
            elif all(board[i + x][j - x] == 'O' for x in range(k)):
                return 'O'
    return 'draw'


k = int(input("Enter the size of field: "))
board = []

for _ in range(int(k)):
    board.append(input("Enter the {} line: \n".format(_ + 1)))

print("winner is ", check_winner(board))
