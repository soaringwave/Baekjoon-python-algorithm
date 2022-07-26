# 7576
# 토마토
from collections import deque

row, col = map(int, input().split())

# 토마토 상자 그리기
graph = []
for i in range(col):
    graph.append(list(map(int, input().split())))

# 동서남북 이동 좌표
mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]

# 토마토를 탐색할 좌표 큐
queue = deque()

def count_tomato(graph):
    # 익은 토마토 찾기
    for i in range(col):
        for j in range(row):
            # 토마토가 익었다면
            if graph[i][j] == 1:
                queue.append((i, j))
    bfs_tomato()
    # 토마토가 익었는지 확인하기
    max_day = 0
    for i in range(col):
        for j in range(row):
            # 하나라도 안 익은 토마토가 있다면
            if graph[i][j] == 0:
                return -1
            if graph[i][j] > max_day:
                max_day = graph[i][j]
    return max_day - 1


def bfs_tomato():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            # 토마토 판 안의 좌표이고, 토마토가 있다면
            if 0 <= nx < col and 0 <= ny < row and graph[nx][ny] != -1:
                # 토마토가 익지 않았다면
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
                # 더 짧은 날에 익을 수 있다면
                elif graph[nx][ny] > graph[x][y] + 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
                else:
                    continue
    return


print(count_tomato(graph))