from collections import deque

n, m = map(int, input().split())

grid = []

q = deque()
fresh = 0

for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

    for j in range(m):
        if grid[i][j] == 2:
            q.append((i, j))
        elif grid[i][j] == 1:
            fresh += 1

if fresh == 0:
    print(0)
else:
    time = 0

    directions = [
        (-1, 0),  
        (1, 0),   
        (0, -1),  
        (0, 1)   
    ]

    while q:
        size = len(q)
        rotted = False

        for _ in range(size):
            x, y = q.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
                        rotted = True

        if rotted:
            time += 1

    if fresh == 0:
        print(time)
    else:
        print(-1)

