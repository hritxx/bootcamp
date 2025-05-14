import json

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_edge(self, from_node, to_node):
        self.nodes.update([from_node, to_node])
        self.edges.append((from_node, to_node))

    def to_dict(self):
        return {"nodes": list(self.nodes), "edges": self.edges}

    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        graph = cls()
        graph.nodes = set(data['nodes'])
        graph.edges = data['edges']
        return graph