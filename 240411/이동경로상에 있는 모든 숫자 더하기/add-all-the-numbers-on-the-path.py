import sys
read = sys.stdin.readline

N, T = map(int, read().rstrip().split())
alpha = read().rstrip()

nums = [list(map(int, read().rstrip().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
idx = 0

x , y = N//2, N//2
res = nums[x][y]
for a in alpha:
    if a == 'R':
        idx = (idx+1)%4        
    elif a == 'L':
        idx = (idx+3)%4
    else:
        cx = x + dx[idx]
        cy = y + dy[idx]

        if cx < 0 or cx >= N or cy < 0 or cy >= N : continue

        res += nums[cx][cy]
        x = cx
        y = cy
print(res)