import numpy as np
import networkx as nx
import matplotlib.pyplot as mlib

def fun_conflict_serial(parameter1, parameter2): # function to check CS or not
    if parameter1 == "----" or parameter2 == "----":
        return False
    operator1, operator2 = parameter1[0], parameter2[0] # trans no
    data1, data2 = parameter1[2], parameter2[2]
    if operator1 == "W" or operator2 == "W": # either one of the operation is write operation
        if data1 == data2: # data same
            return True
    return False
file_path = input("Enter directory of input file ") # file path
with open(file_path) as file:
    line1 = file.readline().split(":")
    no_of_trans = len(line1[1].split(','))
twod = [[] for i in range(no_of_trans)] #2d array is created for storing transcations

with open(file_path) as file:
    for i in range(3):
        skip = file.readline() # three lines are skipped
    line = file.readline() # from this line transcations are there in file
    while line:
        l1 = line.split(":")
        transaction_no = int(l1[0][1])
        count = 0
        for i in range(len(twod)):
            if i == transaction_no - 1:
                twod[i].append(l1[1][:-2]) # is transcation then append
            else:
                twod[i].append("----") # if no transcation then append ----
        line = file.readline()

    print(twod)


G = nx.DiGraph()
for i in range(len(twod)):
    T_id = i
    G.add_node(T_id)

G.nodes()
length = len(twod[0])
for t_id in range(no_of_trans):
    for i in range(length):
        instruction = twod[t_id][i]
        for j in range(no_of_trans):
            if j == t_id:
                continue
            else:
                for k in range(i+1,length):
                    if fun_conflict_serial(instruction, twod[j][k]):
                        G.add_edge(t_id,j)

G.edges() # adding edes to graph
nx.draw(G, with_labels=True, font_weight='bold')
# mlib.show()
#nx.find_cycle(G)
try:
    nx.find_cycle(G)
    print("Schedule is not Conflict Serializable")
except:
    print("Schedule is Conflict Serializable")

print(nx.find_cycle(G))
