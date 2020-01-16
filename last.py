# visits all the nodes of a graph (connected component) using BFS
import sys
from importlib import util
from timeit import default_timer as timer

# Load the model
if len(sys.argv) < 2:
    print("Error: No model specified.")
    quit()
print("Loading model from \"{0}\"...".format(sys.argv[1]), end="", flush=True)
spec = util.spec_from_file_location("model", sys.argv[1])
model = util.module_from_spec(spec)
spec.loader.exec_module(model)
network = model.Network()  # create network instance
print(" done.")
# Print some information about the model and the initial state
start_time = timer()
start = network.get_initial_state()
existingproperty = []


# print("The destination node of this transition is ", start)
# for checking state space


def graphwork(graph,start):

    explored = []
    queue = [start]
    cost = 0
    rewards = []
    while queue: 
               node = queue.pop(0)
               if node not in explored:
                   explored.append(node)
                   transitionstates = network.get_transitions(node)
                   for trans in transitionstates:
                      next_state = network.jump_np(node, trans, cost)
                      #rewards = [network.properties[0].exp.args[0]]
                      queue.append(next_state)
                      print(network.get_expression_value(next_state))
                      print(cost)
                     # print(network.transition_labels[trans.label])

    return explored


graphwork(network,start)