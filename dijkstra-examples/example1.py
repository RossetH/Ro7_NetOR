from algorithms import Dijkstras

source = 1

nodes = [1,2,3,4,5,6]

arc_lengths = {
    1: {2: 2, 3: 8},
    2: {3: 5, 4: 3},
    3: {2: 6, 5: 0},
    4: {3: 1, 5: 7, 6: 6},
    5: {4: 4},
    6: {5: 2}
    }

method = Dijkstras(nodes, arc_lengths, source)

method.solve()

len(method.visited) == len(nodes)

method.distance_label

method.predecessor