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
# Print some information about the model and the initial state
start_time = timer()
start=network.get_initial_state()
print("The destination node of this transition is ", start)

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
            # add node to list of checked nodes
            explored.append(node)
            print(len(explored))
            transitions = network.get_transitions(node)

           # print("The transition taken is: ", )
            #print (network.transition_labels[explored[0].label])
            for trans in transitions:
                next_state = network.jump_np(node, trans)
                print("The destination node of this transition is ", next_state)
                print("The index is ", network.transition_labels )
                queue.append(next_state)
                print("property is", len(network.properties))

                ap_index=network.properties[0].exp.args[0].args[0].args[0]
                print(network.get_expression_value(next_state, ap_index))
            if (network.get_expression_value(next_state, ap_index)) == True:
                            break

    return explored

#for checking properties

bfs_connected_component(network,start)
bfs_properties()# visits all the nodes of a graph (connected component) using BFS
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
# Print some information about the model and the initial state
start_time = timer()
start=network.get_initial_state()
print("The destination node of this transition is ", start)

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
            # add node to list of checked nodes
            explored.append(node)
            print(len(explored))
            transitions = network.get_transitions(node)

           # print("The transition taken is: ", )
            #print (network.transition_labels[explored[0].label])
            for trans in transitions:
                next_state = network.jump_np(node, trans)
                print("The destination node of this transition is ", next_state)
                print("The index is ", network.transition_labels )
                queue.append(next_state)
                print("property is", len(network.properties))

                ap_index=network.properties[0].exp.args[0].args[0].args[0]
                print(network.get_expression_value(next_state, ap_index))
            if (network.get_expression_value(next_state, ap_index)) == True:
                            break

    return explored

#for checking properties

bfs_connected_component(network,start)
bfs_properties()