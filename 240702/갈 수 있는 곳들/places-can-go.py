import sys
from collections import deque
read = sys.stdin.readline

N, K = map(int, read().rstrip().split())
arr = [list(map(int, read().rstrip().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

res = 0
for _ in range(K):
    r, c = map(int, read().rstrip().split())
    r -= 1
    c -= 1
    deq = deque()
    deq.append((r,c))

    while deq:
        x, y = deq.popleft()

        if visited[x][y]: continue
        visited[x][y] = True

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if 0<=cx<=N-1 and 0<=cy<=N-1 and not visited[cx][cy] and not arr[cx][cy]:
                deq.append((cx,cy))
                res += 1
        
print(res)