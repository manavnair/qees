from heapq import heappush, heappop
# Run as python checker-demo.py model.py
# Requires Python 3.7 or newer

import sys

from importlib import util
from timeit import default_timer as timer
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

minCostProperties = [] #Keep a list of all minimal cost properties
existProperties = [] #Keep a list of all minimal exist properties
visited = set() #Keep a list of all nodes we visited
propertiesFound = [False] * len(network.properties) #Keeps track of which properties have already been found

#Sort properties based on kind
print("* The model has", len(network.properties), "properties.")
counter = 0
for property in network.properties:
    if (property.exp is not None and property.exp.op == "exists" and property.exp.args[0].op == "eventually" and property.exp.args[0].args[0].op == "ap"):
        existProperties.append(counter) #We might have to use atomic proposition instead of index
    else: 
        minCostProperties.append(property.exp.args[1].args[0])
        
    counter = counter + 1    


print("* The model has", len(existProperties), "exist properties.")
print("* The model has", len(minCostProperties), "minimal cost properties.")
if len(minCostProperties)>1: 
    print("You have multiple minimal cost properties. This is not yet supported. Only the first one will be taken into consideration. ")

current_state = network.get_initial_state()
print("* The initial state is:", str(current_state))

#Initialize the priority heap queue
pq = []
cost = 0
#This counter is an ugly fix to prevent ties of cost values in the ordered queue. 
#If it wasn't included, the queue would try to compare two states to break the tie and give an error
counterTie = itertools.count()
trace = {}

while(True):
    #Add all of the transitions from current state to the priority queue
    transitions = network.get_transitions(current_state)
    for trans in transitions:
        costTemp = [0]
        if len(minCostProperties)>0:
            next_state = network.jump_np(current_state, trans, costTemp)
        else:
            next_state = network.jump_np(current_state, trans)
        
        if (next_state in visited) == False:
            #We store mutliple values in this heap so we can remember them when we need to add it to the dictionary
            heappush(pq, (costTemp[0]+cost, next(counterTie), next_state, current_state, trans))

        

    if (len(pq)==0):
        break
   #Get the next state and add to dictionary 
    cost, trash, current_state, source, trans = heappop(pq)    
    visited.add(current_state)
    
    #If there is already an entry in the dictionary, only replace if total cost is lower
    if current_state in trace:
        costT, sourceT, transT = trace[current_state]
        if cost+costTemp[0]<costT:
            trace[current_state] = (cost, source, trans)
    else:
        trace[current_state] = (cost, source, trans)  


    # Check if any exist properties hold. 
    for i in existProperties:
        if (network.get_expression_value(current_state, i)) == True and propertiesFound[i] == False:
            print("\n\nWe have found a trace where the property holds")
            propertiesFound[i] = True
            source = current_state   
            traceList = []
            while(source!=network.get_initial_state()):
                cost, source, trans = trace[source]
                traceList.append(network.transition_labels[trans.label])
                traceList.append(source)

            traceList.reverse()
            for item in traceList:
                print(str(item), end = ', ' )

            print("The amount of notes visited was:", len(visited))
           
            
    
    
    #Check if we satisfied a minimum property   
    counter = 0
    for i in minCostProperties:
        
        if (network.get_expression_value(current_state, i)) == True:
            print("We have found a path with a minimum cost value of ", cost)
            propertiesFound[counter] = True
            source = current_state   
            traceList = []
            while(source!=network.get_initial_state()):
                    cost, source, trans = trace[source]
                    traceList.append(network.transition_labels[trans.label])

            traceList.reverse()
            print(traceList)
            print("The amount of notes visited was:", len(visited))
        counter = counter+1  #Isn't this a bug? Wrong indentation?


     #If all properties have been found
    if ((False in propertiesFound) == False and len(network.properties)>0):
        break    



  
  
    
    

    


