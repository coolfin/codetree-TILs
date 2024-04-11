import sys
read = sys.stdin.readline

def init():
    global N
    #가로, 세로 초기화
    dp[0][0] = scores[0][0]
    for i in range(1, N):
        dp[i][0] = scores[i][0] + dp[i-1][0]
        dp[0][i] = scores[0][i] + dp[0][i-1]

N = int(read().rstrip())
scores = [list(map(int, read().rstrip().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for __ in range(N)]

init()
if N == 1: 
    print(scores[0][0])
    exit()
#dp
for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = scores[i][j] + max(dp[i][j-1] , dp[i-1][j])

print(dp[N-1][N-1])