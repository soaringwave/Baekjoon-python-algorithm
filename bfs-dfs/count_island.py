# 4963
# 섬의 개수
import sys
sys.setrecursionlimit(10 ** 6)

# 다음 자표 이동 범위
dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, 1, -1]

def dfs(x, y):
    # 방문한 노드는 0으로 바꿔줌
    graph[x][y] = 0
    # 현재 노드 기준으로 동서남북, 대각선으로 이동
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < height and 0 <= ny < width:
            if graph[nx][ny] == 1:
                dfs(nx, ny)


width, height = map(int, input().split())

while width != 0 and height != 0:
    graph = [[] for _ in range(height)]
    count = 0
    for i in range(height):
        graph[i] = list(map(int, input().split()))
    for i in range(height):
        for j in range(width):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)
    width, height = map(int, input().split())
