import heapq

graph={
    "S":[("A",1),("B",4)],
    "A":[("C",2)],
    "B":[("G",5)],
    "C":[("G",3)],
    "G":[]
}

h={"S":5,"A":4,"B":4,"C":2,"G":0}

def search(graph,h,start,goal):
    pq=[(h[start],0,start,[start])]
    best={start:0}
    processed=[]
    expanded=0

    while pq:
        f,g,node,path=heapq.heappop(pq)

        if g!=best[node]:
            continue

        processed.append(node)

        if node==goal:
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

for name,heuristic in [("A*",h),("UCS",{n:0 for n in graph})]:
    cost,path,processed,expanded=search(graph,heuristic,"S","G")
    print(name,"Results")
    print("Path:"," -> ".join(path))
    print("Path Cost:",cost)
    print("Independent Cost:",path_cost(path))
    print("Processed Nodes:"," -> ".join(processed))
    print("Expanded Nodes:",expanded)
    print()