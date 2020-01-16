import sys
from importlib import util
from timeit import default_timer as timer

#LOAD THE MODEL

if len(sys.argv) < 2:
    print("Error: No model specified.")
    quit()
print("Loading model from \"{0}\"...".format(sys.argv[1]), end = "", flush = True)
spec = util.spec_from_file_location("model", sys.argv[1])
model = util.module_from_spec(spec)
spec.loader.exec_module(model)
network = model.Network() # create network instance
print(" done.")

#DONE!!!
#ap_index = network.properties[0].exp.args[0].args[0].args[0]
start_time = timer()
#STATE SPACE EXPLORER
def get_length(state): 
    return len(network.get_transitions(state))
#Function to return number of transitions from each state

def trans(state):
    return network.get_transitions(state)

#Function to fetch all transitions
     


initial_state = network.get_initial_state()

states = [initial_state]

#Breadth First Search
# def BFS(states):
#     parents = {}        
#     for i in states: 
#         transitions = trans(i)
#         for j in range(len(transitions)):
#             next_state = network.jump_np(i, transitions[j])
#             parents[str(next_state)] = i
#             if(next_state not in states):
#                 states.add(next_state)
#     for x, y in parents.items():
#         print(x,"---->", y)             


def BFS():
    
    initial_state = network.get_initial_state()
    cur_state = initial_state
    visited = {initial_state}
    parents = {}
    queue = []
    queue.append(initial_state)
    
    expression = False

    cur_state = initial_state

    reward_exps = [network.properties[0].exp.args[0]]
    
    while queue:
        
        transitions = trans(cur_state)
        queue.pop(0)
        childrenTuple = ()
        
        for j in range(len(transitions)):
            if expression == False:
                next_state = network.jump_np(cur_state, transitions[j],reward_exps)
                expression = network.get_expression_value(next_state,1)
                
                if(next_state not in visited):   
                    temp = list(childrenTuple)
                    print(reward_exps)
                    print(str(next_state))
                    visited.add(next_state)
                    queue.append(next_state)
                    if str(cur_state) not in temp:    
                        temp.append(str(cur_state))
                
                else:
                    temp = list(parents[str(next_state)])
                    if str(cur_state) not in temp:
                        temp.append(str(cur_state))                    
                
            childrenTuple = tuple(temp)
            parents[str(next_state)] = childrenTuple 

        cur_state = queue[0]
           
        if expression:
            print("Property becomes true at --->", str(next_state))
            break
    
    if expression == False:    
        print("Property does not hold")

    #for x, y in parents.items():
    #     print("Child =",x,"---->","Parent =", y)
    
    
    cur_state = str(next_state)
    initial_state = str(initial_state)
    
    #print("!!!!",str(cur_state))
    
    #while(cur_state != initial_state):
    #    parent = parents[cur_state][0]
    #    print(parent)
    #    cur_state = str(parent)
    return visited


#BFS(states)
#for k in range(len(states)):
#    print(str(states[k]))

#Depth First Search
def DFS():
    visited = {initial_state}
    stack = [initial_state]
    cur_state = initial_state
    expression = False
    parents = {}
    for i in stack: 
        for j in range(len(trans(i))):
            if expression == False:
                next_state = network.jump_np(i, trans(i)[j])
                n = str(next_state)
                parents[n] = cur_state 
                stack.append(next_state)
                expression = network.get_expression_value(next_state,0)
                if next_state not in visited:
                    visited.add(next_state)
                    cur_state = next_state    
                else:
                    stack.pop()
            else:
                print("Property becomes true at", str(cur_state))
                break
    if expression == False:    
        print("Property does not hold")    
    
    #for x, y in parents.items():
    #    print("Child =",x,"---->","Parent =", y)
    
    return visited

##---------------##---------------------##------------------------##---------------------##

def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if network.get_expression_value(array[j],0) > network.get_expression_value(array[j+1],0):
                array[j], array[j+1] = array[j+1], array[j]

def BestFS():
    pq = [(initial_state,None)]
    closed = [initial_state]
    reward_exps = [network.properties[0].exp.args[0]]
    rew = []
    expression = False
    
    while pq:
        cur_state = pq[0][0]
        transitions = network.get_transitions(cur_state)
        pq.pop(0) 
        for i in range(len(transitions)):
            if expression == False:
                next_state = network.jump_np(cur_state, transitions[i], reward_exps)
                expression = network.get_expression_value(next_state,1)
                pq.append((next_state,reward_exps))
            
        for j in range(len(pq)):
            for k in range(len(pq) - j - 1):
                if pq[k][1][0] > pq[k+1][1][0]:
                    pq[k],pq[k+1] = pq[k+1],pq[k]













## --------------##---------------------##----------------------------##---------------------

#states = {*DFS()}

states = BFS()

#print("The BFS traversal is:")
#for k in states:
#    print(str(k))

    #if network.get_expression_value(i,0):
    #    print("YES")
    #    break

#states = BestFS()
#reward = 0

#for k in states:
    #reward += network.get_expression_value(k, 0)
    #print(reward)
#    print(str(k))


#ADD PROPERTIES HERE
props = []

for i in range(len(network.properties)):
    props.append(str(network.properties[i]))

print("NUMBER OF STATES ------>", len(states))
end_time = timer()
print("Done in {0:.2f} seconds.".format(end_time - start_time))

#reward = network.properties[2].exp.args[0]
#ap_index = network.properties[0].exp.args[0].args[0].args[0]

#print("The properties are", props)

#print("The total reward is ", reward)

#print("AP INDEX =", ap_index)

#print("The reward is", reward)