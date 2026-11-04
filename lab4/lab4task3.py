import heapq

graph={
    "S":[("A",1),("B",4)],
    "A":[("C",2)],
    "B":[("G",5)],
    "C":[("G",3)],
    "G":[]
}

def astar(h):
    pq=[(h["S"],0,"S",["S"])]
    best={"S":0}
    processed=[]
    expanded=0

    while pq:
        f,g,node,path=heapq.heappop(pq)

        if g!=best[node]:
            continue

        processed.append(node)

        if node=="G":
            return g,path,processed,expanded

        expanded+=1

        for nxt,w in graph[node]:
            ng=g+w

            if ng<best.get(nxt,float("inf")):
                best[nxt]=ng
                heapq.heappush(pq,(ng+h[nxt],ng,nxt,path+[nxt]))

    return None,[],processed,expanded

def path_cost(path):
    total=0
    for a,b in zip(path,path[1:]):
        total+=next(w for n,w in graph[a] if n==b)
    return total

heuristics=[
    ("Original A*",{"S":5,"A":4,"B":4,"C":2,"G":0}),
    ("Modified A*",{"S":5,"A":4,"B":4,"C":10,"G":0})
]

for name,h in heuristics:
    cost,path,processed,expanded=astar(h)
    print(name)
    print("Heuristic h(C):",h["C"])
    print("Path:"," -> ".join(path))
    print("Returned Cost:",cost)
    print("Independent Cost:",path_cost(path))
    print("Processed Nodes:"," -> ".join(processed))
    print("Expanded Nodes:",expanded)
    print()