string, turn = raw_input().split()
board = [[None] * 8 for _ in range(8)]
print string, turn


def fill_board(board, string):
    row = 0
    for i in string.split('/'):
        column = 0
        for letter in i:
            if letter.isdigit():
                column = int(letter) - 1
            elif letter != 'p' or letter != 'P':
                board[row][column] = True
                column += 1
            else:
                board[row][column] = 'P'
    return board

for i in string.split('/'):
    for j in i:
        print j
print fill_board(board, string)
