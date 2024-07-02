from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
arr = [list(map(int, read().rstrip().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for __ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

deq = deque()
deq.append([0,0])

while deq:
    x, y = deq.popleft()
    visited[x][y] = True

    for i in range(4):
        cx = x+dx[i]
        cy = y+dy[i]
        
        if cx >= N or cy >= M or cx < 0 or cy < 0 or not arr[cx][cy] or visited[cx][cy]: continue

        if cx == N-1 and cy == M-1:
            print(1)
            exit()
        deq.append([cx,cy])

print(0)