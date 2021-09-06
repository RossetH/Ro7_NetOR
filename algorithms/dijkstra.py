class Dijkstras(object):
    """docstring for implementation of Dijkstra's algorithm to 
    find the shortest path from the source node to all other
    nodes in a network with nonnegative arc lengths. Based on
    Dijkstra's algorithm presenetd by Ahuja's Network flows 
    book"""
    
    def __init__(self, nodes, arc_lengths, source):
        self.nodes = nodes
        self.arc_lengths = arc_lengths 
        self.source = source
        self.visited = []
        self.unvisited = nodes.copy()
        self.distance_label = dict.fromkeys(nodes,float('inf'))
        self.predecessor = dict.fromkeys(nodes,None)

    def get_min_distance_label(self):
        subdict = {
            x: self.distance_label[x] 
            for x in self.unvisited if x in self.distance_label
        }
        return min(subdict, key=subdict.get)

    def solve(self):
        self.distance_label[self.source] = 0
        self.predecessor[self.source] = 0
        while len(self.visited) < len(self.nodes):
            i = self.get_min_distance_label()
            self.visited.append(i)
            self.unvisited.remove(i)
            adjacent_nodes = list(self.arc_lengths[i].keys())
            for adjacent in adjacent_nodes:
                if self.distance_label[adjacent] > self.distance_label[i] + self.arc_lengths[i][adjacent]:
                    self.distance_label[adjacent] = self.distance_label[i] + self.arc_lengths[i][adjacent]
                    self.predecessor[adjacent] = i

if __name__ == '__main__':

    nodes = [1,2,3,4,5,6]

    arc_lengths = {
        1: {2: 6, 3: 4},
        2: {3: 2, 4: 2},
        3: {4: 1, 5: 2},
        4: {6: 7},
        5: {4: 1, 6: 3}
        }

    source = 1

    method = Dijkstras(nodes,arc_lengths,source)

    method.solve()