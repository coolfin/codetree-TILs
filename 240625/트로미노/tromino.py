import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
arr = [list(map(int, read().rstrip().split())) for _ in range(N)]
arr_90 = list(zip(*arr))

res = float('-inf')

#2번블럭
for i in range(N):
    for j in range(M-2):
        row_total = sum(arr[i][j:j+3])
        col_total = sum(arr_90[i][j:j+3])

        res = row_total if res < row_total else res
        
for i in range(M):
    for j in range(N-2):
        col_total = sum(arr_90[i][j:j+3])
        res = col_total if res < col_total else res

#1번블럭 (부분행렬)
for i in range(N - 1):
    tar = []
    for j in range(M - 1):
        tar.append(arr[i][j])
        tar.append(arr[i][j+1])
        tar.append(arr[i+1][j])
        tar.append(arr[i+1][j+1])

        tar.sort()
        tar.pop(0)

        square_res = sum(tar)
        res = square_res if res < square_res else res
        tar.clear()

print(res)