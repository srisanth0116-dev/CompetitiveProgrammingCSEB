V, E = map(int, input().split())

capacity = [[0] * V for _ in range(V)]

for _ in range(E):
    u, v, c = map(int, input().split())
    capacity[u][v] += c

def dfs(u, t, flow):
    if u == t:
        return flow

    visited[u] = True

    for v in range(V):
        if not visited[v] and capacity[u][v] > 0:
            new_flow = min(flow, capacity[u][v])

            result = dfs(v, t, new_flow)

            if result > 0:
                capacity[u][v] -= result
                capacity[v][u] += result
                return result

    return 0

source = 0
sink = V - 1
max_flow = 0

while True:
    visited = [False] * V

    flow = dfs(source, sink, 10**9)

    if flow == 0:
        break

    max_flow += flow

print(max_flow)

