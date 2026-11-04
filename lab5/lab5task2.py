def minimax(depth,index,max_turn,scores,target,counter):
    if depth==target:
        counter[0]+=1
        return scores[index]

    if max_turn:
        left=minimax(depth+1,index*2,False,scores,target,counter)
        right=minimax(depth+1,index*2+1,False,scores,target,counter)
        return max(left,right)
    else:
        left=minimax(depth+1,index*2,True,scores,target,counter)
        right=minimax(depth+1,index*2+1,True,scores,target,counter)
        return min(left,right)

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

scores=[3,5,2,9,3,5,2,9]
target=3

minimax_count=[0]
minimax_value=minimax(0,0,True,scores,target,minimax_count)

alphabeta_count=[0]
alphabeta_value=alphabeta(0,0,True,scores,target,float("-inf"),float("inf"),alphabeta_count)

print("Minimax value:",minimax_value)
print("Minimax evaluated leaves:",minimax_count[0])
print("Alpha-Beta value:",alphabeta_value)
print("Alpha-Beta evaluated leaves:",alphabeta_count[0])
print("Leaves saved:",minimax_count[0]-alphabeta_count[0])