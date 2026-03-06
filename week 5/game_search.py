board = [' '] * 9
def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in w)
def full():
    return ' ' not in board
def minimax(ai):
    if win('O'): return 1
    if win('X'): return -1
    if full(): return 0

    best = -2 if ai else 2
    for i in range(9):
        if board[i]==' ':
            board[i] = 'O' if ai else 'X'
            val = minimax(not ai)
            board[i] = ' '
            best = max(best,val) if ai else min(best,val)
    return best

def best_move():
    move, best = -1, -2
    for i in range(9):
        if board[i]==' ':
            board[i]='O'
            val = minimax(False)
            board[i]=' '
            if val>best:
                best,move = val,i
    return move

while not win('X') and not win('O') and not full():
    print(board[0:3],"\n",board[3:6],"\n",board[6:9])
    m = int(input("Move(0-8): "))
    if board[m]==' ':
        board[m]='X'
        if not win('X') and not full():
            board[best_move()]='O'

print(board[0:3],"\n",board[3:6],"\n",board[6:9])
if win('X'): print("You win")
elif win('O'): print("AI wins")
else: print("Draw")

