class DijkstrasHeap(object):
    """docstring for """

    def __init__(self,nodes,arc_lengths, source):
        self.nodes = nodes
        self.arc_lengths = arc_lengths 
        self.source = source

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