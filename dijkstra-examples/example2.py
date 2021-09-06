from algorithms import Dijkstras

source = 's'

nodes = ['s','a','b','c','d','t']

arc_lengths = {
    's': {'a': 2, 'b': 1},
    'a': {'s': 3, 'b': 4, 'c':8},
    'b': {'s': 4, 'a': 2, 'd': 2},
    'c': {'a': 2, 'd': 7, 't': 4},
    'd': {'b': 1, 'c': 11, 't': 5},
    't': {'c': 3, 'd': 5}
    }

method = Dijkstras(nodes, arc_lengths, source)

method.solve()

len(method.visited) == len(nodes)

method.distance_label

method.predecessor