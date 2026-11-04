def minimax(depth,index,max_turn,scores,target,counter):
    if depth==target:
        counter[0]+=1
        return scores[index]

    if max_turn:
        values=[]
        for i in range(2):
            values.append(minimax(depth+1,index*2+i,False,scores,target,counter))
        return max(values)
    else:
        values=[]
        for i in range(2):
            values.append(minimax(depth+1,index*2+i,True,scores,target,counter))
        return min(values)

def alphabeta(depth,index,max_turn,scores,target,alpha,beta,counter):
    if depth==target:
        counter[0]+=1
        return scores[index]

    if max_turn:
        value=float("-inf")
        for i in range(2):
            value=max(value,alphabeta(depth+1,index*2+i,False,scores,target,alpha,beta,counter))
            alpha=max(alpha,value)
            if alpha>=beta:
                break
        return value
    else:
        value=float("inf")
        for i in range(2):
            value=min(value,alphabeta(depth+1,index*2+i,True,scores,target,alpha,beta,counter))
            beta=min(beta,value)
            if alpha>=beta:
                break
        return value

def run_case(name,scores):
    target=3
    mini_count=[0]
    mini_value=minimax(0,0,True,scores,target,mini_count)
    ab_count=[0]
    ab_value=alphabeta(0,0,True,scores,target,float("-inf"),float("inf"),ab_count)

    print(name)
    print("Leaf values:",scores)
    print("Minimax value:",mini_value)
    print("Minimax evaluated leaves:",mini_count[0])
    print("Alpha-Beta value:",ab_value)
    print("Alpha-Beta evaluated leaves:",ab_count[0])
    print("Leaves pruned:",mini_count[0]-ab_count[0])
    print()

original=[3,5,2,9,3,5,2,9]
reordered=[9,2,5,3,9,2,5,3]

run_case("Original branch order",original)
run_case("Reordered branch order",reordered)