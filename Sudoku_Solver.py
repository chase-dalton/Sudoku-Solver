board =[[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def print_board(board):
    print("\n\n".join(["  ".join([str(i) for i in line]) for line in board]))
    
def find_zero(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return[row,col]

    return None


def is_valid(arg_board,row, col, value):
    coordinate = arg_board[row][col]
    column = [row[col] for row in arg_board]
    box_y = row // 3
    box_x = col // 3
    
    #making sure it's not a value that's already set
    if coordinate != 0:
        return "Not an Empty Space!"

    candidates = [*arg_board[row], *column]
    #checking if the value is in the same 3x3 grid
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            candidates = [*candidates, arg_board[i][j]]
    
    return value not in candidates


def solve_square(board):
    find = find_zero(board)
    if not find:
        return True
    else:
        row, col = find
        valid_pos = [x for x in range(1,10) if is_valid(board, row, col, x)]
        for value in valid_pos:
            board[row][col] = value
            if solve_square(board):
                return True
        board[row][col] = 0
        return False

print(solve_square(board))
print_board(board)
