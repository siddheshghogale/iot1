N=int(input("enter the size of chessboard"))

def snq(board,col):
    if col==N:
        print(board)
        return True
    for i in range(N):
        if issafe(board,i,col):
            board[i][col]=1
            if snq(board,col+1):
                return True
            board[i][col]=0
    return False


def issafe(board,row,col):
    for x in range(col):
        if board[row][x]==1:
            return False
    for x,y in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[x][y]==1:
            return False
    for x,y in zip(range(row,N,1),range(col,-1,-1)):
        if board[x][y]==1:
            return False
    return True
board=[[0 for x in range(N)] for y in range(N)]
if not snq(board,0):
    print("no solution found")




def TOH(n,s,d,a):
	if n==1:
		print ("Move disk 1 from source",s,"to destination",d)
		return
	TOH(n-1,s,a,d)
	print ("Move disk",n,"from source",s,"to destination",d)
	TOH(n-1,a,d,s)
