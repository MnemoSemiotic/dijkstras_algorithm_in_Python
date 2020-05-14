

class Node:
    def __init__(self, nodename, connections):
        self.nodename = nodename
        self.connections = connections

        self.cost_table = {self.nodename: {'cost': 0, 'previous': None}}

        for name, cost in self.connections.items():
            self.cost_table[name] = {'cost': cost, 'previous': self.nodename}

    # def __repr__(self):




if __name__ == '__main__':
    # define nodes
    A = Node('A', {'B': 5, 'C': 7, 'D': 2})

    print(A)