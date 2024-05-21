def solution(board):
    n = len(board)
    answer = n*n
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                board[i][j]=2
                answer-=1
                if 0<=i<n and 0<=j-1<n and board[i][j-1]==0:
                    board[i][j-1]=2
                    answer-=1
                if 0<=i<n and 0<=j+1<n and board[i][j+1]==0:
                    board[i][j+1]=2
                    answer-=1
                if 0<=i-1<n and 0<=j<n and board[i-1][j]==0:
                    board[i-1][j]=2
                    answer-=1
                if 0<=i+1<n and 0<=j<n and board[i+1][j]==0:
                    board[i+1][j]=2
                    answer-=1
                if 0<=i-1<n and 0<=j-1<n and board[i-1][j-1]==0:
                    board[i-1][j-1]=2
                    answer-=1
                if 0<=i+1<n and 0<=j-1<n and board[i+1][j-1]==0:
                    board[i+1][j-1]=2
                    answer-=1
                if 0<=i+1<n and 0<=j+1<n and board[i+1][j+1]==0:
                    board[i+1][j+1]=2
                    answer-=1
                if 0<=i-1<n and 0<=j+1<n and board[i-1][j+1]==0:
                    board[i-1][j+1]=2
                    answer-=1
    return answer