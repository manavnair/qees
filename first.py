import sys
from importlib import util
from timeit import default_timer as timer
import itertools
import heapq

# Load the model
if len(sys.argv) <2:
	print("Error: No model specified.")
	quit()
print("Loading model from \"{0}\"...".format(sys.argv[1]), end = "", flush = True)
spec = util.spec_from_file_location("model", sys.argv[1])
model = util.module_from_spec(spec)
spec.loader.exec_module(model)
network = model.Network() # create network instance
print(" done.")
# Print some information about the model and the initial state
start_time = timer()
start=network.get_initial_state()
print("The destination node of this transition is ", start)

heap=[]
cost=0
reward_exps = []

Dictionary= {}               # mapping of tasks to entries

counter = itertools.count()     # unique sequence count


is_reward = network.properties[0].exp is not None and network.properties[0].exp.op == "xmin" and network.properties[0].exp.args[1].op == "ap"
if is_reward:
  reward_exps = [network.properties[0].exp.args[0]]
ap_prop =is_reach = network.properties[0].exp is not None and network.properties[0].exp.op == "exists" and network.properties[0].exp.args[0].op == "eventually" and network.properties[0].exp.args[0].args[0].op == "ap"
if ap_prop:
  ap_index=network.properties[0].exp.args[0].args[0].args[0]
#for checking state space
def bfs_connected_component(graph, start):

        # keep track of all visited nodes
   
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
     node = queue.pop(0)
     
     if node not in explored:
        explored.append(node)
        print(len(explored))
        transitions = network.get_transitions(node)
        #for  looping  
        for transition in transitions:
            #temperorary cost
              cost_initial=[0]
              #if is_reward:
                   #if cost property exists
              #    next_state = network.jump_np(node,transition,cost_initial)
              #else:
              next_state=network.jump_np(node,transition)
              print("The destination node of this transition is ",next_state)
              print("The index is ",network.transition_labels)
              queue.append(next_state) 
              print("property is", len(network.properties))
              
              # print(network.get_expression_value(next_state,ap_index)
              #will push everything in queue
             # heappush=(heap,(cost_initial+cost,next(counter),next_state,node,transition))
     return explored         
                                    
            #print(network.get_expression_value(next_state, ap_index))
    print("* The initial state has", str(len(transitions)), "transitions.")
    print("* The first transition out of the initial state is labelled:", network.transition_labels[transitions[0].label])            
    
    
#def property()

    
bfs_connected_component(network,start)
