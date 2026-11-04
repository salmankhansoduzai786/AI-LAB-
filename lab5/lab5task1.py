import math

def minimax(depth,index,max_turn,scores,target_depth):
    if depth==target_depth:
        return scores[index]

    if max_turn:
        left=minimax(depth+1,index*2,False,scores,target_depth)
        right=minimax(depth+1,index*2+1,False,scores,target_depth)
        return max(left,right)
    else:
        left=minimax(depth+1,index*2,True,scores,target_depth)
        right=minimax(depth+1,index*2+1,True,scores,target_depth)
        return min(left,right)

scores=[3,5,2,9,0,7]
target_depth=math.ceil(math.log2(len(scores)))
scores += [0]*(2**target_depth-len(scores))

print("Leaf values:",scores)

level2=[max(scores[i],scores[i+1]) for i in range(0,len(scores),2)]
print("Level 2 MAX values:",level2)

level1=[min(level2[i],level2[i+1]) for i in range(0,len(level2),2)]
print("Level 1 MIN values:",level1)

result=minimax(0,0,True,scores,target_depth)
print("Optimal Minimax value:",result)