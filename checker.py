# visits all the nodes of a graph (connected component) using BFS
import sys
from importlib import util
from timeit import default_timer as timer

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
start_time = timer()
start=network.get_initial_state()
print("The destination node of this transition is ", start)
#for checking state space

def bfs_connected_component(graph, start):
pq[]#queue 
 # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    minCostProperties = []  # Keep a list of all minimal cost properties
    existProperties = []  # Keep a list of all minimal exist properties
    propertiesFound = [False] * len(network.properties)  # Keeps track of which properties have already been found

    # Sort properties based on kind
    print("* The model has", len(network.properties), "properties.")
    counter = 0
    for property in network.properties:
        if (property.exp is not None and property.exp.op == "exists" and property.exp.args[0].op == "eventually" and
                property.exp.args[0].args[0].op == "ap"):
            existProperties.append(counter)  # We might have to use atomic proposition instead of index
        else:
            minCostProperties.append(property.exp.args[1].args[0])

        counter = counter + 1


    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        count=0;
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            print(len(explored))
            transitions = network.get_transitions(node)
           # print("The transition taken is: ", )
            #print (network.transition_labels[explored[0].label])
            for trans in transitions:
            ###############costproperty
            if minCostProperties>0
                 # print("The destination node of this transition is ", next_state)
                   next_state = network.jump_np(node, trans,cost)
                 else
                   next_state = network.jump_np(node, trans)
              heappush(pq,())          
              #  print("The index is ", network.transition_labels)
                queue.append(next_state)

        # Check if any exist properties hold.
        for i in existProperties:
            if (network.get_expression_value(node, i)) == True and propertiesFound[i] == False:
                print("\n\nWe have found a trace where the property holds")
                propertiesFound[i] = True
                source = node
            


        # Check if we satisfied a minimum property
        counter = 0
       
    return explored
en
        #for checking properties

bfs_connected_component(network,start)







