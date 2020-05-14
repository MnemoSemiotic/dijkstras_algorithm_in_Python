
class Graph: 
    def __init__(self, nodes_in_graph=[]):
        self.nodes_in_graph = nodes_in_graph

    def add_node(self, node):
        self.nodes_in_graph.append(node)

    def add_nodes(self, node_list):
        for node in node_list:
            self.add_node(node)


class Node:
    def __init__(self, nodename, connections):
        self.nodename = nodename
        self.connections = connections

        self.cost_table = {self.nodename: {'cost': 0, 'previous': None}}

        for name, cost in self.connections.items():
            self.cost_table[name] = {'cost': cost, 'previous': self.nodename}

    def __repr__(self):
        cost_table_header = '\tNode\tCost\tPrevious\n'
        cost_table_str = ''.join([f'\t{node}\t{vals["cost"]}\t{vals["previous"]}\n' for node, vals in self.cost_table.items()])

        return f'nodename: {self.nodename}\nconnections: {self.connections}\ncost_table:\n {cost_table_header}{cost_table_str}'

    def __str__(self):
        cost_table_header = '\tNode\tCost\tPrevious\n'
        cost_table_str = ''.join([f'\t{node}\t{vals["cost"]}\t{vals["previous"]}\n' for node, vals in self.cost_table.items()])

        return f'nodename: {self.nodename}\nconnections: {self.connections}\ncost_table:\n {cost_table_header}{cost_table_str}'

    def build_cost_table(self, graph):
        '''
        dijkstras

        Let cost from this node to itself = 0
        Populate the cost table entries with all nodes in the graph
        Let distance to all other nodes = 10**9 (e.g. infinity)

        Repeat:
            Visit the unvisited node with the smallest known distance from this start node
                For current node, examine its unvisited neighbors
                For current node, calc the distance of each neighbor from this start node
                if the calc'd distance of a node is less than the current distance in the cost_table, update the shortest distance in the cost table
                Update the previous node for each updated distance
                Add the current node to the list of visited nodes and remove it from the list of unvisited nodes
        Until all nodes are visited
        '''

if __name__ == '__main__':
    # define nodes
    A = Node('A', {'B': 5, 'C': 7, 'D': 2})
    B = Node('B', {'A': 5, 'E': 4})
    C = Node('C', {'A': 7, 'D': 3, 'F': 5})
    D = Node('D', {'A': 2, 'C': 3, 'E': 4, 'G': 6})
    E = Node('E', {'B': 4, 'D': 4, 'G': 2})
    F = Node('F', {'C': 5, 'G': 7, 'H': 6 })
    G = Node('G', {'D': 6, 'E': 2, 'F': 7, 'H': 3})
    H = Node('H', {'F': 6, 'G': 3})


    # print(A)

    graph = Graph()
    graph.add_nodes([A, B, C, D, E, F, G, H])

    print(graph.nodes_in_graph)
