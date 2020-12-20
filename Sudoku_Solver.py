board = [[5, 3, 0, 7, 0]]
#,
#[6, 0, 0, 1, 9, 5, 0, 0, 0],
#[0, 9, 8, 0, 0, 0, 0, 6, 0],
#[8, 0, 0, 0, 6, 0, 0, 0, 3],
#[4, 0, 0, 8, 0, 3, 0, 0, 1],
#[7, 0, 0, 0, 2, 0, 0, 0, 6],
#[0, 6, 0, 0, 0, 0, 2, 8, 0],
#[0, 0, 0, 4, 1, 9, 0, 0, 5],
#[0, 0, 0, 0, 8, 0, 0, 7, 9]]

def print_board(board):
    if board == []:
        print("Not a Valid Board")
    for line in board:
        line_to_print = ""
        for word in line:
            line_to_print += str(word)
        print(line_to_print)

def find_zero(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                print(row,col)
                

find_zero(board)


