from algorithms import Dijkstras

source = 1

nodes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,
         15,16,17,18,19,20,21,22,23,24]

#TODO: Add an explanation of this instance/network
arc_lengths = {
    1:  {2: 1},
    2:  {3: 1, 11: 1, 23: 3},
    3:  {4: 1},
    4:  {5: 1, 9: 1, 21: 3},
    5:  {6: 1},
    6:  {7: 1},
    7:  {8: 1, 18: 1},
    8:  {5: 1, 9: 1},
    9:  {10: 1,},
    10: {3: 1, 11: 1},
    11: {12: 1},
    12: {1: 1},
    13: {12: 1, 14: 1},
    14: {15: 1, 23: 1},
    15: {16: 1},
    16: {17: 1, 21: 1},
    17: {18: 1},
    18: {19: 1},
    19: {20: 1},
    20: {5: 3, 17: 1, 21: 1},
    21: {22: 1},
    22: {3: 3, 15: 1, 23: 1},
    23: {24: 1},
    24: {13: 1} 
    }

method = Dijkstras(nodes, arc_lengths, source)

method.solve()

len(method.visited) == len(nodes)

method.distance_label

method.predecessor