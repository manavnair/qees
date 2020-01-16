from heapq import heappush,heappop
import sys
from importlib import util
from timeit import default_timer as timer
import itertools

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
  node=queue.pop(0)
  if node not in explored:
    # keep looping until there are nodes still to be checked
   print("The index is ", network.transition_labels )
   while(queue):
    transitions = network.get_transitions(start)
    #print("The transition taken is: ", )k.get_transitions(node)
    #print (network.transition_labels[explored[0].label])
    for trans in transitions:
                next_state = network.jump_np(node,trans)
                
                   
   
   print("The amount of notes visited was:", len(explored))   
   return explored
bfs_connected_component(network,start)