# 24479
# dfs
# 참고(https://coooco.tistory.com/57)

# 재귀 주의
import sys
sys.setrecursionlimit(10 ** 6)

# 정점 수, 간선 수, 시작 정점 입력받기
n, m, r = map(int, sys.stdin.readline().split())

# 그래프
# 배열 = [노드][노드와 연결된 노드들]
# 연결노드 그래프 초기화(1번노드와 인덱스 값이 같게 하기 위해서 n+1로 )
# [[],[],[],[],[],[]]
graph = [[] for _ in range(n + 1)]

# 원소 개수는 n개, 0으로 초기화
visited = [0] * (n + 1)
count = 1

def dfs(graph, v, visited):
    global count
    # 순서 입력
    visited[v] = count
    for i in graph[v]:
        if visited[i] == 0:
            count += 1
            dfs(graph, i, visited)

# 그래프 입력받기
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 그래프 오름차순으로 정렬
for i in range(n + 1):
    graph[i].sort()

# dfs 실행
dfs(graph, r, visited)

# 순서대로 출력
for i in range(n + 1):
    if i != 0:
        print(visited[i])