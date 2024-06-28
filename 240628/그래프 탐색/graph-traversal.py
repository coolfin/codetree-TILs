import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

res = 0
def dfs(index):
    global res 
    for vertex in graph[index]:
        if not visited[vertex]: 
            visited[vertex] = True
            res += 1
            dfs(vertex)
    

for _ in range(M):
    x, y = map(int, read().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

visited[1] = True
dfs(1)

print(res)