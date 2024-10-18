def minimax(depth,nodeIndex,maximizingPlayer,values,alpha,beta):
    if depth==3:
        return values[nodeIndex]
    
    if maximizingPlayer:
        maxEval=float('-inf')
        for i in range(2):
            eval=minimax(depth+1,nodeIndex * 2 + i,False,values,alpha,beta)
            maxEval=max(maxEval,eval)
            alpha=max(alpha,eval)
            if beta <= alpha:
                break
        return maxEval

    else:
        minEval=float('inf')
        for i in range(2):
            eval=minimax(depth+1,nodeIndex * 2 + i,True,values,alpha,beta)
            minEval=min(minEval,eval)
            beta=min(beta,eval)
            if beta <= alpha:
                break
        return minEval
    

if __name__ == "__main__":
        values=[3,5,6,9,1,2,0,-1]
        optimal_value=minimax(0,0,True,values,float('-inf'),float('inf'))
        print("The optimal value is :",optimal_value)



b.Implement hill climbing problem. 

Code:
import random
def objective_function(x):
    return -x**2 + 4*x

def generate_neighbor(current_x,step_size):
    return current_x+random.uniform(-step_size,step_size)

def hill_climbing(starting_point,step_size,max_iterations):
    current_x=starting_point
    current_value=objective_function(current_x)

    for _ in range(max_iterations):
        neighbor_x=generate_neighbor(current_x,step_size)
        neighbor_value=objective_function(neighbor_x)

        if neighbor_value>current_value:
            current_x=neighbor_x
            current_value=neighbor_value

    return current_x,current_value

starting_point=random.uniform(0,4)
step_size=0.1
max_iterations=100

best_x,best_value=hill_climbing(starting_point,step_size,max_iterations)

print(f"Best x:{best_x},Best value: {best_value}")
