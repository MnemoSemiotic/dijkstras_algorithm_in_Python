
class Graph: 


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
        pass

if __name__ == '__main__':
    # define nodes
    A = Node('A', {'B': 5, 'C': 7, 'D': 2})

    # print(A)

    graph = Graph()
    graph.add_nodes([A])
