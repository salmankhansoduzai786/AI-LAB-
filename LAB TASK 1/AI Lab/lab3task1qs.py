from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}


def bfs(start, goal):
    queue = deque([(start, [start])])
    seen = {start}
    visit_order = []

    while queue:
        node, path = queue.popleft()
        visit_order.append(node)

        if node == goal:
            return path, visit_order

        for neighbour in graph[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None, visit_order


def dfs(start, goal):
    stack = [(start, [start])]
    seen = set()
    visit_order = []

    while stack:
        node, path = stack.pop()

        if node in seen:
            continue

        seen.add(node)
        visit_order.append(node)

        if node == goal:
            return path, visit_order

        for neighbour in reversed(graph[node]):
            if neighbour not in seen:
                stack.append((neighbour, path + [neighbour]))

    return None, visit_order


if __name__ == "__main__":

    bp, bo = bfs("A", "G")
    dp, do = dfs("A", "G")

    print("BFS path:", " -> ".join(bp))
    print("BFS visit order:", " -> ".join(bo))

    print()

    print("DFS path:", " -> ".join(dp))
    print("DFS visit order:", " -> ".join(do))