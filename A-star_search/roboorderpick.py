import heapq

R, C = 5, 4

def astar(s, g):
    h = lambda a: abs(a[0]-g[0]) + abs(a[1]-g[1])
    pq, dist, parent = [(0, s)], {s: 0}, {}

    while pq:
        _, cur = heapq.heappop(pq)
        if cur == g:
            path = [cur]
            while cur in parent:
                cur = parent[cur]
                path.append(cur)
            return path[::-1]

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = cur[0]+dx, cur[1]+dy
            if 0 <= nx < R and 0 <= ny < C:
                nxt, nd = (nx, ny), dist[cur] + 1
                if nxt not in dist or nd < dist[nxt]:
                    dist[nxt] = nd
                    heapq.heappush(pq, (nd + h(nxt), nxt))
                    parent[nxt] = cur
    return []

orders = [(2,1), (4,3), (1,2)]
start, path = (0,0), []

for o in orders:
    p = astar(start, o)
    path += p[:-1]
    start = o

print(path + [orders[-1]])