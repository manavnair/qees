# Run as python checker-demo.py model.py
# Requires Python 3.7 or newer

import sys

from importlib import util
from timeit import default_timer as timer
import heapq
import itertools


# Load the model
if len(sys.argv) < 2:
	print("Error: No model specified.")
	quit()
print("Loading model from \"{0}\"...".format(sys.argv[1]), end = "", flush = True)
spec = util.spec_from_file_location("model", sys.argv[1])
model = util.module_from_spec(spec)
spec.loader.exec_module(model)
network = model.Network() # create network instance
print(" done.")
explored = [] 
print("* The model has", len(network.properties), "properties.")
counter = 0
#checkproperty
ap_index=[]
#checkrewards
reward_exps=[]
#Cost_initially
cost = 0
#Initial_state
current_state = network.get_initial_state()
propertiesFound = [False] * len(network.properties) 
#cost_property

print("* The initial state is:", str(current_state))
#Queue
heap = []
counter = itertools.count()
#Dictionary
Dictionary={}
while(True):
    transitions = network.get_transitions(current_state)
    explored.append(current_state)
    for trans in transitions:
            print("transitions")
            next_state = network.jump_np(current_state, trans)  
            heapq.heappush(heap, (next(counter), next_state, current_state, trans))
            print("added to heap")
            
            
    priority, current_state, source, trans = heapq.heappop(heap)    
    Dictionary[current_state] = (source, trans) 
           
    for i in Dictionary:
        print(i)
           
    print("The amount of notes visited was:", len(explored))
         
    
    
  
        

