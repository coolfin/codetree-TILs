import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
arr = [list(map(int, read().rstrip().split())) for i in range(N)]
arr_90 = list(zip(*arr))

def find(array):
    global M
    for i in range(M-1):
        if array[i] != array[i+1]: return False
    return True

res = 0
for i in range(N):
    for j in range(len(arr[i]) - M + 1):
        p_arr = arr[i][j:j+M]
        if find(p_arr): 
            res += 1
            break

for i in range(N):
    for j in range(len(arr_90[i]) - M + 1):
        p_arr = arr_90[i][j:j+M]
        if find(p_arr): 
            res += 1
            break

        

print(res)