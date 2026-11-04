import heapq

graph = {
    'A': [('B', 1), ('C', 6)],
    'B': [('D', 2), ('E', 1)],
    'C': [('F', 2), ('G', 6)],
    'D': [],
    'E': [('G', 1)],
    'F': [],
    'G': []
}

def ucs(start, goal):
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, cost

        for next_node, weight in graph[node]:
            if next_node not in visited:
                heapq.heappush(
                    queue,
                    (cost + weight, next_node, path + [next_node])
                )

    return None, float('inf')

path, cost = ucs('A', 'G')

print("Path:", path)
print("Total Cost:", cost)