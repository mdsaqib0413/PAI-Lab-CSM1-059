import heapq

R, C = 5, 4

def astar(start, goal):
    h = lambda a: abs(a[0]-goal[0]) + abs(a[1]-goal[1])
    pq = [(0, start)]
    g = {start: 0}
    parent = {}

    while pq:
        _, cur = heapq.heappop(pq)
        if cur == goal:
            path = [cur]
            while cur in parent:
                cur = parent[cur]
                path.append(cur)
            return path[::-1]

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = cur[0]+dx, cur[1]+dy
            if 0 <= nx < R and 0 <= ny < C:
                nxt = (nx, ny)
                new_g = g[cur] + 1
                if nxt not in g or new_g < g[nxt]:
                    g[nxt] = new_g
                    heapq.heappush(pq, (new_g + h(nxt), nxt))
                    parent[nxt] = cur

print(astar((0,0), (4,3)))