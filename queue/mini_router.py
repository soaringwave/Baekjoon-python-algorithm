# 15828
# Router
import sys
from collections import deque

input = sys.stdin.readline
buffer_limit = int(input())

queue = deque([])

answer = int(input())
while answer != -1:
    if answer > 0 and len(queue) < buffer_limit:
        queue.append(answer)
    elif answer == 0:
        queue.popleft()
    answer = int(input())

if queue:
    for i in queue:
        print(i, end=" ")
else:
    print('empty')