###BFS 도중 최대값을 계속해서 비교한다.
# max값이 바뀌면 (R,C)가 저장돼있는 배열을 초기화하고 해당 좌표를 추가한다.
# max값이 안바뀌면 (R,C)를 배열에 추가한다.

###결과: 탐색을 마쳤을 때 
    # (R,C) 배열의 길이가 0이라면 움직이는 것을 종료하고 현 위치를 출력한다.
    # (R,C) 배열의 길이가 0보다 크다면, KEY = [행, 열] 순으로 오름차순 정렬을 한 뒤 0번 인덱스에 접근한다.

from collections import deque
import sys
read = sys.stdin.readline

N, K = map(int, read().rstrip().split())
arr = [list(map(int, read().rstrip().split())) for _ in range(N)]

r,c = map(int, read().rstrip().split())
r-=1
c-=1

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for k in range(K):
    max_val = -1
    max_arr = []

    deq = deque()
    deq.append((r,c))

    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    while deq:
        x, y = deq.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if 0<=cx<=N-1 and 0<=cy<=N-1 and not visited[cx][cy] and arr[r][c] > arr[cx][cy]:
                deq.append((cx, cy))
                visited[cx][cy] = True

                if arr[cx][cy] > max_val:
                    max_arr.clear()
                    max_val = arr[cx][cy]
                    max_arr.append([cx,cy])
                elif arr[cx][cy] == max_val:
                    max_arr.append([cx,cy])
    if max_arr:
        max_arr.sort(key=lambda x: (x[0], x[1]))
        r, c = max_arr[0]
    else:
        break

print(r+1, c+1)