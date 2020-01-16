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
is_reward = network.properties[0].exp is not None and network.properties[0].exp.op == "xmin" and network.properties[0].exp.args[1].op == "ap"
if is_reward:
  reward_exps.append(network.properties[0].exp.args[0])
#exist_property
ap_prop = network.properties[0].exp is not None and network.properties[0].exp.op == "exists" and network.properties[0].exp.args[0].op == "eventually" and network.properties[0].exp.args[0].args[0].op == "ap"
if ap_prop:
  ap_index.append(network.properties[0].exp.args[0].args[0].args[0])

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
            costTemp=[0]
            if is_reward is True:
                next_state=network.jump_np(cost,current_state,trans)
            else :   
                next_state = network.jump_np(current_state, trans)  
            heapq.heappush(heap, (costTemp[0]+cost, next(counter), next_state, current_state, trans))
            print("added to heap")
            

    cost, priority, current_state, source, trans = heapq.heappop(heap)    
    Dictionary[current_state] = (cost, source, trans) 
         
    for i in Dictionary:
        print(i)
           
    for i in ap_index:        
        
       if (network.get_expression_value(current_state, i)) == True and propertiesFound[i] == False:
            print("\n\nWe have found a trace where the property holds")
            propertiesFound[i] = True
            source = current_state   
            traceList = []
            while(source!=network.get_initial_state()):
                cost, source, trans = trace[source]
                traceList.append(network.transition_labels[trans.label])
                traceList.append( )

            traceList.reverse()
            for item in traceList:
                print(str(item), end = ', ' )

            print("The amount of notes visited was:", len(visited))
         
    
    
  
        

