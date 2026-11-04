

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path

    if limit == 0:
        return "CUTOFF", None

    cutoff_occurred = False

    for child in graph[node]:
        if child not in path:
            status, result = dls(
                child, goal, limit - 1, path + [child]
            )

            if status == "FOUND":
                return status, result

            if status == "CUTOFF":
                cutoff_occurred = True

    if cutoff_occurred:
        return "CUTOFF", None

    return "FAILURE", None

print("DEPTH LIMITED SEARCH (DLS)")

for limit in range(1, 5):
    status, path = dls("A", "G", limit, ["A"])

    print("\nDepth Limit:", limit)
    print("Status:", status)

    if path:
        print("Path:", " -> ".join(path))
    else:
        print("Path: Not Found")


# Iterative Deepening Depth First Search
def iddfs(start, goal, max_depth):
    attempted_limits = []

    for depth in range(max_depth + 1):
        attempted_limits.append(depth)

        status, path = dls(
            start, goal, depth, [start]
        )

        if status == "FOUND":
            return status, path, attempted_limits

        if status == "FAILURE":
            return status, None, attempted_limits

    return "CUTOFF", None, attempted_limits


# Test IDDFS with different maximum depths
print("\n\nITERATIVE DEEPENING DFS (IDDFS)")

for max_depth in range(1, 5):
    status, path, attempts = iddfs(
        "A", "G", max_depth
    )

    print("\nMaximum Depth:", max_depth)
    print("Status:", status)
    print("Limits Attempted:", attempts)

    if path:
        print("Path:", " -> ".join(path))
    else:
        print("Path: Not Found")
