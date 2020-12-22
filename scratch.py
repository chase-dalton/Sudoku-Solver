
def is_in_box(board,row, col, value):
    box_x = row // 3
    box_y = col // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == value and i != row and j != col:
                return True
    

