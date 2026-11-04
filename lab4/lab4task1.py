
import heapq
def astar(g,h,s,goal):
    pq=[(h[s],0,s,[s])]
    best={s:0}
    while pq:
        f,c,n,p=heapq.heappop(pq)
        if c!=best[n]:continue
        if n==goal:return c,p
        for x,w in g.get(n,[]):
            nc=c+w
            if nc<best.get(x,float("inf")):
                best[x]=nc
                heapq.heappush(pq,(nc+h[x],nc,x,p+[x]))
g={"S":[("A",1),("B",4)],"A":[("C",2)],"B":[("G",5)],"C":[("G",3)],"G":[]}
h={"S":5,"A":4,"B":4,"C":2,"G":0}
print(astar(g,h,"S","G"))
