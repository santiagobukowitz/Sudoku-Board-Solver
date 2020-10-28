print("Welcome to my Sudoku Solver!")

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],    #I set up a sudoku board using a basic example
    [8,0,0,0,6,0,0,0,3],    #that was available online.  
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
 ]

def solver(bd):
    f = empty_space(bd)
    if not f:
        return True
    else:
        r,c = f
    for i in range(1,10):
        if validity(bd, i, (r,c)):
            bd[r][c] = i

            if solver(bd):
                return True

            bd[r][c] = 0

    return False
            

    
    


def validity(bd, num, pos):

    #check if the rows are valid
    for i in range(len(bd[0])):
        if bd[pos[0]][i] == num and pos[1] !=i:
            return False

    #check if the columns are valid
    for i in range(len(bd)):
        if bd[i][pos[1]] == num and pos[0] !=i:
            return False
    
    #Determine position on the board
    b_x  = pos[1] // 3
    b_y = pos[0] // 3

    for i in range(b_y*3, b_y*3 + 3):
        for j in range(b_x*3, b_x*3 + 3):
            if bd[i][j] == num and (i,j) !=pos:
                return False
    return True



def visual_board(bd):
    
    for i in range(len(bd)):
        if i % 3 == 0 and i !=0:
            print("-------------------------")

    
        for j in range(len(bd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
    
            if j == 8:
                print (bd[i][j])
            else:
                print(str(bd[i][j]) + " ", end="")

def empty_space(bd):
    
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            if bd[i][j] == 0:
                return (i,j)
    return None


print("-------------------------")
print("The original, untouched sudoku board")
print("-------------------------")
visual_board(board)
solver(board)
print("------------------------")
print("The sudoku board solved:")
print("------------------------")
visual_board(board)

