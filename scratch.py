board =[[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def is_in_box(board,row, col, value):
    box_x = row // 3
    box_y = col // 3
    starting_location = board[row][col]
    print(f"Starting Location: ({row}, {col}), value: {starting_location}")
    for i in range(box_y*3, box_y*3 + 3):
        #print(f"I: {i}")
        for j in range(box_x * 3, box_x*3 + 3):
            #print(board[i][j])
            #print(f"J: {j}")
            if board[i][j] == value and i != row and j != col:
                return True
    

is_in_box(board,5,5,3)