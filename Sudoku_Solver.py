board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]]


def print_board(board):
    if board == []:
        print("Not a Valid Board")
    for line in board:
        line_to_print = ""
        for word in line:
            line_to_print += str(word)
        print(line_to_print)
        #return line_to_print

def find_zero(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return(row,col)
                


def is_valid(board,row, col, value):
    coordinate = board[row][col]
    column = [row[col] for row in board]
    box_x = row // 3
    box_y = col // 3
    
    #making sure it's not a value that's already set
    if coordinate != 0:
        return "Not an Empty Space!"

    #checking if the value is in the row
    for item in board[row]:
        if item == value:
            return False
            #return "Value is in the row!"

    #checking if the value is in the column
        else:
            for item in column:
                if item == value:
                    return False
                    #return "Value is in the column!"
    
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == value and i != row and j != col:
                return False
    return True
    


def print_col(board,col):
    return [row[col] for row in board]
        

print_board(board)
#print(find_zero(board2))
print(is_valid(board, 0, 2, 6))

#print(print_col(board2,2))
